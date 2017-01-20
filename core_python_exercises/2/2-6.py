#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = raw_input('Enter a number:')

try:
    int(a)
except ValueError:
    print 'Please enter a number.'
    a = raw_input('Enter a number:')

a = int(a)

print isinstance(a, int)

if a > 0:
    print 'This is a positive number.'
elif a < 0:
    print 'This is a negative number.'
else:
    print 'Zero.'