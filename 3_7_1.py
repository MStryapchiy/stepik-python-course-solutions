# 3.7.1
#add input data to array
# a = 0
# data = []
# n = int(input())
# while a < n:
#     data.append(input().split(';'))
#     a += 1

# #create dict
# res = {}
# b = 0
# for j in data:
#     res[j[0]] = [0, 0, 0, 0, 0]
#     res[j[2]] = [0, 0, 0, 0, 0]

# #def for calculate results and generate table
# def greate_table():
#     for key in res:
#         for j in data:
#             if key in j:
#                 res[key][0] += 1
#     for j in data:
#         if j[1] == j[3]:
#             res[j[0]][2] += 1
#             res[j[2]][2] += 1
#             res[j[0]][4] += 1
#             res[j[2]][4] += 1
#         elif int(j[1]) < int(j[3]):
#             res[j[2]][1] += 1
#             res[j[0]][3] += 1
#             res[j[2]][4] += 3
#         elif int(j[1]) > int(j[3]):
#             res[j[2]][3] += 1
#             res[j[0]][1] += 1
#             res[j[0]][4] += 3
#     for key in res.keys():
#         print(key+ ':', ' ', end='')
#         for i in res[key]:
#             print(i, ' ', end='')
#         print()

# greate_table()
