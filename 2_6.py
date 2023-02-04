# 2.6
# a = []
# ch = 1
# s = 0
# while ch != 0:
#     b = int(input())
#     ch = 0
#     a.append(b)
#     for i in a:
#         ch = ch+int(i)
# for n in a:
#     s = s+(n**2)
# print(s)

# a = int(input())
# res = []
# j = 1
# i = 1
# c = 0
# while i <= a:
#     j = 1
#     while j <= i:
#         res.append(i)
#         j += 1
#     i += 1
# while c < a:
#     print(res[c],' ', end='')
#     c += 1

a = [int(i) for i in input().split()]
b = int(input())
res = []
num = 0
for j in a:
    if b == j:
        res.append(num)
    num += 1
if len(res) > 0:
    for k in res:
        print(k, ' ', end='')
else:
    print('Отсутствует')
