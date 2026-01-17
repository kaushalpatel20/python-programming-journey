#WAP TO PRINT PYHTON FOR 10 TIMES
# i=0
# while i<10:
#     print("Python")
#     i+=1

#--------------------------------
#WAP TO PRINT THE CHARCATERS PRESENT IN SIDE THE STRING
# n=input('enter the string :')
# i=0
# while i<len(n):
#     print(n[i])
#     i+=1

#--------------------------------
#WAP TO PRINT CHARACTERS PRESENT AT ODD INDEX USING WHILE LOOP
# n=input('enter the string :')
# i=0
# while i<len(n):
#     print(n[i])
#     i+=2

#--------------------------------
# WAP TO REVERSE THE STRING USING WHILE LOOP

# a = input('Enter a string:')

# i = 0
# out = ''
# while i < len(a):
#     out = a[i] + out
#     i+=1
# print(out)

# -------------------------------------------
# WAP TO CHECK IF A GIVEN STRING IS PALINDROME OR NOT USING WHILE LOOP

# a = input('Eneter a string: ')
# i=0
# out = ''

# while i<len(a):
#     out = a[i]+out
#     i+=1
# if a == out:
#     print('Palindrome')
# else:
#     print('Not palindrome')

# --------------------------------------
# WAP TO PRINT SUM OF N NATURAL NUMBERS
# n = int(input('Enter a number: '))
# i = 1
# out = 0
# while i <=n:
#     out = out+i
#     i = i+1
# print(out)

# -------------------------------------
# WAP TO REVERSE THE NUMBER USING WHILE LOOP

# a = int(input('Enter a numebr: '))
# out = 0
# while a > 0:
#     ld = a%10
#     out = out*10+ld
#     a = a//10
# print(out)

# ---------------------------------------
# WAP TO CHECK NUMBER IS PALINDROME OR NOT

# a = int(input('Enter a numebr: '))
# temp = a
# out = 0
# while a > 0:
#     ld = a%10
#     out = out*10+ld
#     a = a//10
# if temp == out:
#     print('palindrome')
# else:
#     print('not palindrome')

# --------------------------------------------
# WAP TO CHECK IF A GIVEN NUMBER IS PERFECT NUMBER OR NOT

# n = int(input('Enter a value: '))
# i = 1
# out = 0
# while i < n:
#     if n%i==0:
#         out = out + i
#     i = i +1
# if out == n:
#     print('Perfect')
# else:
#     print('Not Perfect')

#---------------------------------------------
#WAP TO FIND FACTORIAL

# n = int(input('Enter a value finde factorial: '))
# i=n
# f=1

# while i>0:
#     f=f*i
#     i-=1
# print(f'Factorial of {n} is {f}')

#---------------------------------------------

#upper=['P','T','H']
#lower=['y']
#special=['@','!']
#digit=['1','2']

# c='PyTH@1!2'

# upper=[]
# lower=[]
# special=[]
# digit=[]
# i=0
# while i<len(c):
#     if 'A'<=c[i]<='Z':
#         upper.append(c[i])
#     elif 'a'<=c[i]<='z':
#         lower.append(c[i])
#     elif '0'<=c[i]<='9':
#         digit.append(c[i])
#     else:
#         special.append(c[i])
#     i+=1

# print(upper)
# print(lower)
# print(special)
# print(digit)

#---------------------------------------------
# c=input('Enter a string : ')
# u=''
# l=''
# s=''
# d=''
# i=0
# while i<len(c):
#     if 'A'<=c[i]<='Z':
#         u=u+c[i]
#     elif 'a'<=c[i]<='z':
#         l=l+c[i]
#     elif '0'<=c[i]<='9':
#         d=d+c[i]
#     else:
#         s=s+c[i]
#     i=i+1

# result=l+u+d+s
# print(result)

#----------------------------------------------
#upper=3
#lower=2
#digit=2
# special=1


# a = input('Enter input: ')
# i = 0
# upper = 0
# lower = 0
# digit = 0
# special = 0

# while i < len(a):
#     if 'A'<=a[i]<='Z':
#         upper +=1
#     elif 'a'<=a[i]<='z':
#         lower += 1 
#     elif '0'<=a[i]<='9':
#         digit += 1
#     else:
#         special +=1
#     i+=1
# result = lower+upper+digit+special
# print(f'upper:{upper}') 
# print(f'lower:{lower}')
# print(f'digit:{digit}')
# print(f'special:{special}')

#----------------------------------------------
#WAP TO FIND SUM OF DIGITS OF A NUMBER
#125=1+2+5=8

# a = int(input('Enter digit: '))
# result = 0
# while a > 0:
#     ld = a%10
#     result = result+ld
#     a = a//10
# print(result)


