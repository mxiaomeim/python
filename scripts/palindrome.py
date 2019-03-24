# -*- coding=utf-8 -*-
def is_palindrome(n):
    string=list(str(n))
    mid=len(string)/2
    i=0
    j=-1
    flag=0
    while i<=mid :
        if string[i]!=string[j-i]:
            flag=1
        i=i+1
    if flag==0:
        return n

            
        
