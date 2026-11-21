"""Download pinned public skill sources without replacing an existing install."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

def run(*args,cwd=None):
    return subprocess.check_output(args,cwd=cwd,text=True,encoding='utf-8',stderr=subprocess.STDOUT).strip()

def install(target,platform='all'):
    catalog=json.loads((Path(__file__).parent/'catalog.json').read_text(encoding='utf-8'))
    chosen=[p for p in catalog['projects'] if platform=='all' or p['platform']==platform]
    if not chosen:raise ValueError('Unknown platform')
    for p in chosen:
        if not re.fullmatch('[a-z0-9-]+',p['skill']) or not re.fullmatch('[a-f0-9]{40}',p['commit']):raise ValueError('Invalid catalog entry')
        if (target/p['skill']).exists():raise FileExistsError(f"目标目录已存在，不覆盖: {target/p['skill']}")
        if not re.fullmatch(r'https://github.com/dstmg/[a-z0-9-]+',p['repository']):raise ValueError('Unexpected repository URL')
    # Validate every download before writing any installation directory.
    with tempfile.TemporaryDirectory(prefix='keyword-skills-') as tmp:
        staged=[]
        for p in chosen:
            source=Path(tmp)/p['platform']
            run('git','clone','--quiet','--no-checkout',p['repository']+'.git',str(source))
            run('git','checkout','--quiet','--detach',p['commit'],cwd=source)
            if run('git','rev-parse','HEAD',cwd=source)!=p['commit']:raise ValueError('Commit mismatch')
            skill=(source/'SKILL.md').read_text(encoding='utf-8-sig')
            if not re.search(r'^name:\s*'+re.escape(p['skill'])+r'\s*$',skill,re.M):raise ValueError('Skill name mismatch')
            if 'MIT License' not in (source/'LICENSE').read_text(encoding='utf-8'):raise ValueError('License mismatch')
            staged.append((p,source))
        target.mkdir(parents=True,exist_ok=True)
        for p,source in staged:
            shutil.copytree(source,target/p['skill'],ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
            print(p['platform']+': '+p['commit']+' -> '+str(target/p['skill']))
    return len(chosen)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target',required=True,type=Path,help='Agent skill parent directory')
    parser.add_argument('--platform',choices=['all','xianyu','xiaohongshu','douyin'],default='all')
    args=parser.parse_args()
    print('Installed projects:',install(args.target.resolve(),args.platform))
