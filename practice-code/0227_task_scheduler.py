# pip install schedule

import time
import schedule


def job():
    print("Running scheduled task!")

# schedule the task to run every day at 10:00 AM
schedule.every().day.at("10:00").do(job)
# or
# schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)