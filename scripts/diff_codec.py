#!/usr/bin/env python3
import base64
import sys
import os

def codec(input_filename, encode=True):
    splitext = os.path.splitext(input_filename)
    suffix = '_enc' if encode else '_dec'
    output_filename = splitext[0] + suffix + splitext[1]
    with open(input_filename, 'r') as f_in:
        if encode:
            out = base64.b32encode(bytes(f_in.read(), 'utf-8'))
        else:
            out = base64.b32decode(bytes(f_in.read(), 'utf-8'))
        with open(output_filename, 'w') as f_out:
            f_out.write(out.decode())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: differ_codec.py [enc|dec] input.txt")
        quit()

    mode, input_filename = sys.argv[1:]
    encode = True if mode == 'enc' else False
    codec(input_filename, encode)