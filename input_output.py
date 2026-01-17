# a=10
# b=20
# print(a,b,end=' ',sep='$')
# print(b)

# addition of two value 
# a = int(input('enter value of a :'))
# b = int(input('enter value of b :'))

# print('total of a & b is :', a + b)
# print('minus of a & b is :', a - b)
# print('multiplication  of a & b is :', a * b)
# print('divison of a & b is :', a / b)

#eval input to accept any kind of value (with no restriction)
# a=eval(input('enter the name:'))
# print(a,type(a))

#formated string
# a=eval(input('enter the data :'))
# print(f'the type of data is {a}')
# # print('the type of data is',a)
# print(f'the type of data is {a} and datatype is {type(a)}')

#write progra to check number even or odd
# a = int(input('enter value for check even or odd :'))
# print(a%2==0)

#if condition
#  
# a = int(input('enter value for check even or odd :'))

# if a%2==0:
#     print("value is even")

# if a==0:
#     print("value is zero")
# elif a%2==0:
#     print("value is even")
# else:
#     print("value is odd")

# -------------------------------
#Q: WAP TO FIND GREATEST AMONG 3 NUMBER
# a = int(input('enter value of A:'))
# b = int(input('enter value of B:'))
# c = int(input('enter value of c:'))

# if a>b and a>c :
#     print(f'value of {a} is greatest')
# elif b>a and b>c :
#     print(f'value of {b} is greatest')
# else:
#     print(f'value of {c} is greatest')

# --------------------------------
#Q: WAP TO FIND LOWEST AMONG 4 NUMBER
# a = int(input('enter value of A:'))
# b = int(input('enter value of B:'))
# c = int(input('enter value of c:'))
# d = int(input('enter value of d:'))
# if a<b and a<c and a<d:
#     print(f'value of {a} is lowest')
# elif b<a and b<c and b<d :
#     print(f'value of {b} is lowest')
# elif c<a and c<b and c<d:
#     print(f'value of {c} is lowest')
# else:
#     print(f'value of {d} is lowest')

# --------------------------------
#WAP TO CHECK TO GIVEN NUMBER IS POSTIVE,NEGATIVE OR ZERO
# a = int(input('enter value for check even or odd :'))

# if a==0:
#     print("value is zero")
# elif a%2==0:
#     print("value is even")
# else:
#     print("value is odd")

# --------------------------------
# Q:ACCEPT A NUMBER IF NUMBER IS DIVISIBLE BY 3
# AND 5 PRINT "FIZZbUZZ". IF DIVISIBLE BY 3 ->
# "FIZZ".IF DIVISIBLE BY 5->"BUZZ"

# n = int(input('enter value of N:'))

# if n%3==0 and n%5==0:
#     print("FizzBuzz")
# elif n%3==0:
#     print("Fizz")
# elif n%5==0:
#     print("Buzz")
# else:
#     print("this is not divided by 5 and 3")

# ---------------NESTED IF-----------------
#Q:WAP TO CHECK IF A GIVEN CHARCTER IS VOWEL OR NOT 

# n = input('enter any character:')

# if 'A'<=n<='z' or 'a'<=n<='z':
#     if n in 'AEIOUaeiou':
#         print('input is vowel')
#     else:
#         print('not a vowel')
# else:
#     print('charcter should be upper or lowercase')

# --------------------------------------
#Q:WAP TO LOGIN INTO INSTAGRAM BY INTERING CORRET USER NAME AND PASSWORD 
# user='kaushal@17'
# passw='Kp@17'

# user_nm= input('enter your user name: ')
# password= input('enter password :')

# if user_nm==user:
#     if password==passw:
#         print('LOGIN DONE..')
#     else:
#         print('PASSWORD IS CORRECT')
# else:
#     print('USERNAME IS INCORRECT')

# ----------------------------------------
#Q:WAP TO FIND GREATEST AMONG 3 NUMBERS USING NESTED IF
# n=int(input('enter value of N:'))
# m=int(input('enter value of M:'))
# o=int(input('enter value of o:'))

# if n>m:
#     if n>o:
#         print(f'{n} is greatest')
#     else:
#         print(f'{o} is greatest')
# else:
#     if m>o:
#         print(f'{m} is greatest')
#     else:
#         print(f'{o} is greatest')

# ----------------------------------------
#Q:WAP TO FIND GREATEST AMONG 4 NUMBERS USING NESTED IF
# a=int(input('enter value of A:'))
# b=int(input('enter value of B:'))
# c=int(input('enter value of c:'))
# d=int(input('enter value of d:'))

# if a>b:
#     if a>c:
#         if a>d:
#             print(f'{a} is greatest')
#         else :
#             print(f'{d} is greatest')
#     else :
#         if c>=d:
#             print(f'{c} is greatest')
#         else:
#             print(f'{d} is greatest')
    
# else :
#     if b>c:
#         if b>d:
#             print(f'{b}is greatest')
#         else:
#             print(f'{d}is greatest')
#     else:
#         if c>d:
#             print(f'{c}is greatest')
#         else:
#             print(f'{d} is greatest')

#WAP TO PRINT THE MIDDLE CHARCTER OF GIVEN STRING ONLY IF IT IS UPPERCASE CHARCTER
# n=input("enter the string :")
# if len(n)%2!=0:
#     character=len(n)//2
#     if 'A'<=n[character]<='Z':
#         print('MIDDLE CHARACTER IS UPPERCASE')
#     else:
#         print('MIDDLE CHARACTER IS LOWERCASE')
# else:
#     print('length of string should be odd only')



#WAP TO PRINT REVERSE STRING ONLY IF THE STRING IS STARTING WITH VOWEL AND ENDING WITH CONSONET ALONG WITH THAT
#IT IS HAVING MIDDLE VALUE
vowels = 'aeiouAEIOU'

n=input("enter the string :")
if len(n)%2!=0:
    if n[0] in vowels and n[-1] not in vowels:
        print(f'Revsred string is {n[::-1]}')
    else:
        print('string does not either start with vovel or end with consonant')
else:
    print('Middle value does not exist')





    






