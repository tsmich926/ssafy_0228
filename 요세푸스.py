N,K =map(int,input().split())
lst = []
for i in range(1,N+1):
    lst.append(i)
#처음 수 뺄때
del(lst[K-1])
lst[K-1] = -1
print(lst)
while len(lst)