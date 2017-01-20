#!/usr/bin/env python
# -*- coding: utf-8 -*-

#5-6 算术。写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符：
#N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数，运算符可以是+, -, *, /, %, ** 分别表示
#加法，减法， 乘法， 整数除，取余和幂运算。计算这个表达式的结果，然后显示出来。提示：
#可以使用字符串方法 split(),但不可以使用内建函数 eval().
def operator(str) :
    if str.find('+') >= 0:
        return '+'
    elif str.find('-') >= 0:
        return '-'
    elif str.find('*') >= 0:
        return '*'
    elif str.find('/') >= 0:
        return '/'
    elif str.find('%') >= 0:
        return '%'
    else :
        return '**'
calStr = raw_input('输入计算表达式,如a+b形式：')
op = operator(calStr)
num = calStr.split(op)
print num
res = 0.0
if op == '+':
    res = float(num[0]) + float(num[1])
elif op == '-':
    res = float(num[0]) - float(num[1])
elif op == '*':
    res = float(num[0]) * float(num[1])
elif op == '/':
    res = float(num[0]) / float(num[1])
elif op == '%':
    res = int(num[0]) % int(num[1])
elif op == '**':
    res = float(num[0]) ** float(num[1])
print 'result is %f' % str(res)