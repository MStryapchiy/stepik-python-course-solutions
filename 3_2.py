# 3.2
# d ={22:[23], 25:[32]}
# key = 12
# value = 32
# def update_dictionary(d, key, value):
#     a = key*2
#     if key in d:
#         d[key].append(value)
#     elif key not in d and a in d:
#         d[a].append(value)
#     elif 2*key not in d:
#         d[a]=[value]
# update_dictionary(d, key, value)
# print(d)

# a = [i.lower() for i in input().split(' ')]
# b = {}
# n = 0
# for i in a:
#     b[i] = 0
# for i in a:
#     if a[n] in b.keys():
#         b[i]+=1
#     n+=1
# for key, value in b.items():
#     print(key, value)


def f(x):
    a = x*2
    return a
a = int(input())
n = 0
ls = []
d = {}
while n < a:
    c = int(input())
    ls.append(c)
    n += 1
n = 0
for i in ls:
    d[i]= 0
for key in d:
    d[key] = f(key)
for i in ls:
    print(d[i])
