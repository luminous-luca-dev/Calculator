def half(a,b):
    s = (a|b)&(~(a&b))
    c = a&b
    return s,c

def all(a,b,x):
    s1,c1 = half(a,b)
    s2,c2 = half(s1,x)
    c = c1|c2
    s = s1
    return s,c

def bit8():
    
    return

print(all(int(input()),int(input()),0))