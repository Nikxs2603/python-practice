# def countdown(num):
#     print('starting')
#     while num>0:
#         yield num
#         num -= 1
# cd = countdown(4)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))


# #to print a sequence of numbers starting from 0 to the given number
# def print_numbers(num):
#     num_list = []
#     n = 0
#     while n < num:
#         num_list.append(n)
#         n+=1
#     return num_list
# #the same thing using a generator
# def print_numbers_gen(num):
#     n = 0
#     while n<num:
#         yield n
#         n+=1

# my_num = print_numbers(10)
# my_num_gen = print_numbers_gen(10)
# # print(my_num)
# print(sum(my_num))
# print(sum(my_num_gen))

#to run fibonacci series
def fibonacci(num):
    a,b = 0,1
    while a < num:
        yield a 
        a,b = b, b+a
fib = fibonacci(7)
for i in fib:
    print (i)


