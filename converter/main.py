#!/usr/local/bin/python2.7
# encoding: utf-8
'''
converter.main -- conversion utility for teensy_track_logger

converter.main is a tool for converting teensy_track_logger data files to a variety of standard data-logger
formats.

It defines classes_and_methods

@author:     sceaj

@copyright:  2019 sceaj. All rights reserved.

@license:    license

@contact:    
@deffield    updated: 2019-05-20
'''

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import os
import sys

from converter.data_state import DataState
from converter.parser import Parser
from converter.formatter import FormatterFactory
import datetime

__all__ = []
__version__ = 0.1
__date__ = '2019-05-20'
__updated__ = '2019-05-20'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def process(input_paths, output_path, format, tags):
    data = DataState()
    last_data_time = data.state_time
    parser = Parser(data)
    formatter = FormatterFactory.getFormatter(format, tags)
    with open(output_path, "w") as ofile:
        header_line = formatter.formatHeading(data)
        if header_line is not None:
            print(header_line)
            ofile.write(header_line)
            ofile.write("\n")
        for path in input_paths:
            print("Processing {0}".format(path))
            with open(path, "r") as ifile:
                for data_line in ifile:
                    input_line = data_line.strip()
                    print(input_line)
                    parser.parse(input_line)
                    output_line = formatter.formatData(data)
                    if output_line is not None:
                        print(output_line)
                        ofile.write(output_line)
                        ofile.write("\n")
                    if data.state_time > last_data_time:
                        last_data_time = data.state_time
                        output_line = formatter.formatTimeIncrement(data)
                        if output_line is not None:
                            print(output_line)
                            ofile.write(output_line)
                            ofile.write("\n")
        footer_line = formatter.formatFooter(data)
        if footer_line is not None:
            print(footer_line)
            ofile.write(footer_line)
            ofile.write("\n")

def buildTags(args):
    tags = dict()
    tags['vin'] = args.tag_vin
    tags['vehicle'] = args.tag_vehicle
    tags['mileage'] = args.tag_mileage
    return tags
    

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s".format(__version__)
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2019 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-f', '--format',      dest='output_format', help='Output format to generate. Currently CSV or INFLUXDB are supported.')
        parser.add_argument('-i', '--vin',         dest='tag_vin',     default='n/a', help='VIN number used to tag data. (output formats that support tagging)')
        parser.add_argument('-n', '--vehicle',     dest='tag_vehicle', default='n/a', help='Vehicle name used to tag data. (output formats that support tagging)')
        parser.add_argument('-m', '--mileage',     dest='tag_mileage', default='0',   help='Mileage used to tag data. (output formats that support tagging)')
        parser.add_argument('-o', '--output',      dest="output_path", help="Destination path of output file")
        parser.add_argument('-t', '--temperature', dest='tag_temp',    help='Ambient temperature used to tag the data. (output formats that support tagging)')
        parser.add_argument('-D', '--start_date',  dest='start_date',  default=None,  help='Date datum (in ISO format: YYYY-MM-DD). If supplied GPS_Date data in log data is ignored.')
        parser.add_argument('-T', '--start_time',  dest='start_time',  default=None,  help='Time datum (in ISO format: HH24:MM:SS.ffffff[Z]) used with Time field to generate Unix timestamps')
        parser.add_argument("-v", "--verbose",     dest="verbose",     action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument('-V', '--version',     action='version',   version=program_version_message)
        parser.add_argument(dest="input_paths",    help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", nargs='+')

        # Process arguments 
        args = parser.parse_args()

        input_paths = args.input_paths
        output_format = args.output_format
        output_path = args.output_path
        verbose = args.verbose
        
        if args.start_date is not None:
            start_date_datum = datetime.date.fromisoformat(args.start_date)
        else:
            start_date_datum = None
        if args.start_time is not None:
            start_time_datum = datetime.time.fromisoformat(args.start_time)
        else:
            start_time_datum = None
        tags = buildTags(args)

        print("Input Path(s): {0}".format(input_paths))
        print("Output Format: {0}".format(output_format))
        print("Output Path(s): {0}".format(output_path))
        print("Start Date Datum: {0}".format(start_date_datum))
        print("Start Time Datum: {0}".format(start_time_datum))
        print("Tags: {0}".format(tags))
        if verbose > 0:
            print("Verbose mode on")

        process(input_paths, output_path, output_format, tags)
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-v")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'converter.main_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())