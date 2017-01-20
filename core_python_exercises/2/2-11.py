#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sumed(): # 求和函数
    a = []
    for i in range(5):
        b = raw_input('Enter NO.%i:' % (len(a)+1))
        try:
            c = int(b)
        except ValueError:
            print 'Please enter a number.'
        a.append(c)
    return sum(a)

def mean():  # 求均值函数
    a = []
    while len(a) < 5:
        b = raw_input('Enter NO.%i :' % (len(a)+1))
        try:
            c=int(b)
        except ValueError:
            print 'Please enter a number.'
        a.append(c)
    return float(sum(a)) / 5
while True:
    command = raw_input(u'''请输入命令：1/2/x；
                        1.取五个数的和,
                        2.取五个数的平均值,
                        x.退出''')
    if command == 'x':
        break
    elif command == '1':
        print 'sum', sumed()
    elif command == '2':
        print 'mean', mean()
    else:
        print 'Please Enter the right command'
