#!/usr/bin/python

''' PYTHON FRAME WORK '''

# Import all the standard python libraries
import sys

# Import Jarvis framework libraries
try:
    from lib import arguments, system, handler, logger, mail
except ImportError as err:
    print ("Error:\n{}".format(str(err)))
    sys.exit(1)

# Global variables
__SYSTEM_INFO__ = dict()
__ARGS__ = None
__LOG_INI__ = 'config/logger.ini'

# Import config from logging
import logging.config

# Load logging configuration for logging
logging.config.fileConfig(__LOG_INI__)

# Load the logger into a log variable
log = logger.log

# Read the framework config
try:
    from config.default import config as DEFAULT_CFG
except ImportError as err:
    print ("Error:\n{}".format(str(err)))
    sys.exit(1)

# Run argument checks
__ARGS__ = arguments.check_args(DEFAULT_CFG)
if not __ARGS__:
    log.info("Argument check ... FAILED")
    sys.exit(1)
#log.info("Argument check ... DONE")

# Create the log folder
if not handler.makeDir(__ARGS__.log):
    log.error("Unable to create log folder")
    sys.exit(1)

# Write the arguments recived to 'args.json'
handler.writeJson(__ARGS__.log + '/args.json', vars(__ARGS__))

# Gather the system information
__SYSTEM_INFO__ =  system.Platform().Platform
#log.info("System check ... DONE")

# Write the system information to 'system.json'
handler.writeJson(__ARGS__.log + '/system.json', __SYSTEM_INFO__)

# Run system check for OS and distribution support
if not system.chk_support(__SYSTEM_INFO__['os'], DEFAULT_CFG['os']['supported']):
    sys.exit(1)
if not system.chk_distribution(__SYSTEM_INFO__['kernel'], DEFAULT_CFG['os']['distribution'][__SYSTEM_INFO__['os']]):
    sys.exit(1)

# Print out system details and arguments list if 'debug' is True
if __ARGS__.debug:
    print(__ARGS__.debug)
    print ("")
    print (" System Info ".center(65, "*"))
    for key, val in __SYSTEM_INFO__.items():
        print ("{}: {}".format(key, val))
    print ("".center(65, "*"))

    print ("")
    print (" Arguments ".center(65, "*"))
    for args in vars(__ARGS__):
        print ("{}: {}".format(args, __ARGS__.__getattribute__(args)))
    print ("".center(65, "*"))
    print ("")

# Pass the args list to the respective module.
submodule = __ARGS__.command
try:
    log.info("Initiating {} module".format(str(submodule)))
    module = __import__("modules.{}.run".format(str(submodule)), fromlist=['modules.{}'.format(str(submodule))])
    dir(module.run(arguments=__ARGS__, system=__SYSTEM_INFO__))
except ImportError as err:
    print ("Error:\b{}".format(err))
    sys.exit(1)