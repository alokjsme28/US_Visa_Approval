from us_visa.logger import logging
from us_visa.exception import USvisaexception
import sys

logging.info('Trying Exception')
try:
    a = 1/0
except Exception as ex:
    raise USvisaexception(ex,sys)