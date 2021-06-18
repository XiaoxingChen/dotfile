#!/usr/bin/env python3
import base64
import sys
import os

def encSuffix():
    return 'enc'

def codec(input_filename, encode=True):
    splitext = os.path.splitext(input_filename)
    if encode:
        output_filename = splitext[0] + '_' + encSuffix() + splitext[1]
    else:
        output_filename = splitext[0][:-len(encSuffix())] + splitext[1]
    with open(input_filename, 'r') as f_in:
        if encode:
            out = base64.b32encode(bytes(f_in.read(), 'utf-8'))
        else:
            out = base64.b32decode(bytes(f_in.read(), 'utf-8'))
        with open(output_filename, 'w') as f_out:
            f_out.write(out.decode())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: differ_codec.py input.txt")
        quit()

    input_filename = sys.argv[1]
    encode = True if (os.path.splitext(input_filename)[0].split('_')[-1] != encSuffix()) else False
    if encode:
        print("Encode")
    else:
        print("Decode")
    codec(input_filename, encode)

    print("Done")