# def bbit_print(i):
#     out=""
#     for j in range(7,-1,-1):
#         out += "1" if i & (i<<j) else "0"
#     print(out)
#
# for i in range(-5,6):
#     print("%3d = "%i, end='')
#     bbit_print(i)


#7개 자르는 방법1
# for i in range(0,len(s),7):
#     st=s[i:i+7]
# #배열에서 7개 바이트를 묶어서 10진수로 출력
s= '0000000111100000011000000111100110000110000111100111100111111001100111'
# #방법2
# for i in range(0,len(s),7):
#     st = " "
#     for j in range(7):
#         st += s[i+j]
#     print(st)

def bintohex2(st):
    resd = int(st[0])*64 + int(st[1])*32 + int(st[2])*16 + int(st[3])*8+int(st[4])*4+int(st[5])*2+int(st[6])
    return resd

for i in range(0,len(s),7):
    st=s[i:i+7]
    print(bintohex2(st))


