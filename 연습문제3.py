s = '0269FAC9A0'
def hextobin(s):
    mapping = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
               '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101' ,'E':'1110','F':'1101'}
    return mapping[s]

eq= ""
for i in range(len(s)):
    eq += hextobin(s[i])
print(eq)

pl = 0
i=len(eq)-1
while eq[i] != 1:
    i -= 1
    if eq[i] == 1:
        pl = i
        break
print(pl)