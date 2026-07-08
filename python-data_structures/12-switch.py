#!/usr/bin/python3
a = 10
b = 89
sed -i '4s/.*/a, b = b, a/' 12-switch.py
print("a={} - b={}".format(a, b))
