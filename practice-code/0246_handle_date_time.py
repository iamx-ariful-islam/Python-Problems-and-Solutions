# pip install arrow

import arrow


now = arrow.now()
print(now.format('YYYY-MM-DD HH:mm:ss'))
print(now.shift(hours=+2).format('YYYY-MM-DD HH:mm:ss'))



'''output:

2025-02-12 18:36:38
2025-02-12 20:36:38
'''