s= '01D06079861D79F99F'
#4자리의 이진수로 나타낸다음 7자리씩 슬라이싱
# 00000001110100001010

#2진수를 10진수로 바꿔주는 함수
# def bintohex2(st):
#     resd = int(st[0])*8 + int(st[1])*4 + int(st[2])*2 + int(st[3])
#     return resd

# 10진수를 2진수로 바꾸기
# def dectobin(value):
#     for j in range(3,-1,-1):
#         r = value & (1<<j)
#         if r != 0:
#             print(1)
#         else:
#             print(0)

#2진수의 형태로 있는 문자열을 10진수로 표현

def bintohex2(st):
    resd = int(st[0])*64 + int(st[1])*32 + int(st[2])*16 + int(st[3])*8 +int(st[4])*4 +int(st[5])*2 +int(st[6])
    return resd


#16진수를 2진수로 바꿔줌
def hextobin(s):
    mapping = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
               '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101' ,'E':'1110','F':'1101'}
    return mapping[s]

eq= ""
for i in range(len(s)):
    eq += hextobin(s[i])
print(eq)

#7자리씩 슬라이싱
for i in range(0,len(eq),7):
    st=eq[i:i+7]
    print(st)
    # for i in range(12):
    #     a= bintohex2(st)
