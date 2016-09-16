#!/usr/bin/python3

import os
import sys

if len(sys.argv) != 2:
    print('One parameter required: filename extension')
    sys.exit(1)

input_ext = sys.argv[1]

for file in os.listdir():
    if file.endswith(input_ext):
        print(file)
