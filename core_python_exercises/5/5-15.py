#!/usr/bin/env python
# -*- coding: utf-8 -*-

def GCD():
    a = raw_input('a:')
    b = raw_input('b:')
    a = int(a)
    b = int(b)
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

if __name__ == '__main__':
    print GCD()