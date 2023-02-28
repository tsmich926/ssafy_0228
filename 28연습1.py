a = 0x10 #16이 출력됨
print(a)

a = 0x10203040
print(a)

s = '0000000111100000011000000111100110000110000111100111100111111001100111

# arr = list(map(int,input()))
# N = len(arr)
# num = 0
# # print(N,arr)
# for i in range(N):
#     j = i % 7
#     num += arr[i] * (2**(6-j))
#     if j == 6: #7개 끊기
#         print(num, end= ' ')
#         num = 0
# print()


# arr = input()
# for x in arr:
#     num = int(x,16)
#     for j in range(3,-1,-1):
#         bit = 1 if num&(1<<j) else 0
#         print(bit, end ='')
#     print('', end = '')

# def bintodec():
#
#
# for idx in range(0,len(s),7):
#     bintodec(s[idx:idx+7])

# s= 'F'
# def hextodec(s):
#     if s.isdigit():
#         return int(s)
#     else:
#         return ord(s) -ord(A) + 10

s= 'F'
print(int(s,16)) #기본적으로는 10진수로 바꿔주고 있었음

a = 0.0625
for i in range(100):
    a =a+(i*0.1)
    print(a)

def bbit_print(i):
    out=""
    for j in range(7,-1,-1):
        out += "1" if i & (i<<j) else "0"
    print(out)

for i in range(-5,6):
    print("%3d = "%i, end='')
    bbit_print(i)
