# Import all the modules required
import hashlib
import json
import multiprocessing
import os
import subprocess
import sys
import time

# import logging function
from . import logger
log = logger.log

#****************************#
# Utility functions
#****************************#
def getTime(format=None):
    ''' Return a formated current date time (Default: dd-mm-yyyy HH:mm:ss)'''
    if not format:
        return time.strftime("%c")
    return time.strftime(format)

def runCmd(command, shell=False, cont=False, debug=False, log=None, close_fds=False, **kwargs):
    ''' Run system commands (Supports both linux and Windows) '''

    # Create an empty return payload
    payload = {'result': None, 'error': None, 'status': False, 'start_time': None, 'end_time': None, 'time': None, 'cmd': str(command)}
    try:
        command_string = command if shell else subprocess.list2cmdline(command)

        # Print the running command only if debug is True
        if debug: print ("Running {}".format(command_string))

        # Capture the start time
        payload['start_time'] = time.time()

        # Run the command
        result = subprocess.Popen(command, 
            shell=shell, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            close_fds=close_fds,
            cwd=kwargs['cwd'] if 'cwd' in kwargs.keys() else None
        )

        cmd_output, cmd_err = result.communicate()
        payload['end_time'] = time.time() # Capture the end time
        payload['time'] = (payload['end_time'] - payload['start_time']) / 60 # Calculate the time taken for the subprocess

        with open(log, "a+") as log_obj:
            log_obj.write(str(cmd_output))
            log_obj.write("\nERROR:\n{}".format(str(cmd_err)))
            log_obj.write("\nTime:\n{}".format(str(payload['time'])))

        if result.returncode == 0: # Get the result output of the command
            payload['result'] = cmd_output if cmd_output else None
            payload['status'] = True
        else: # Get the error output of the command
            payload['error'] = cmd_err if cmd_err  and 'Removing leading' not in cmd_err else None

    except subprocess.CalledProcessError as err:
        log.error('{}'.format(err))
        payload['error'] = str(err)
        if not cont:
            sys.exit(1)
    finally:
        return payload

def md5sum(file=None, debug=False):
    if not file:
        return None
    try:
        result = hashlib.md5(file)
        if debug: log.debug ("{}: Md5Sum ({})".format(str(file), str(result))) # Print the MD5 value if debug is set to True
        return result.hexdigest()
    except Exception as err:
        log.error("{}".format(err))
        return None

#****************************#
# File and Directory functions
#****************************#
def makeDir(path=None):
    if not path:
        return False
    try:
        os.makedirs(path)
        return True
    except OSError as err:
        if not os.path.isdir(path):
            return True
        log.error("{}".format(err))
        return False

def readJson(filename):
    ''' Read a JSON file '''
    source_file = filename
    try:
        if os.path.isfile(source_file):
            with open (source_file) as file_obj:
                return json.load(file_obj)
        log.error("Unable to find {}".format(source_file))
        return False
    except Exception as err:
        log.error('{}'.format(err))
        return False

def writeJson(filename, data):
    ''' Write to a JSON file '''
    try:
        with open(filename, 'w+') as file_obj:
            json.dump(data, file_obj, sort_keys=True)
            return True
    except IOError as err:
        log.error("{}".format(str(err)))
        return False
    except Exception as err:
        log.error("{}".format(str(err)))
        return False

def checkFile(filename=None):
    if filename:
        try:
            return os.path.isfile(filename)
        except Exception as err:
            log.error("{}".format(str(err)))
            return False
    log.error("Filename not passed (recieved none)")
    return False

#****************************#
# Helper classes
#****************************#
class Console():
    ''' '''
    def __init__(self, log_path, debug=False):
        self.debug = debug
        self.log_path = log_path

    def display(self, message):
        if self.debug: print (message)

    def banner(self, title='', char='*', length=50):
        title = title.upper()
        print ("")
        print (title.center(length, char))
        print ("")


if __name__ == "__main__":
    pass