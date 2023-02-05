# 3.4
# with open('file.txt', 'r') as fl:
#     str = fl.readline()
# num = '0'
# a = '0'
# str=str+'W'
# out =''
# for i in str:
#     if not i.isdigit():
#         out = out + a*int(num)
#         num='0'
#         a = i
#     else:
#         num = num+i
# with open('output.txt', 'w') as output:
#     output.write(out)

# with open('dataset_3363_3.txt', 'r') as fl:
#     instr = []
#     for j in fl:
#         j = j.strip()
#         instr.append(j.lower().split(' '))
# print(instr)
# dct = {}
# a, b, c, d = 0, 0, 0, 0
# strf = []
# for i in instr:
#     for j in instr[b]:
#         dct[j] = 0
#     b += 1
# for i in instr:
#     for j in i:
#         if j in dct:
#             dct[j] += 1
# for key, value in dct.items():
#     if value > a:
#         a = value
# for key, value in dct.items():
#     if value == a:
#         strf.append(key + ' ' + str(value))
# print(strf)
# strf.sort()
# print(strf)
# with open('output.txt', 'w') as res:
#     res.write(strf[0])
