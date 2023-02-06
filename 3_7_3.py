# 3.7.3
d = int(input())
# creating dict with known words
chdict = {}
i = 0
while i < d:
    chdict[input().lower()] = 'Correct'
    i += 1

# creating arrey with checking data
l = int(input())
arr = []
j = 0
while j<l:
    arr.append(input().lower().split(' '))
    j+=1

# def for check data
def check():
    res = []
    n = 0
    while n<len(arr):
        for i in arr[n]:
            if i not in chdict:
                if i not in res and i !='':
                    res.append(i)
        n+=1
    for i in res:
        print(i)
check()

