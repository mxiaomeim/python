# -*- coding=utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return (None,None)
    else:
        min=L[0]
        max=L[0]
        for i in L:
            if min>i :
                min=i
            if max<i :
                max=i
        return (min,max)
