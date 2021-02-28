import randgen.libraries as libraries
from lazy import lazy
import csv
import sys


def add_subparser(subparsers):
    parser = subparsers.add_parser('csv', help='comma separated values')
    parser.set_defaults(function=_run)
    parser.set_defaults(headers=True)
    parser.set_defaults(quoting=True)
    parser.add_argument('--headers', type=str, nargs='+', help="headers to be used")
    parser.add_argument('--no-headers', help="No headers", action='store_false', dest='headers')
    parser.add_argument('-c', '--ncolumns', type=int, help="column count (ignored if headers are specified)", default=5)
    parser.add_argument('-r', '--nrows', type=int, help="row count", default=100)
    parser.add_argument('--no-quoting', help="don't use characters that require quoting", action='store_false', dest='quoting')
    parser.add_argument('-q', '--quotechar', help="character used for quoting", default='"')
    parser.add_argument('-d', '--delimiter', help="character used as delimiter", default=',')


def _run(args, generator):
    Context(args, generator).run()


class Context:
    def __init__(self, args, generator):
        self.__generator = generator
        self.__args = args
        self.__writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def run(self):
        self.__write_headers()
        self.__write_rows()

    @lazy
    def __headers(self):
        if self.__args.headers:
            if isinstance(self.__args.headers, list):
                return self.__args.headers
            else:
                return [ self.__generate_string() for _ in range(self.__args.ncolumns) ]

    @lazy
    def __nheaders(self):
        return len(self.__headers)

    def __write_headers(self):
        self.__writer.writerow(self.__headers)

    def __write_rows(self):
        for _ in range(self.__args.nrows):
            self.__write_row()

    def __write_row(self):
        contents = [ self.__generate_string() for _ in range(self.__nheaders) ]
        self.__writer.writerow(contents)

    def __generate_string(self):
        alphabet = libraries.lowercase_alphabet()
        if self.__args.quoting:
            alphabet += f'{self.__args.delimiter}{self.__args.quotechar}'
        return self.__generator.string(min_length=5, max_length=15, alphabet=alphabet)

