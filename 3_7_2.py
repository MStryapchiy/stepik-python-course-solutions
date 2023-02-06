# 3.7.2
a = input()
b = input()

# generate code dict
cdict = {}
n = 0
for i in a:
    cdict[i] = b[n]
    n += 1

# generate encode dict
encdict = {}
m = 0
for i in b:
    encdict[i] = a[m]
    m += 1

ln1 = input()
ln2 = input()

# change letters in 1th ln
def code():
    m = 0
    for i in ln1:
        print(cdict[i], end='')
        m += 1


# change letters in 2nd ln
def encode():
    m = 0
    for j in ln2:
        print(encdict[j], end='')
        m += 1

code()
print()
encode()
