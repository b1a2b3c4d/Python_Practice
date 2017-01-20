#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_cents():
    a = raw_input('cents:')
    a = int(a)
    a1 = a // 50
    b = a % 50
    b1 = b // 25
    c = b % 25
    c1 = c //10
    d = c % 10
    d1 = d // 5
    e = d % 5
    f = e / 1
    return a1, b1, c1, d1, f

if __name__ == '__main__':
    a = count_cents()
    print  '50: %s, 25: %s, 10: %s, 5: %s, 1: %s' \
           % a

u'''def changes(money):
    list = [50，25,10,5,1]
    count = 0
    for i in list:
        result = divmod(money,i)
        count += result[0]
        money = result[1]
    正常的算法。
'''