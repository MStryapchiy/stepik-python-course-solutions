# 2.3
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a <= b and c <= d and a, b, c, d <= 10):
#     for i in range(c, d+1):
#         if (i == c):
#             print('\t', end='')
#         print(i, "\t", end='')
#     print()
#     for n in range(a, b+1):
#         print(n, '\t', end='')
#         for j in range(c, d+1):
#             print(j*n, '\t', end='')
#         print()

a = int(input())
b = int(input())
sum=0
count=0
for i in range(a, b+1):
    if i%3==0:
        sum=sum+i
        count=count+1
print(sum/count)