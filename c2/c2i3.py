'''
ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function

ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1

ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1

ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c
'''
import math

print("*** New Range ***")
print("Enter Input : ", end="")
n = list(map(float, input().split(" ")))

l = []
if len(n) == 3:
    start = n[0]
    end = n[1]
    off = n[2]
    while (start < end):
        l.append(round(start, 3))
        start += n[2]
elif len(n) == 2:
    off = n[0] % 1
    l = list(map(float, range(math.floor(n[0]), math.ceil(n[1]), 1)))
    for e in range(len(l)): l[e] += off
else:
    l = list(map(float, range(0, math.ceil(n[0]), 1)))
r = str(l).replace("\'", "")
r = r.replace("[", "(").replace("]", ")")
print(r)