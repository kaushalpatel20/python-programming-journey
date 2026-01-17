# k=input('Enter your name  : ')
# for i in k:
#     print(i)

#-------------------------------
# for i in[1,2.4,'python','hii',9+8j]:
#     print(i)

# for i in (1,2.4,'python','hii',9+8j):
#      print(i)

# for i in {1,2.4,'python','hii',9+8j}:
#      print(i)

# for i in {'a':1,'b':2,'c':3}:
#      print(i)
#it access only key in dict

# a={'a':10,'b':20,'c':30}
# for i in a:
#     print(a[i])

# for i in a.items():
#     print(i)

#------------RANGE FUNCATION------------------
# a=list(range(-20,0,1))
# print(a)

#PRINT THE NUMBER BETWEEN 20 AND 10 USING RANGE FUNACTION
# a=list(range(20,9,-1))
# print(a)

#PRINT THE NUMBER BETWEEN-10 AND 20 USINGE RANGE FUNACTION
# a=list(range(-10,21,1))
# print(a)

#WAP TO PRINT THE NUMBERS FROM UPTO 20 USING RANGE FUNCTION
# a=list(range(21))
# print(a)

# a=list(range(55,12))
# print(a)
#WHEN WE GOING TO REVERSE YOU MUST BE GIVE JUMP (-1)

#WAP TO PRINT THE EVEN NUMBER UP TO N
# n=int(input('Enter the limit :'))
# for i in range(2,n+1,2):
#     print(i)

# n=int(input("enter the limit :"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

#------------FOR LOOP ------------------
#WAP TO REVERSE THE STRING USING FOR LOOP
# out=''
# n=input('Enter the string reverse :')
# for i in n:
#       out=i+out
# print(out)

#USING RANGE FUNCATION
# out=''
# n=input('Enter the string reverse :')
# for i in range(0,len(n)):
#       out=n[i]+out
# print(out)

#---------------------------------------------------
# WAP TO CHECK IF GIVEN NUMBER IS PRIME NUMBER OR NOT 
# n=int(input('Enter the limit :'))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count+=1
# if count==0:
#     print('it is prime number')
# else:
#     print('it is not prime number')

#----------------------------------------------------
#WAP TO CHECK IF A GIVE NUMBER IS PERFECT NUMBER OR NOT
# n=int(input('Enter the Number to check perfect:'))
# count=0
# for i in range(1,n):
#     if n%i==0:
#         count+=i
# if count==n:
#     print('perfect number')
# else:
#     print('not perfect number')

#----------------------------------------------------
#1.WAP TO PRINT THE CHARACTER PRESENT AT ODD INDEX FROM A STRING
# n = input("Enter a string: ")
# out=''
# for i in range(len(n)):
#     if i % 2 != 0:
#         out=n[i]+out
# print(out)

#2.INPUT ='HoLIdaY' TO OUTPUT='hOliDAy'
# n = input("Enter a string: ")
# result = ""

# for i in n:
#     if i.isupper():
#         result = result + i.lower()
#     else:
#         result = result + i.upper()

# print("Output:", result)

#or
# a="HoLIdaY"
# out=''
# for i in a:
#     if "A"<=i<='Z':
#         out=out+i.lower()
#     elif"a"<=i<='z':
#         out=out+i.upper()
# print(out)


#3.WAP TO EXTRACT ALL THE LOWERCASE CHARACTERS FROM STRING ONLY IF ASCII VALUE IS EVEN
# n = input("Enter a string: ")
# out = ""

# for i in n:
#     ascii_val = ord(i)

#     if 97 <= ascii_val <= 122 and ascii_val % 2 == 0:
#         out = out + i

# print("Extracted characters:", out)


#4.WRITE A PROGRAM TO REPLACE SPACE BY * IN THE STRING
# n = input("Enter a string: ")
# out = ""

# for i in n:
#     if i == ' ':
#         out = out + '*'
#     else:
#         out = out + i

# print(f'Output:{out}')


#write program to remove duplicates from list
# a=[12,34,12,78,90,80]
# out=[]

# for i in a:
#     if i not in out:
#         out.append(i)
# print(out)


#wap to chech if given list is homogenious list or hetrogenious list
# a=[1,3,4,5,7,8,10,15]
# a=[3,1.4,'python',True]

# check=type(a[0])
# counter=0

# for i in range (1,len(a)):
#     if check!=type(a[i]):
#         counter+=1
# if counter==0:
#     print('homogenious list')
# else:
#     print('hetrogenious list')


#WAP TO COUNT OF NUMBER OF TIMES A PARTICULAR CHARCATER IS REPATED IN THE STRING USING FOR LOOP
# a=input('enter any string :')
# char=input('enter character to find repeatations: ')
# counter=0

# for i in a:
#     if char==i:
#         counter+=1
# print(f'{char} is repeat {counter} times')


#WAP to create a list of cube of number between 1 to 30
# cube=[]

# for i in range(1,31):
#     cube.append(i**3)
# print(cube)


#WAP TO EXTRACT ALL THE INTEGERS FROM THE LIST WHICH ARE MULTIPLY OF 5 AND IS THREE DIGIT NUMBER FROM A LIST
# a=[12.34,'lemon',50,200,9+8j,550]
# out=[]

# for i in a:
#     if type(i)==int:
#         if 100<=i<=999 and i%5==0:
#             out.append(i)
# print(out)





