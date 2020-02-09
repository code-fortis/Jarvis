import os, sys

config = dict()

# Supported module(s)
# <module>: {'status': True, 'help': '<help message>', 'description': '<module description>'}
config['modules'] = {
    'default': {'status': True, 'help': 'Prints Hello World', 'description': 'Prints Hello World', 'args_chk': False},
    'albus': {'status': True, 'help': 'Mongo Db/Data operations', 'description': 'Mongo Db/Data operations', 'args_chk': True}
}

# Mail Configuration
# <prod_type> : {'server': '<server name>', 'from': '<from_email_address>'}
config['mail'] = {
    'production': {
        'server': 'localhost',
        'from': 'devOps_admin@domain.com'
    },
    'test': {
        'server': 'localhost',
        'from': 'devOps_admin@domain.com',
        'to': 'akshayag@domain.com'
    }
}

# Supported OS(s) and Distribution(s)
config['os'] = {
    'supported': {'linux': True, 'windows': True},
    'distribution': {
        'linux': ['3.10.0-693.el7.x86_64'],
        'windows': ['8']
    }
}

# Enviornment Variables to be set
config['env'] = None
config['DEBUG'] = False

# Set Framework defaults, some of these defaults can be override via command line options.
config['APP_ROOT'] = os.path.abspath(os.path.dirname(sys.argv[0]))
config['LOG_ROOT'] = os.path.abspath(os.path.dirname(sys.argv[0]))
