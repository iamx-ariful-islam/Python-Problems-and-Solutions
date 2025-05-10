import logging


# set the message format
format_msg = "[%(asctime)s] - %(levelname)s - [%(filename)s %(name)s %(funcName)s (%(lineno)d)]\t- %(message)s"
logging.basicConfig(filename=("app.log"), level=logging.DEBUG, format=format_msg) # configure the logger message format

# store the logger data
logging.debug('this is the test')