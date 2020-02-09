# /usr/bin/python
'''
    Get system information based on type OS (Linux/Windows/Mac).
'''
# Import all the modules required
import multiprocessing
import os
import platform

# import logging function
from . import logger
log = logger.log

class Platform(object):
    ''' Get generalized wrapper based on type of platform Linux/Windows
        Windows: system, architecture, hostname, kernel/release, version, processor, 
    '''
    def __init__(self, debug=True, cont=True):
        self.debug = debug
        self.cont = cont
        self.platform = None
        self.Platform = dict()
        self.run()
    
    def run(self):
        ''' Initiate the class objects and returns the defaults '''
        # Get details that are not based on OS
        self.Platform['hostname'] = self.get_hostname()

        # Get details that are based on OS
        self.Platform['os'] = self.get_platform()
        self.Platform['distribution'] = self.get_distribution()
        self.Platform['kernel'] = self.get_kernel()
        self.Platform['version'] = self.get_version()
        self.Platform['architecture'] = self.get_architecture()
        self.Platform['cores'] = self.get_corecount()
        self.Platform['username'] = self.get_user()

    def __doc__(self):
        'DOC how is it going'

    def get_platform(self):
        current_platform = str(platform.system().strip().lower())
        if current_platform:
            self.platform = current_platform
            return current_platform
        if self.debug and not current_platform:
            log.error("Unable to determine OS platform")
        return False

    def get_hostname(self):
        hostname = str(platform.node().strip().lower())
        if hostname:
            return hostname
        if self.debug and not hostname:
            log.error("Unable to determine hostname")
        return False

    def get_distribution(self):
        if self.platform == 'linux':
            return str("-".join(platform.linux_distribution()[0].strip()))
        elif self.platform == 'windows':
            return str(platform.platform().strip().lower())
        elif self.debug:
                log.error("Unable to determine for {} distribution".format(self.platform))
        return False

    def get_kernel(self):
        kernel = str(platform.release().strip().lower())
        if kernel:
            return kernel
        if self.debug and not kernel:
            log.error("Unable to determine kernel/release")
        return False

    def get_version(self):
        if platform.version():
            return str(platform.version().strip().lower())
        if self.debug:
            log.error("Unable to determine OS version")
        return False

    def get_architecture(self):
        if platform.machine():
            return str(platform.machine().strip().lower())
        if self.debug:
            log.error("Unable to determine OS architecture")
        return False

    def get_corecount(self):
        core_count = str(multiprocessing.cpu_count())
        return core_count if core_count else None
        
    def get_user(self):
        return (lambda: os.environ["USERNAME"] if "C:" in os.getcwd() else os.environ["USER"])()

# General purpose functions
def chk_support(os, os_chk):
    if not os_chk or str(type(os_chk)) == 'dict' and os not in os_chk.keys() or not os_chk[os] or str(type(os_chk)) == 'list' and os not in os_chk or str(type(os_chk)) == 'string' and os != os_chk:
        log.error("Error: OS '{}' is currently not supported/enabled for the framework".format(os))
        return False
    return True

def chk_distribution(dist, dist_chk):
    if not dist_chk or str(type(dist_chk)) == 'dict' and dist not in dist_chk.keys() or str(type(dist_chk)) == 'list' and str(dist) not in dist_chk or str(type(dist_chk)) == 'string' and dist != dist_chk:
        log.error("Error: Distribution '{}' is currently not supported/enabled for the framework".format(dist))
        return False
    return True