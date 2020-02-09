#!/usr/bin/python
import os
__version__ = 1.0

def check_args(parser):
    #*********************************************#
    # Optional arguments (override configuration)
    #*********************************************#

    # Argument options for 'Ingest'
    ingest_group =  parser.add_argument_group(title="Ingest", description="Import data in database [Mongo]")
    ingest_group.set_defaults(action="ingest")
    ingest_group.add_argument('--ingest', action='store_true')
    ingest_group.add_argument('--file', required=True, action='store', help='Input source file.')
    ingest_group.add_argument('--type', required=True, action='store', help='File type accepted as input source.')
    ingest_group.add_argument('--db', required=True, action='store', help='Database URL')
    ingest_group.add_argument('--coll', required=True, action='store', help='Database collection')


if __name__ == '__main__':
    pass
