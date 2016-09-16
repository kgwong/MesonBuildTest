#!/usr/bin/python3

import glob
import sys

if len(sys.argv) != 2:
    print('One parameter required: filename extension')
    sys.exit(1)

input_ext = sys.argv[1]

for file in glob.glob('./**/*' + input_ext, recursive=True):
    print(file)
