#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LNode:
    '''表结点'''
    def __init__(self, elem, next_=None):
        self.elem = elem  # 表元素域
        self.next_ = next_  # 下一结点 链接域

'''llist1 = LNode(1)
    p = llist1  # p指向llist1
    print '1', p
    for i in range(2, 4):
        p.next_ = LNode(i)
        print p.next_
        # 将p.next_一个实例，也就是指向下一个表结点
        p = p.next_
        print p
        # 将p实例化，变为下一个表结点
    print '2', p.next_  # None
    print '3', p     # 指向新的值了
    p = llist1   # p重新指向llist1
    print '4', p
    while p is not None:
        print p.elem
        p = p.next_
'''

class LinkedListUnderFlow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        '''给表头插入元素'''
        self._head = LNode(elem, self._head)

    def pop(self):
        '''删除并返回表头元素'''
        if self._head is None:  # 若_head域里无结点则引发异常
            raise LinkedListUnderFlow('in pop')
        e = self._head.elem
        self._head = self._head.next_
        return e

    def append(self, elem):
        '''表后端插入元素'''
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next_ is not None:
            p = p.next_
        p.next_ = LNode(elem)

    def pop_last(self):
        '''删除并返回表尾元素'''
        if self._head is None:
            raise LinkedListUnderFlow( "in pop_last")
        p = self._head
        if p.next_ is None:
            e = p.elem
            self._head = None
            return e
        while p.next_.next_ is not None:
            p = p.next_
        e = p.next_.elem
        p.next_ = None
        return e

    def find(self, pred):
        ''' 查找到第一个元素'''
        p = self._head
        while p is not None:
            if pred(p.elem):
                # print 'Had found'
                return p.elem
            p = p.next_

    def printall(self):
        p = self._head
        while p is not None:
            print p.elem,
            if p.next_ is not None:
                print ',',
            p = p.next_
        print ''

    def filter(self, pred):
        '''查找所有元素'''
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next_

    def rev(self):
        '''反转'''
        p = None
        while self._head is not None:
            q = self._head  # q = 1, sh = 1
            print 'sh', self._head
            print 'q', q
            self._head = q.next_  # sh=2
            print 'sh', self._head
            print 'q', q
            q.next_ = p   # qn = none, 2 的链接域为none
            print 'sh', self._head
            p = q         # p=
            print 'q', q
            print
        self._head = p

mlist1 = LList()
for i in range(4):
    mlist1.append(i)
'''for i in range(3, 8):
    mlist1.append(i)
mlist1.printall()
def find3(a):
    if a == 3:
        return True
print mlist1.find(find3)
print mlist1.filter(find3)
for x in mlist1.filter(find3):
    print x,'''
mlist1.printall()
mlist1.rev()
mlist1.printall()


class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        '''首插'''
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        '''尾插'''
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next_ = LNode(elem)
            self._rear = self._rear.next_

    def pop_last(self):
        '''尾弹返'''
        if self.head is None:
            raise LinkedListUnderFlow
        p = self._head
        if p.next_ is None:
            e = p.elem
            self._head = None
            return e
        while p.next_.next_ is not None:
            p = p.next_
        e = p.elem
        p.next_ = None
        self._rear = p
        return e