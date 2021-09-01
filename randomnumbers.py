# import random

# # .random() prints random float between 0 to 1
# a = random.random()
# print(a)
# # .uniform() gives a random float in the range specified
# a = random.uniform(1,30)
# print(a)
# # .randrage is used to print an integer in the given range
# a = random.randrange(1,10)
# print(a)
# #to pick an element from a sequence
# my_list = list("ABCDEFGHIJKLMNOPQRSTUV")
# a= random.choice(my_list)
# print(a)
# #to pick multiple elements
# a = random.sample(my_list,3)
# print(a)
# # to shuffle the order of the list
# random.shuffle(my_list)
# print(my_list)

# #With random.seed(), you can make results reproducible, and the chain of calls after random.seed() will produce the same trail of data. The sequence of random numbers becomes deterministic, or completely determined by the seed value.
# random.seed(1)
# print(random.random())
# print(random.randrange(1,10))
# random.seed(3)
# print(random.random())
# print(random.randrange(1,10))
# random.seed(1)
# print(random.random())
# print(random.randrange(1,10))
# random.seed(3)
# print(random.random())
# print(random.randrange(1,10))

# #true random numbers, for security purposes
# import secrets
# #prints a random integer below the given number
# a = secrets.randbelow(10)
# print(a)
# #returns an integer with k random bits
# a = secrets.randbits(4)
# print(a)
# #to choose a random element from a sequence
# a = secrets.choice(list("ABCDEFGH"))
# print(a)

#numpy module
import numpy as np
#prints a random array 
a = np.random.rand(3)
print(a)
a= np.random.rand(3,3)
print(a)
#to print an array with random integers
a =np.random.randint(0,10,5) #prints 5 integers between 0 to 9
print(a)
a= np.random.randint(0,10,(3,4))
print(a)
# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)
#seed method
np.random.seed(1)
a = np.random.rand(2)
print(a)
np.random.seed(1)
a = np.random.rand(2)
print(a)


