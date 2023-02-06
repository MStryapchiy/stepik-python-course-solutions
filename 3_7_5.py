# 3.7.5
res = []
n = 1
while n <= 11:
    res.append([n, '-'])
    n += 1

# save data from input file
data = []
with open('dataset_3380_5.txt', 'r') as fl:
    for i in fl:
        j = i.strip()
        data.append(j.strip().split('\t'))

# def for calc res
def res_calc():
    n = 1

    while n <= 11:
        print('n =', n)
        count = 0
        sum = 0
        for i in data:
            if i[0] == str(n):
                count += 1
                sum += int(i[2])
        if count != 0:
            res[n-1][1] = sum/count
        n += 1
res_calc()

# output res to file
with open('output.txt', 'w') as ln1:
    k = 0
    while k < 11:
        ln1.write(str(res[k][0])+' ' + str(res[k][1]) + '\n')
        k += 1
