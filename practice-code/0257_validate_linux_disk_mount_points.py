from re import search
from pathlib import Path


fstab_read = Path('/etc/fstab').read_text().splitlines()
fstab      = {x.split()[1] for x in fstab_read if x.startswith('UUID')}

mounts_read = Path('/proc/mounts').read_text().splitlines()
mounts      = {y.split()[1] for y in mounts_read if search(r'^/dev/(?!.*snap)', y)}

output = fstab - mounts

if not output:
    print('All disks are mounted correctly')
else:
    print('These mount point not mounted:', *output, sep='\n')