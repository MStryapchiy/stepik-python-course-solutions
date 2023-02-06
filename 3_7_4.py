# 3.4.7
res = [0, 0]
n = int(input())

# read data
ch = 0
indata = []
while ch < n:
    indata.append(input().lower().split())
    ch += 1

# def for calc res
def calcres():
    n = 0
    while n < len(indata):
        for i in indata[n]:
            if i == 'север':
                res[1] += int(indata[n][1])
            elif i == 'юг':
                res[1] -= int(indata[n][1])
            elif i == 'восток':
                res[0] += int(indata[n][1])
            elif i == 'запад': 
                res[0] -= int(indata[n][1])
        n+=1
    return print(res[0], res[1])
calcres()
