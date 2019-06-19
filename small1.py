from itertools import combinations
str0,num1=map(int,input().split())
n0=len(str(str0))
L1=list(combinations(str(str0),n0-num1))
L1=(sorted(L1))
a1="".join(L1[0])
print(a1)
