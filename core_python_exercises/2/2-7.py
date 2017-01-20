#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = raw_input('Enter a string:')

print isinstance(a, basestring)
b = len(a)
c = len(a)
while b > 0:
    print a[c-b],
    b = b - 1
print
for i in a:
    print i,

