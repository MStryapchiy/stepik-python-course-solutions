import requests

#3.6
# with open ('dataset_3378_2.txt', 'r') as fl:
#     url = fl.readline().strip()
# r = requests.get(url)
# instr = []
# res = r.text.splitlines()
# print(len(res))

a = ''
with open ('dataset_3378_3.txt', 'r') as fl:
    url= fl.readline().strip()
    print(url)
while a!= 'We':
    a=''
    r = requests.get(url)
    a = a + r.text[:2]
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + r.text.strip()
    res = r.text
print(res)