# -*- coding: utf-8 -*-
def trim(s):
    start=0
    for i in s:
        if i == ' ':
            start=start+1
        else:
            break
    j=-1
    while (-j)<=len(s):
        if s[j] == ' ':
            j=j-1
        else:
            break
    end=len(s)+j+1
    return s[start:end]
    
        
