#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = raw_input('Enter A')
b = raw_input('Enter B')
c = raw_input('Enter C')
a = int(a)
b = int(b)
c = int(c)

if a>b:
    a, b = b, a

if b>c:
    b, c = c, b
    if a>b:
        a, b = b, a

print  a, b, c