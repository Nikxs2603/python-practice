import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#roll over 1kb, and keep backup log app.log1, app.log2 etc
handler = RotatingFileHandler('app.log', maxBytes=1000, backupCount=2)
logger.addHandler(handler)
for _ in range(10):
    logger.info('hello there')

#Timedrotatingfilehandler
import logging
from logging.handlers import TimedRotatingFileHandler
import time
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#This will create a new log file every 5 seconds, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timedapp.log', when='s', interval=5, backupCount=4)
logger.addHandler(handler)
for _ in range(6):
    logger.info('testing timed rotating file handler')
    time.sleep(10)


