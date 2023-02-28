import sys
sys.stdin = open("input2.txt","r")

def findcode(value):
    codes = {211:0,221:1,122:2,411:3,132:4,231:5,114:6,312:7,213:8,112:9}
    return codes[value]


def hextobin():
    hexPATT = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
               '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101' ,'E':'1110','F':'1111'}

    for rows in ARR:
        s = ''
        for hexV in rows:
            s += hexPATT[hexV]
        binARR.append(s)

TC= int(input())
# TC = 1
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    ARR = [input() for _ in range(N)]

    # 16진수를 2진수로
    binARR = []
    hextobin()
    # print(binARR)


    for row in range(1,N):
        col = M*4-1
        while col>54:
        # for col in range(M*4-1,-1,-1):
            if binARR[row-1][col] == '0' and binARR[row][col]=='1':
                #마지막 위치를 찾음
                # print(tc,row,col)

                #유의미한 row와 col찾기
                # while col
                # 1의 갯수를 센다
                # 0의 갯수를 센다
                # 1의 갯수를 센다

                codes= [-1]*8
                for idx in range(8):
                    # print(tc,row,col)
                    cnt1 =0
                    while binARR[row][col] == '1':
                        col -= 1
                        cnt1 += 1

                    cnt2 =0
                    while binARR[row][col] == '0':
                        col -= 1
                        cnt2 += 1

                    cnt3 =0
                    while binARR[row][col] == '1':
                        col -= 1
                        cnt3 += 1

                    cnt4 =0
                    while binARR[row][col] == '0':
                        col -= 1
                        cnt4 += 1

                    ratio = min(cnt1,cnt2,cnt3)
                    code = findcode(cnt3//ratio*100+cnt2//ratio*10+cnt1//ratio)
                    # print(code)
                    codes[7-idx]= code
                print(tc,codes)
            else:
                col -= 1
    #09488243 순으로 거꾸로 하고
    #암호 판별한다음에 암호맞으면 다 더해서 값을 도출