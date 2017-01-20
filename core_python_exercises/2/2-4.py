#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = raw_input('enter a number:')
try:
    int(a)
except ValueError:
    print 'please enter a number.'
    a = raw_input('enter a number:')
print a