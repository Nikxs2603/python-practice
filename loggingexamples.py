import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
#setting the level for the handle
stream_h.setLevel(logging.DEBUG)
file_h.setLevel(logging.ERROR)
#setting a formatter
stream_f = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d %m %Y : %H %M %S')
stream_h.setFormatter(stream_f)
file_h.setFormatter(file_f)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('This is an error')
logger.debug('this is debugging')