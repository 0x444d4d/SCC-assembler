#!/usr/bin/env python3

import sys
import tempfile

from SCCUtils import *


def main(argv):
    #Create virtual file

    in_file_name = ""
    out_file_name = ""

    for i in range(len(argv)):
        if argv[i] == "-i":
            in_file_name = argv[i + 1]
            i = i + 1
        elif argv[i] == "-o":
            out_file_name = argv[i + 1]
            i = i + 1

    virtual_file = tempfile.SpooledTemporaryFile(mode = "w+", encoding = "utf-8", dir = "/tmp/")

    #Open input file
    input_file = open( in_file_name, 'r' )
    #Strip file
    strip_input(virtual_file, input_file)
    #resolve jump directions
    operateFile(virtual_file, resolveDirections)
    #translate asm into machine code
    instructions = operateFile(virtual_file, translate)
    input_file.close()
    #write codd to file
    writeList2File(out_file_name, instructions)

    



if __name__ == "__main__":
    main(sys.argv)
