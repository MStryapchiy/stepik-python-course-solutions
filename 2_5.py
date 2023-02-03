# 2.5
# a = [int(i) for i in input().split()]
# sum =0
# for i in a:
#     sum=sum+i
# print(sum)

# a = [int(i) for i in input().split()]
# res = []
# n = 0
# result = ''
# if len(a)==1:
#     print(a[0])
# else:
#     while (n <= (len(a)-1)):
#         j = a[n-1]
#         if (n == len(a)-1):
#             k = a[0]
#         else:
#             k = a[n+1]
#         b = j+k
#         res += [str(b)]
#         n += 1
#     for l in res:
#         print(l, ' ', end='')

a = [int(i) for i in input().split()]
res = []
tp = ''
a.sort()
for i in a:
    if tp!=i:
        tp=i
    elif ((i==tp) and (i not in res)):
        res += [i]
for j in res:
    print(j, ' ', end='')
