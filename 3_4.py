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
# strf.sort()
# with open('output.txt', 'w') as res:
#     res.write(strf[0])

data = []
with open('dataset_3363_4.txt', 'r') as fl1:
    for i in fl1:
        j = i.strip()
        data.append(j.strip().split(';'))
print(data)

#add average values to array
res = []
for i in data:
    res.append((int(i[1])+int(i[2])+int(i[3]))/3)

#calculate averege values
math = 0
phys = 0
russ = 0
for i in data:
    math = math + int(i[1])
    phys = phys + int(i[2])
    russ = russ + int(i[3])
math = math/(len(data))    
phys = phys/(len(data))
russ = russ/(len(data))

with open('output.txt', 'w') as fl2:
    for i in res:
        fl2.write(str(i) + '\n')
    fl2.write(str(math) + ' ' + str(phys) + ' ' + str(russ))
