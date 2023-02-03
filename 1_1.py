# #a = int(input())
# #print(a//60)
# #print(a%60)

# x = int(input())
# h = int(input())
# m = int(input())
# print((h*60 + m + x)//60)
# print((m + x)%60)


# x = 5
# y = 10
# print((y > (x * x)) or ((y >= (2 * x)) and (x < y)))

# a = True
# b = False
# print(a and b or not a and not b)

# a = int(input())
# b = int(input())
# h = int(input())
# if (a<=b and h>0 and a>0 and b>0):
#     if h<a:
#         print('Недосып')
#     elif (a<=h<=b or a==h==b):
#         print('Это нормально')
#     elif (h>b):
#         print('Пересып')
# else:
#     print('Вы не справились!')

# n = int(input())
# if (1900<=n<=3000):
#     if ((n%4 == 0 and n%100!=0) or n % 400 ==0):
#         print('Високосный')
#     else:
#         print('Обычный')


# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c)/2
# print((p*(p-a)*(p-b)*(p-c))**0.5)

# a = int(input())
# if ((-15<a<=12) or (14<a<17) or 19<=a):
#     print('True')
# else:
#     print('False')

# a = float(input())
# b = float(input())
# op = input()

# if (op == "+"):
#     print(a+b)
# elif (op == "-"):
#     print(a-b)
# elif (op == "*"):
#     print(a*b)
# elif (op == "/"):
#     if (b != 0):
#         print (a/b)
#     else: print('Деление на 0!')
# elif (op == "mod"):
#     if (b !=0):
#         print(a%b)
#     else: print('Деление на 0!')
# elif (op == "div"):
#     if (b !=0):
#         print(a//b)
#     else: print('Деление на 0!')
# elif (op == "pow"):
#     print(a**b)

# tp = input()
# if (tp == 'прямоугольник'):
#     a = float(input())
#     b = float(input())
#     print(a*b)
# elif (tp == 'треугольник'):
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = (a + b + c)/2
#     print((p*(p-a)*(p-b)*(p-c))**0.5)
# elif (tp == 'круг'):
#     r = float(input())
#     print(3.14*r**2)

# a = int(input())
# b = int(input())
# c = int(input())
# max = a
# min = b
# last = c
# if (a > b and a > c or a == b and a > c or a == c and a > b):
#     max = a
# elif (a < b and b > c or b == a and b > c or b == c and b > a):
#     max = b
# elif (a < c and b < c or a == b or c == b and c > a or c == a and c > b):
#     max = c

# if (a < b and a < c or a == b and a < c or a == c and a < b):
#     min = a
# elif (c < b and c < a or b == a and b < c or b == c and b < a):
#     min = c
# elif (b < a and b < c or c == a and c < b or c == b and c < a):
#     min = b

# sum = abs(a) + abs(b) + abs(c)
# last = sum - (abs(min) + abs(max))
# if (last!=a and last!=b and last!=c):
#     last = last*(-1)

# print(max)
# print(min)  )
# print(last)

# n = int(input())
# if n>=0:
#     if (n==0 or n%10 == 0 or n==11 or n==12 or n==13 or n%100==13 or n%100 ==12 or n%100 ==11 or n==14 or n%100==14 or n ==5 or n%10 ==5 or n==6 or n%10 ==6 or n==7 or n%10 ==7 or n==8 or n%10 ==8 or n==9 or n%10==9) :
#         print(n, 'программистов')
#     elif (n==1 or n%10 == 1 and n!=11):
#         print(n, 'программист')
#     elif (n==2 or n%10 ==0 or n!=12 or n==3 or n%10 ==3 and n!=13 and n%100 != 13 or n==4 or n%10==4 and n!=14 and n%100 != 14):
#         print(n, 'программиста')

n = int(input())
a = n//1000
b = n % 1000
a1, a3, a2 = a//100, a % 10, (a//10) % 10
b1, b3, b2 = b//100, b % 10, (b//10) % 10
sum1, sum2 = (a1+a2+a3), (b1+b2+b3)
if (sum1==sum2):
    print('Счастливый')
else:
    print('Обычный')