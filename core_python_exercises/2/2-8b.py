#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = []
for i in range(5):

    b = raw_input('Enter NO.%i:' % (len(a)+1))
    try:
        int(b)
    except ValueError:
        print 'Please enter a number.'
    else:
        c = int(b)
    a.append(c)

print a
print sum(a)
