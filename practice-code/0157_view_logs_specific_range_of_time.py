from re import search
from pathlib import Path


# set or input start date time
start_time = 'Mar 19 02:00'

# set or input end date time
end_time = 'Mar 19 02:15'

log_lines = Path('/var/log/syslog').read_text().splitlines()

for x in log_lines:
    log_time = search(r'^\w{3}\s+\d+\s\d{2}:\d{2}', x).group()
    if start_time <= log_time <= end_time:
        print(x)