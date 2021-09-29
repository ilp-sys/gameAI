#2021-09-13
# -*- coding: utf-8 -*- 

def Hanoi(n, A, C, B): #개수-시작-목적지-버퍼
    if n==1:
        print(A,C)
    else:
        Hanoi(n-1, A, B, C)
        print(A,C)
        Hanoi(n-1, B, C, A)

n = int(input())
print(2**n-1)
Hanoi(n, 1, 3, 2)


