from pathlib import Path
from re import compile, search
from os import statvfs_result as svfs


comp  = compile(r'^/dev/(?!.*snap)')
mline = Path('/proc/mounts').read_text().splitlines()
fs    = [i.split()[1] for i in mline if comp.search(i)]

for x in fs:
    def usep(x, y):
        return f"{(x-y)/x:0%}"
    percent = usep(svfs(x).f_blocks, svfs(x).f_bfree)
    if int(percent.replace('%', '')) > 80:
        print(f'Running out of space {x} above {percent:80}')