import random as rad

def throw():
    sticks=[0,0,0,0]
    for i in range(len(sticks)):
        sticks[i]=rad.randint(0,1)
    return sticks

# 점수 배정 함수
def yoot(sticks):
    cnt=0
    for i in sticks:
        cnt+=i
    if cnt==0:
        score=4
        name='윷'
    elif cnt==4:
        score=5
        name='모'
    elif cnt==1:
        score=3
        name='걸'
    elif cnt==2:
        score=2
        name='개'
    elif cnt==3:
        score=1
        name='도'
    return score,name

#현재스코어 ==> 결과 후 스코어 
# 결과가 나와야 윷이나 모 해결!
def hng(hng_score):
    hng=throw()
    hng_yoot=yoot(hng)
    hng_score=hng_score+hng_yoot[0]
    print(f'흥부 {hng}: {hng_yoot[1]} ({hng_yoot[0]}점)/(총 {hng_score}점)--->')
    return hng_score,hng_yoot[1]

def nol(nol_score):
    nol=throw()
    nol_yoot=yoot(nol)
    nol_score=nol_score+nol_yoot[0]
    print(f'\t\t\t\t\t\t<--- 놀부 {nol}: {nol_yoot[1]} ({nol_yoot[0]}점)/(총 {nol_score}점)')
    return nol_score,nol_yoot[1]

# 흥부최악
def hng_worst(hng_score):
    hng=[1,1,1,1]
    hng_yoot=yoot(hng)
    hng_score=hng_score+hng_yoot[0]
    print(f'흥부 {hng}: {hng_yoot[1]} ({hng_yoot[0]}점)/(총 {hng_score}점)--->')
    return hng_score,hng_yoot[1]

# 놀부최악
def nol_worst(nol_score):
    nol=[1,1,1,1]
    nol_yoot=yoot(nol)
    nol_score=nol_score+nol_yoot[0]
    print(f'\t\t\t\t\t\t<--- 놀부 {nol}: {nol_yoot[1]} ({nol_yoot[0]}점)/(총 {nol_score}점)')
    return nol_score,nol_yoot[1]

def main(hng,nol):
    hng_score=0
    nol_score=0
    win_score=20
    while True:
        hng_yoot='윷'
        nol_yoot='윷'
        while hng_yoot=='윷' or hng_yoot=='모':
            hng_throw=hng(hng_score)
            hng_score=hng_throw[0]
            hng_yoot=hng_throw[1]
            if hng_score>=20:
                print(f'흥부 승리 => 흥부: {hng_score}, 놀부: {nol_score}')
                break
        if hng_score>=20:
            break    
        while nol_yoot=='윷' or nol_yoot=='모':
            nol_throw=nol(nol_score)
            nol_score=nol_throw[0]
            nol_yoot=nol_throw[1]
            if nol_score>=20:
                print(f'놀부 승리 => 흥부: {hng_score}, 놀부: {nol_score}')
                break
        if nol_score>=20:
            break  

# 메인 게임
main(hng,nol)

## 최악의 경우-흥부승리
main(hng_worst,nol)

## 최악의 경우-놀부승리
main(hng,nol_worst)