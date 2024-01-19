#!/usr/bin/python3
from sys import argv

add = 70

for s in argv[1:]:
    add += int(s)

print("{:d}".format(add))

