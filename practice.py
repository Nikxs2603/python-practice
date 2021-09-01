# #sqrroot of a number
# import math
# def sqr_root(num):
#     print(math.sqrt(num))
# mynum = sqr_root(4)
# #sqr toot of a complex number
# import cmath
# num = eval(input("Enter a complex number: "))
# result = cmath.sqrt(num)
# print(result)


# #area of a triangle
# baseof = 4
# height = 10
# area = 0.5*baseof*height
# print(area)


# #to solve a quadratic equation
# a = 3
# b = 4
# c = 5
# solution = (-b +((b**2)-4*a*c)**0.5)/2*a
# print(solution)


# #to swap two variables
# x =10
# y =5
# x,y = y,x
# print("x is : ", x)
# print("y is : ", y)


# #to check for a leap year
# year = 2004
# if (year % 4) == 0:
#     if (year % 100 == 0): #if year is divisible by 4, we check if its a century year. if its divisible by 100, then we need to check if its divisible by 400 also, only then a century year can be a leap year. if it's not divisble by 100 but divisible by 4, it is a leap year
#         if(year % 400 == 0):
#             print("{} is leap year".format(year))
#         else:
#             print("{} is not leap year".format(year))
#     else:
#         print("{} is leap year".format(year))
# else:
#     print("{} not a leap year".format(year))


# #to check for a prime number
# num = int(input("Enter a number: "))
# flag =  False
# if (num>1):
#     for i in range(2,num):
#         if (num%i==0):
#             flag = True
#             break
# if flag:
#     print("{} is not prime number". format(num))
# else:
#     print(num ,"is a prime number")


# #to find the factorial of a number
# num = 2
# factorial = 1
# if(num<0):
#     print("factorial doesn't exist for negative numbers")
# elif(num==0):
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial = factorial*i
#     print("the factorial for {} is {}".format(num,factorial))

#to print multiplication table
# num = 8
# for i in range(1,11):
#     print("{} x {} = {}".format(num,i,num*i))

# #factorial using recursion
# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return(n*factorial(n-1))
# number= 3
# if number<0:
#     print("enter a valid number")
# else:
#     print(factorial(number))

# to print fibonacci series
# numofterms = int(input("enter number of terms: "))
# a,b = 0,1
# count = 0
# if(numofterms<=0):
#     print("Enter valid number of terms")
# elif(numofterms==1):
#     print(a)
# else:
#     while count<numofterms:
#         print(a)
#         nth = a+b
#         a=b
#         b=nth
#         count+=1

# #fibonacci using recursion
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return(fibonacci(n-1)+fibonacci(n-2))
# nterms = 3
# if nterms<0:
#     print("enter a positive number")
# else:
#     for i in range(nterms):
#         print(fibonacci(i))

# #to check for amstrong number
# num = int(input("Enter a number"))
# order = len(str(num))
# sum = 0
# temp = num
# while temp>0:
#     digit=temp%10
#     sum+=digit**order
#     temp//=10
# if(num==sum):
#     print("amstrong number")
# else:
#     print("not an amstrong number")

# #to find the sum of n natural numbers
# num = int(input("Enter the number of natural numbers: "))
# sum=0
# if(num<0):
#     print("enter a positive number")
# else:
#     for i in range(1, num+1):
#         sum+=i
#     print(sum)
    # while(num>0):
    #     sum+=num
    #     num-=1
    # print(sum)

# #sum of n natural numbers using recursion
# def sumof(n):
#     if n<=1:
#         return n
#     else:
#         return(n+sumof(n-1))
# nterms = 5
# if nterms<0:
#     print("enter a positive number")
# else:
#     print(sumof(nterms))

# # Display the powers of 2 using anonymous function
# num = 10
# result = list(map(lambda x: 2**x, range(num+1)))
# for i in range (num+1):
#     print("2 raised to the power {} is {}".format(i,result[i]))

# #to find numbers divisible by another number
# my_list = [1,2,3,4,5,6,7,8]
# result = list(filter(lambda x: (x%2==0), my_list))
# print(result)

# # Python program to convert decimal into other number systems
# #A number with the prefix 0b is considered binary, 0o is considered octal and 0x as hexadecimal.
# dec = 10
# print(bin(dec))   #has builtin functions
# print(oct(dec))
# print(hex(dec))

# #Python Program to Find ASCII Value of Character
# #we use built in functions ord() and chr()
# letter = "a"
# asci= 65
# print(" the ascii value of {} is {}".format(letter, ord(letter)))
# print("the representation of the ascii value {} is {}".format(asci, chr(asci)))

# #to find HCF of a given two numbers
# num1, num2 = 6,12
# if num1<num2:
#     smaller = num1
# else:
#     smaller=num2
# for i in range(1,smaller+1):
#     if(num1%i==0) and (num2%i==0):
#         hcf = i
# print("HCF of the given two numbers is : ", hcf)

# #to find the LCM of given two numbers
# num1,num2 = 5,4
# if num1>num2:
#     greater = num1
# else:
#     greater = num2
# while(True):
#     if(greater%num1==0) and (greater%num2==0):
#         print("LCM is: ", greater)
#         break
#     greater+=1

# #to find factors of a number
# num = 4
# for i in range(1, num+1):
#     if(num%i==0):
#         print(i)

# #building a simple calc
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# def add(x,y):
#     sum = x+y
#     return sum
# def sub(x,y):
#     difference = x-y
#     return difference
# def multiply(x,y):
#     product = x*y
#     return product
# def divide(x,y):
#     quotient=x/y
#     return quotient

# print("Select operation: \n 1.add \n 2.subtract \n 3.multiply\n 4.divide")
# num = int(input("Enter choice[1/2/3/4]: "))
# if num in (1,2,3,4):
#     if(num==1):
#         print(num1," + ",num2, "is equal to " ,add(num1,num2))
#     elif(num==2):
#         print(num1," - ", num2," is equal to ", sub(num1,num2))
#     elif(num==3):
#         print(num1," * ",num2," is equal to ", multiply(num1,num2))
#     elif(num==4):
#         print(num1," / ",num2," is equal to ", divide(num1,num2))
# else:
#     print("Invalid input")

# from datetime import datetime, timedelta, timezone
# obj = datetime.now()
# print(obj)
# # datetime.datetime(2018, 10, 7, 12, 27, 25, 527961)
# obj += timedelta(days=7)
# print(obj)
# obj.astimezone(timezone.utc)
# print(obj)
# # datetime.datetime(2018, 10, 14, 10, 27, 25, 527961, tzinfo=datetime.timezone.utc)

#to shuffle a deck of cards
# In the program, we used the product() function in itertools module to create a deck of cards. This function performs the Cartesian product of the two sequences.

# The two sequences are numbers from 1 to 13 and the four suits. So, altogether we have 13 * 4 = 52 items in the deck with each card as a tuple. For example,
# deck[0] = (1, 'Spade')

# import random, itertools
# deck = list(itertools.product(range(1,14),["spade","heart","diamond","club"]))
# random.shuffle(deck)
# for i in range(5):
#     print(deck[i][0]," of ",deck[i][1])

# #to display the calender of a given date
# import calendar
# mm = 3
# yy = 2002
# print(calendar.month(yy,mm))

# #to add two matrices
# def matrix(m,n):
#     o = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             inp = int(input(f"Enter o[{i}][{j}]"))
#             row.append(inp)
#         o.append(row)
#     return o
# def sum(A,B):
#     result = []
#     for i in range(len(A)): #number of rows
#         row = []
#         for j in range(len(A[0])): #number of columns 
#             row.append(A[i][j]+B[i][j])
#         result.append(row)
#     return result

# m= int(input("Enter number of rows: "))
# n= int(input("Enter number of columns: "))
# print("Enter matrix A")
# A = matrix(m,n)
# print(A)
# print("Enter matrix B")
# B = matrix(m,n)
# print(B)
# s = sum(A,B)
# print("Sum is: ",s)

##other code
# m = int(input("enter number of rows: "))
# n = int(input("enter number of cols: "))
# def matrix(m,n):
#     o =[]
#     for i in range(m):
#         row=[]
#         for j in range(n):
#             values = int(input(f"Enter o[{i}][{j}]"))
#             row.append(values)
#         o.append(row)
#     return o

# def sum(A,B):
#     result = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             row.append(A[i][j]+B[i][j])
#         result.append(row)
#     return result

# print("enter matrix A: ")
# A = matrix(m,n)
# print(A)
# print("enter matrix B")
# B = matrix(m,n)
# print(B)
# s = sum(A,B)
# print(s)

# #to find transpose of a matrix
# def matrix(m,n):
#     o =[]
#     for i in range(m):
#         row = []
#         for j in range(n):
#             inp = int(input(f"Enter o[{i}][{j}]"))
#             row.append(inp)
#         o.append(row)
#     return o
# def transpose(A):
#     t = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             row.append(A[j][i])
#         t.append(row)
#     return t          
# m = int(input("Enter number of rows: "))
# n = int(input("Enter number of columns: "))
# print("Enter matrix A")
# A = matrix(m,n)
# trans = transpose(A)
# print(f"Transpose of {A} is {trans}")

#to multiply two matrices
# Program to multiply two matrices using list comprehension

# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]

# result = [[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]
 
# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(Y)):
#             result[i][j] += X[i][k]*Y[k][j]


# for r in result:
#    print(r)

# # Program to check if a string is palindrome or not
# mystr = "Dad"
# mystr1 = mystr.casefold()
# rev_mystr = reversed(mystr1)

# if(list(mystr1)==list(rev_mystr)):
#     print("is a palindrome")
# else:
#     print("not a palindrome")
        
# #Python Program to Remove Punctuations From a String
# import string
# mystr = "Hello, This is nikki!!"
# newstr =""
# for char in mystr:
#     if char not in string.punctuation:
#         newstr+=char
# print(newstr)

# #Python Program to Sort Words in Alphabetic Order
# mystr= "zey chis bs aikki"
# mystrlist = mystr.split()
# mystrlist.sort()
# print(mystrlist)

# #Python Program to Count the Number of Each Vowel
# vowels = "aeiou"
# mystr = "heey, this is nikki"
# count=0
# for char in mystr:
#     if char in vowels:
#         count+=1
# print(count)

# #merge two dicts
# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}
# dict_3 = dict_1.copy()
# dict_3.update(dict_2)
# print(dict_3)

# #Python Program to Access Index of a List Using for Loop
# my_list = [21, 44, 35, 11]
# for count, item in enumerate(my_list):
#     print(count,item)

# # Program to print half pyramid using *
# rows = int(input("Enter number of rows: "))
# for x in range(rows):
#     for y in range(x+1):
#         print("*", end="")
#     print("")

# #Program to print half pyramid a using numbers
# rows = int(input("Enter number of rows: "))
# for x in range(1,rows+1):
#     for y in range(1,x+1):
#         print(y,end="")
#     print("\n")

# #Program to print half pyramid using alphabets
# rows = int(input("Enter number of rows: "))
# ascii_val = 65
# for x in range(rows):
#     for y in range(x+1):
#         alphabet = chr(ascii_val)
#         print(alphabet,end="")
#     ascii_val+=1
#     print("\n")

# #Inverted half pyramid using *
# rows = int(input("Enter number of rows: "))
# for x in reversed(range(rows)): #or range(rows,0,-1)
#     for y in range(x):
#         print("*", end="")
#     print("\n")

# #Inverted half pyramid using numbers
# rows = int(input("Enter number of rows: "))
# for x in range(rows,0,-1):
#     for y in range(1,x+1):
#         print(y,end="")
#     print("\n")

# #Program to print full pyramid using *
# rows = int(input("Enter number of rows: "))
# for i in range(0,rows):
#     for space in range(0,rows-i):
#         print(end=" ")
#     for j in range(0,2*i+1):
#         print("*",end="")
#     print()

# #Python Program to Make a Flattened List from Nested List
# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# flat_list = [num for sublist in my_list for num in sublist]
# print(flat_list)
# #or
# from functools import reduce
# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# print(reduce(lambda x,y: x+y,my_list))
# #or
# from itertools import chain
# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# flat_list = chain(*my_list)
# print(list(flat_list))

# #Sort the dictionary based on values
# dt = {5:4, 1:6, 6:3}
# dt_sorted = {key:value for key,value in sorted(dt.items(),reverse=True)}
# print(dt_sorted)








