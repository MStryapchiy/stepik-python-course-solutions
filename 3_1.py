# 3.1
x = float(input())
def f(x):
    if x <= -2:
        a = 1 - (x + 2)**2
    if -2 < x <= 2:
        a = -1*x/2
    if 2 < x: 
        a = (x - 2)**2 + 1
    return a

# l = [1, 7, 0, -2, 8, 6, 3, 5, 7, 8]
# def modify_list(l):
#     ch = 0
#     j =[]
#     while ch < len(l):
#         if l[ch] % 2 == 0:
#             l[ch]= l[ch]//2
#         else: 
#             del l[ch]
#             ch-=1
#         ch+=1

