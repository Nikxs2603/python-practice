# from multiprocessing import Process
# import os

# def sqr_func():
#     for i in range(10):
#         print(i*i)
# if __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count()  # number of CPUs on the machine. Usually a good choise for the number of processes
#     # create processes and asign a function for each process
#     for i in range(num_processes):
#         process = Process(target = sqr_func)
#         processes.append(process)
#     # start all processes
#     for process in processes:
#         process.start()
#      # wait for all processes to finish
#     # block the main programm until these processes are finished
#     for process in processes:
#         process.join()

# # Since processes don't live in the same memory space, they do not have access to the same (public) data. Thus, they need special shared memory objects to share data.
# # Data can be stored in a shared memory variable using Value or Array.
# # Value(type, value): Create a ctypes object of type type. Access the value with .target.
# # Array(type, value): Create a ctypes array with elements of type type. Access the values with [].

# # Task: Create two processes, each process should have access to a shared variable and modify it (in this case only increase it repeatedly by 1 for 100 times). Create another two processes that share an array and modify (increase) all the elements in the array.
# # from multiprocessing import Process, Value, Array, Lock
# # import time

# def add_100(shared_number, lock):
#     with lock:
#         for i in range(100):
#             shared_number.value += 1

# def add100_array(shared_array,lock):
#     for _ in range(100):
#         with lock:
#             for i in range(len(shared_array)):
#                 shared_array[i]+=1

# if __name__ == "__main__":
#     lock = Lock()
#     shared_number = Value('i', 0)
#     shared_array = Array('i', [100, 200, 250])
#     print('Value at beginning is ', shared_number.value)
#     print('Value at the begiining is ', shared_array[:])
#     process1 = Process(target = add_100, args = (shared_number,lock) )
#     process2 = Process(target = add_100, args = (shared_number,lock ))

#     process3 = Process(target= add100_array, args = (shared_array, lock))
#     process4 = Process(target = add100_array, args =(shared_array, lock))

#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()

#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()
#     print("Value at the end is ", shared_number.value)
#     print("Value at the end is ", shared_array[:])



#A process pool object controls a pool of worker processes to which jobs can be submitted It supports asynchronous results with timeouts and callbacks and has a parallel map implementation. It can automatically manage the available processors and split data into smaller chunks which can then be processed in parallel by different processes.
from multiprocessing import Pool

def cube(number):
    return number*number*number

if __name__ == "__main__":
    pool = Pool()
    numbers = range(11)
    result= pool.map(cube, numbers)

    pool.close()
    pool.join()
    print(result)
    print(type(numbers))
