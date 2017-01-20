#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Score():
    score = raw_input('score:')
    score = int(score)

    if score >= 90:
        print 'A'
    elif  80 <= score < 90:
        print 'B'
    elif 70 <= score < 80:
        print 'C'
    elif 60 <= score < 70:
        print 'D'
    else:
        print 'F'

if __name__ == '__main__':
    Score()