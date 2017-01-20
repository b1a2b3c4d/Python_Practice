#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
N = random.randint(1, 101)
a = 1000
list1 = []

for i in range(0,N):
    list1.append(random.randint(0,a))

print list1

list2 = random.sample(list1, 3)
list2.sort()

print list2