#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python

'readTextFile.py -- read and display text file'

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