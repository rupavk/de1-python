import json
import sys

try:
    with open(sys.argv[1]) as data:
        for line in data:
            print(line)
except FileNotFoundError:
    print("File not found, please check your path")