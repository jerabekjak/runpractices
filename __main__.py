#!/usr/bin/python3
import parser
from practices import Practices


if __name__ == '__main__':
    sens = Practices(parser.read_parser())
    sens.run()
