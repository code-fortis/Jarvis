# Import library
from string import Template

# Import inhouse module(s)
# Setup log

welcome_message =  Template('''
Hello $user,

Welcome to python framework v1.0. Looks like you have initiated an template module.
This module serves as basic example on how to integrate your very own python modules
to this massive framework.
''')

class run(object):
    def __init__(self, arguments, system):
        self.__args = arguments
        self.__system = system
        self.__debug = False if not self.__args.debug else self.__args.debug
        self.run()

    def run(self):
        if hasattr(self.__args, "message"):
            print(self.__args.message)
        else:
            print (welcome_message.substitute({'user': self.__system['username']}))
