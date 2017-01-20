#!/usr/bin/env python
# -*- coding: utf-8 -*-


while True:
    a = raw_input('Enter a number between 1-100:')
    try:
        int(a)
    except ValueError:
        print 'Please enter a number.'
    else:
        c = int(a)
    print c > 0
    print c < 100
    if (c > 0) and (c < 101):
        print 'right'
        break
    else:
        print 'wrong'