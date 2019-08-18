'''
Created on Aug 3, 2019

@author: Jeffrey
'''
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import os
import sys

__all__ = []
__version__ = 0.1
__date__ = '2019-08-03'
__updated__ = '2019-08-03'

def validate(inpath):
    with open(inpath, "r") as ifile:
        line_num = 0
        for data_line in ifile:
            line_num += 1
            if not data_line.startswith('$'):
                print("Line {} does not start with the required '$'.".format(line_num))
            if data_line.rfind('$') > 0:
                print("Line {} contains an '$' in the middle of the data.".format(line_num))

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
    parser.add_argument('-V', '--version', action='version', version="%s %s".format(program_name, program_version))
    parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
    parser.add_argument(dest="inpath", help="paths to source file to be validated")

    # Process arguments
    args = parser.parse_args()

    input_path = args.inpath
    verbose = args.verbose

    if verbose > 0:
        print("Verbose mode on")

    print("Validating %s...".format(input_path))
    validate(input_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())