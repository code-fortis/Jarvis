# Import all the modules required
import logging

# Setup log variable to be exported out
log = logging.getLogger('logger')

# Function: runExample
# Allows developer to test the logger prehand.
def runExample():
    log.debug('debug message')
    log.info('info message')
    log.warning('warning message')
    log.error('error message')
    log.critical('critical message')
    log.exception('exception message')

# Set the log file name
def setLogFile(filename):
    log.addHandler(logging.handlers.RotatingFileHandler(filename))
