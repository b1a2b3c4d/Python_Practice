#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mtf ():
    # makeTextFile.py -- create text file
    import os
    ls = os.linesep

     # get filename
    while True:
        fname = raw_input(u'输入文件名')
        if os.path.exists(fname):
            print "ERROR: '%s' already exists" % fname
        else:
            break

     # get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"

    # loop until user terminates input
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

     # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print 'DONE!'

def rtf():
    # get filename
    fname = raw_input('Enter filename: ')
    print

    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
    else:
    # display contents to the screen
        for eachLine in fobj:
            print eachLine.strip()
            # s.strip(rm)        删除s字符串中开头、结尾处，
            # 位于 rm删除序列的字符，当rm为空时，
            # 默认删除空白符（包括'\n', '\r',  '\t',  ' ')
        fobj.close()

a = raw_input(u'创建文件或读取文件，创建输入m，读取输入r：')

if a=='m':
    mtf()
elif a=='r':
    rtf()
else:
    print u'请输入m或r。'
