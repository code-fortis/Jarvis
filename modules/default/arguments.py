#!/usr/bin/python
import os
__version__ = 1.0

def check_args(parser):
    #*********************************************#
    # Optional arguments (override configuration)
    #*********************************************#
    parser.add_argument('--message', metavar='M', required=False, action='store', help='Override default print message.')


if __name__ == '__main__':
    pass
