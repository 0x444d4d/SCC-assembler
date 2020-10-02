#!/usr/bin/env python3

import sys
import tempfile

from SCCUtils import *


def main(argv):
    #Create virtual file
    virtual_file = tempfile.SpooledTemporaryFile(mode = "w+", encoding = "utf-8", dir = "/tmp/")

    #Open input file
    input_file = open( "test_strip.csv", 'r' )

    #Strip file
    strip_input(virtual_file, input_file)

    operateFile(virtual_file, resolveDirections)
    instructions = operateFile(virtual_file, translate)
    input_file.close()


    with open('a.out', 'w') as file:
        for instruction in instructions:
            file.write(f'{instruction}\n')

    



if __name__ == "__main__":
    main(sys.argv)
