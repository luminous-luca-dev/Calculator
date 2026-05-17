def half(a,b):
    s = (a|b)&(~(a&b))
    c = a&b
    return s,c

def all(a,b,x):
    s1,c1 = half(a,b)
    s2,c2 = half(s1,x)
    c = c1|c2
    s = s1
    print(s,c)
    return s,c

def bit8(a,b):
    a = list(a)
    b = list(b)
    print(a)
    print(b)
    s1,c1 = half(int(a[0]),int(b[0]))
    s2,c2 = all(int(a[1]),int(b[1]),c1)
    s3,c3 = all(int(a[2]),int(b[2]),c2)
    s4,c4 = all(int(a[3]),int(b[3]),c3)
    s5,c5 = all(int(a[4]),int(b[4]),c4)
    s6,c6 = all(int(a[5]),int(b[5]),c5)
    s7,c7 = all(int(a[6]),int(b[6]),c6)
    s8,e = all(int(a[7]),int(b[7]),c7)
    print(f"{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}")
    print(e)
    return 0

# print(all(int(input()),int(input()),0))
bit8(input(),input())