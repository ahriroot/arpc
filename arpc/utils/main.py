import os
import sys
from .arpc import compiles


def print_help():
    text = """Usage: arpc [options] [value]
Options:
    -h, --help     output usage information
    -v, --version  output the version number

    -i, --input    input dir
    -o, --output   output dir
"""
    print(text)


def print_version():
    print("arpc-python version 0.0.1")


def main():
    args = sys.argv
    len_args = len(args)

    if len_args == 1:
        print("No args")
    elif len_args == 2:
        if args[1] == "--help" or args[1] == "-h":
            print_help()
        elif args[1] == "--version" or args[1] == "-v":
            print_version()
        else:
            print("Fatal error: Invalid args\n")
    elif len_args == 5:
        input_ = ""
        output_ = ""
        if args[1] == "--input" or args[1] == "-i":
            input_ = args[2]
        if args[3] == "--output" or args[3] == "-o":
            output_ = args[4]
        if input_ == "" or output_ == "":
            print("Fatal error: Invalid args\n")
        else:
            compiles(input_, output_)
    else:
        print("Fatal error: Invalid args\n")
