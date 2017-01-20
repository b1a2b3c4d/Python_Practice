#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''3–11.
字符串格式化 不再抑制 readTextFile.py 中 print 语句生成的 NEWLINE 字符，
修改你的代码， 在显示一行之前删除每行末尾的空白。 这样，
你就可以移除 print 语句末尾的逗号了。
提示： 使用字符串对象的 strip()方法'''

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