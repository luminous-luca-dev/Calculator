def half(a,b):
    s = (a|b)&(~(a&b))
    c = a&b
    return s,c

def all(a,b,x):
    s1,c1 = half(a,b)
    s2,c2 = half(s1,x)
    c = c1|c2
    s = s2
    return s,c

def bit8(a,b):
    a = list(a)
    b = list(b)
    s1,c1 = half(int(a[7]),int(b[7]))
    s2,c2 = all(int(a[6]),int(b[6]),c1)
    s3,c3 = all(int(a[5]),int(b[5]),c2)
    s4,c4 = all(int(a[4]),int(b[4]),c3)
    s5,c5 = all(int(a[3]),int(b[3]),c4)
    s6,c6 = all(int(a[2]),int(b[2]),c5)
    s7,c7 = all(int(a[1]),int(b[1]),c6)
    s8,e = all(int(a[0]),int(b[0]),c7)
    result = f"{s8}{s7}{s6}{s5}{s4}{s3}{s2}{s1}"
    if e == 1:
        print("オーバーフロー")
    elif e == 0:
        print("正常に計算されました")

    return result

# print(all(int(input()),int(input()),0))
x = format(int(input()), '08b')
y = format(int(input()), '08b')
print(x,y)
act = bit8(x,y)
print(act)
print(int(act,2))