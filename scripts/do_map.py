# -*- coding=utf-8 -*-
from functools import reduce
def normalize(name):
    norname=name[0].upper()+name[1:].lower()
    return norname

def mul(x,y):
    return x*y

def prod(L):
    return reduce(mul,L)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(a,b):
    return a*10+b

def char2num(a):
    return DIGITS[a]


def str2float(s):
    dot=s.find('.')
    return reduce(str2int,list(map(char2num,s[:dot])))+reduce(str2int,list(map(char2num,s[dot+1:])))/10**(len(s)-dot-1)
 
