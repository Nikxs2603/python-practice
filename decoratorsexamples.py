# def decorator_function(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
# @decorator_function
# def print_something():
#     print('alex')
# # print_something = decorator_function(print_something)
# print_something()

# # to allow arguments in the wrapper
import functools
# def add5_Decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
# @add5_Decorator
# def add5(x):
#     return x+5
# result = add5(10)
# print(result)

# #two decorators 
# def repeat(num_times): #this decorator func will take a number as an input
#     def repeat_dec(func): #actual decorator which takes the function as the input
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return repeat_dec
# @repeat(5)
# def print_name(name):
#     print(f"Hello {name}")

# print_name('nikki')

#class decorator
class CountCalls:
    def __init__(self,func):
        functools.update_wrapper(self,func)
        self.func = func
        self.num_times = 0
    def __call__(self,*args,**kwargs):
        self.num_times += 1
        print(f"call {self.num_times} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
@CountCalls
def say_hello(any):
    print("hello")
say_hello(5)



