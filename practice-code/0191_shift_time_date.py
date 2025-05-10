from datetime import datetime, timedelta

__now   = datetime.now() # current date
#__today = __now.strftime("%d.%m.%Y") # if need then use format
print(__now)
__after = __now + timedelta(days=10) # after 10 days
#__after = __after.strftime("%d.%m.%Y") # if need then use format
print(__after)


'''output:

2024-02-05 21:59:23.664042
2024-02-15 21:59:23.664042

if use format
05.02.2024
15.02.2024
'''