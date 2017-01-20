#!/usr/bin/env python
# -*- coding: utf-8 -*-

u'''3–10. 异常。使用类似 readTextFile.py 中异常处理的方法取代 readTextFile.py
makeTextFile.py 中 对 os.path.exists() 的 调 用 。 反 过 来 ，
用 os.path.exists() 取 代
readTextFile.py 中的异常处理方法。
答：第一个没解决。
'''

import os
ls = os.linesep

# get filename
fname = raw_input(u'输入文件名')

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
try:
    fobj = open(fname, 'w')
except IOError:
    print "ERROR: '%s' already exists" % fname
else:
    fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'

