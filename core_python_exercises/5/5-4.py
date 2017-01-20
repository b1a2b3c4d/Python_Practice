#!/usr/bin/env python
# -*- coding: utf-8 -*-

def leap_year():

    a = raw_input('years:')
    a = int(a)
    if a % 100 == 0 and a % 400 == 0:
        return 'It is a leap_year.'
    elif a % 4 == 0 and a % 100 is not 0:
        return 'It is a leap_year.'
    else:
        return 'It is not a leap year.'

if __name__ == '__main__':
    print leap_year()