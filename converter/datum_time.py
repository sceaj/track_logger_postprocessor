'''
Created on Sep 2, 2019

@author: Jeffrey
'''

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from datetime import datetime
from datetime import timedelta
import os
import sys

from converter.data_state import DataState
from converter.parser import Parser


__all__ = []
__version__ = 0.1
__date__ = '2019-09-02'
__updated__ = '2019-02-02'

def scan(inpath, verbose):
    data = DataState()
    parser = Parser(data)
    line_count = 0
    datum_datetime = None
    accumulated_delta = 0.0
    delta_count = 0
    with open(inpath, "r") as ifile:
        for data_line in ifile:
            input_line = data_line.strip()
            if verbose > 0:
                print(input_line)
            if input_line.startswith('$AC') or input_line.startswith('$GPRMC'):
                parser.parse(input_line)
                print("Line {3} - Time: {0}    GPS Timestamp: {1} {2}".format(data.get_data_item('Time'), data.get_data_item('GPS_Date'), data.get_data_item('GPS_Time'), line_count))
                if data.is_dirty('GPS_Date') and data.is_dirty('GPS_Time'):
                    data_datetime = datetime.strptime("{0} {1}".format(data.get_data_item('GPS_Date'), data.get_data_item('GPS_Time')), '%Y-%m-%d %H:%M:%S.%f')
                    data_deltatime = timedelta(0, data.get_data_item('Time'))
                    calculated_datum_datetime = data_datetime - data_deltatime
                    if datum_datetime is None:
                        datum_datetime = calculated_datum_datetime
                    print("Calculated Datum: {0}".format(calculated_datum_datetime.isoformat()))
                    datum_delta = calculated_datum_datetime - datum_datetime
                    print("Calculated Delta: {0}".format(datum_delta.total_seconds()))
                    accumulated_delta = accumulated_delta + datum_delta.total_seconds()
                    delta_count = delta_count + 1
        average_delta = accumulated_delta / delta_count
        print("Average Delta: {0}".format(average_delta))
        datum_datetime = datum_datetime + timedelta(0, average_delta)
        print("Datum: {0}".format(datum_datetime.isoformat()))

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v{0}".format(__version__)
    program_build_date = str(__updated__)
    program_license = '''data_file_validation <data-file>

  Created by jeff.rosen@acm.org on %s.
  Copyright 2019 jeff.rosen@acm.org. All Rights Reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (str(__date__))

    # Setup argument parser
    parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version="%s %s [%s]".format(program_name, program_version, program_build_date))
    parser.add_argument("-v", "--verbose", dest="verbose", action="count", default=0, help="set verbosity level [default: %(default)s]")
    parser.add_argument(dest="inpath", help="paths to source file to be validated")

    # Process arguments
    args = parser.parse_args()

    input_path = args.inpath
    print(args.inpath)
    verbose = args.verbose

    if verbose > 0:
        print("Verbose mode on")

    print("Scanning {0}...".format(input_path))
    scan(input_path, verbose)
    return 0

if __name__ == '__main__':
    sys.exit(main())