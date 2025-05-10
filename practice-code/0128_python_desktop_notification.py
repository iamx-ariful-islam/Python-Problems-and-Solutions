# pip install plyer

from plyer import notification


def get_notification():
    notification.notify(
        title = 'Alert!!!',
        message = 'Take a break! It has been an hour!',
        timeout = 10
    )

if __name__ ==  '__main__':
    get_notification()