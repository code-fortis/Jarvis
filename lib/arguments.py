#!/usr/bin/python
# Import all the modules required
import argparse
from lib import handler
__version__ = 1.0

def check_args(configuration):
    __ARGS__ = None

    # Create parent level argumentParser object
    parser = argparse.ArgumentParser(
        prog='jarvis',
        description='Python Framework v{}'.format(str(__version__)),
        epilog='Note: For additional help, run jarvis <module> --help'
    )

    # Default arguments for the framework. Default arguments can be overriden by the modules if declared.
    parser.add_argument('--debug', action='store_true', help='Enables debug mode.')
    parser.add_argument('--log', required=False, action='store', help='Path to log directory')

    # Create a subparser object for the modules that will be added later on in this script.
    subparsers = parser.add_subparsers(
        title='Available Modules',
        help='For additional help, run jarvis <module> --help',
        #description='valid subcommands',
        dest='command'
    )

    # if modules are found in configuration file, import them.
    if not configuration['modules']:
        parser.error("No modules found to load")
        return False
    import_submodules(configuration['modules'], subparsers)

    # Read and parse the arguments
    __ARGS__ = parser.parse_args()
    # Check if any module has been called or not
    if not __ARGS__.command:
        parser.error("No modules where passed")
        return False

    # Retun False if argument has been returned empty else override 
    # arguments with some defaults and return it
    return False if not __ARGS__ else override_args(__ARGS__, configuration)

#*******************************************************#
# Import all modules with status set to 'True'
# for argparse check
#*******************************************************#
def import_submodules(modules, subparsers):
    for mod, mod_prop in modules.items():
        if mod_prop['status']:
            module_parser = subparsers.add_parser(str(mod), help=str(mod_prop['help']), description=str(mod_prop['description']))
            try:
                if mod_prop['args_chk']:
                    module_import =  __import__("modules.{}.arguments".format(str(mod)), fromlist=['modules.{}'.format(str(mod))])
                    module_import.check_args(module_parser)
            except ImportError as err:
                print ("Error: '{}'".format(str(err)))
                return False
            except Exception as err:
                print ("Error: {}".format(str(err)))
                return False

#*******************************************************#
# Override custom arguments with default configuration
#*******************************************************#
def override_args(arguments, configuration):
    
    # Log: Defaults to 'LOG_ROOT' from configuration if --log flag with path is not provided
    if not arguments.log:
        arguments.log = configuration['LOG_ROOT'] + "/logs/{}/{}/".format(str(arguments.command), str(handler.getTime(format="%d%m%Y_%H%M%S")))
    
    # App root: Defaults to 'APP_ROOT' from configuration
    arguments.__setattr__('app_root', configuration['APP_ROOT'])

    # Module root: Defaults to 'APP_ROOT' from configuration
    arguments.__setattr__('module_root', str( configuration['APP_ROOT']) + "/modules/" + str(arguments.command) + "/")

    # Debug: Defults  to 'DEBUG' from configuration if --debug flag is not provided
    if not arguments.debug:
        arguments.debug = configuration['DEBUG']
    return arguments

if __name__ == '__main__':
    pass