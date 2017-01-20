#!/usr/bin/env python
# -*- coding: utf-8 -*-


def knap_rec(weight, wlist, n):
    print "INITI:", weight, wlist[n - 1], str(n)
    if weight == 0:
        return True

    if weight < 0 or (weight > 0 and n < 1):
        return False

    if knap_rec(weight - wlist[n-1], wlist, n-1):
        print "Item" + str(n) + ":", wlist[n-1], weight
        return True

    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False

a = [2, 1, 3, 4]
weight = 9
n = 4
print knap_rec(weight, a, n)
