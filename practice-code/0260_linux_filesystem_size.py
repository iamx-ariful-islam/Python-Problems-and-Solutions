from pathlib import Path
from subprocess import check_output as cmd


output = [i for i in cmd(['df', '-h']).decode().splitlines()]
dev    = [i.split()[-2:] for i in output if i.startswith('/dev/sd')]
result = [i for i in dev if int(i[0].strip('%')) > 50]
final  = [(Path(k).parts[-1], j) for j, k in result]

print('{:15} {:^14}'.format('Filesystem', 'Used'))
print('*'*26)
for x, y in final:
    print('{:21} {}'.format(x, y))