# 2.4
# str = input()
# str = str.upper()
# n = 0
# cnt = len(str)
# for i in str:
#     if (i == 'C' or i == 'G'):
#         n = n+1
# print((n/cnt)*100)

strn = input()
res = ''
res1 = ''
a = 0
b = 1
strn = strn + '*******************************************'
while (a < len(strn)-1):
    res1 = 1
    res = res + strn[a]
    if strn[a]!='*':
         while (strn[a]==strn[a+1]):
             res1+=1
             a+=1
    else: break
    res = res + str(res1)
    a += 1
print(res[:len(res)-1])


