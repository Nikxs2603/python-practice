import logging
import traceback
try:
    a = [1,2,3,4]
    value = a[5]
# except IndexError as e:
#     logging.error(e, exc_info=True)
except:
    logging.error("the error is %s", traceback.format_exc())