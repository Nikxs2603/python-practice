# #You create a thread with threading.Thread(). It takes two important arguments:
# # target: a callable object (function) for this thread to be invoked when the thread starts
# # args: the (function) arguments for the target function. This must be a tuple
# # Start a thread with thread.start()
# # Call thread.join() to tell the program that it should wait for this thread to complete before it continues with the rest of the code.
# #dummy program:
import queue
from threading import Thread ,Lock
import time

# def sq_func():
#     for i in range(100):
#         result = i*i
# if __name__ == "__main__":
#     threads = []
#     num_of_threads = 10
#     #create threads and assign a function for each of them
#     for i in range(num_of_threads):
#         thread = Thread(target=sq_func)
#         threads.append(thread)
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#         thread.join()


# #Task: Create two threads, each thread should access the current database value, modify it (in this case only increase it by 1), and write the new value back into the database value. Each thread should do this operation 10 times.
# from threading import Lock, Thread 
# import time
# # all threads can access this global variable
# database_value = 0
# def thread_modify(lock):
#     global database_value
#     # lock the state
#     with lock:
#     # get a local copy (simulate data retrieving)
#         local_copy = database_value
#     # simulate some modifying operation
#         local_copy += 1
#         time.sleep(0.1)
#     # write the calculated new value into the global variable
#         database_value = local_copy
    

# if __name__ == "__main__":
#     # create a lock
#     lock = Lock()
#     print("start value: ", database_value)
#     # pass the lock to the target function
#     thread1 = Thread(target = thread_modify, args = (lock,))
#     thread2 = Thread(target = thread_modify, args = (lock,))
#     thread1.start()
#     thread2.start()
    
#     thread1.join()
#     thread2.join()
#     print("end value: ", database_value)

# #Queues can be used for thread-safe/process-safe data exchanges and data processing both in a multithreaded and a multiprocessing environment.
# # A queue is a linear data structure that follows the First In First Out (FIFO) principle.
from queue import Queue
# #create queue
# q = Queue()
# #to add elements
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# # now q looks like this:
# # back --> 3 2 1 --> front
# # get and remove first element
# first = q.get()
# print(first)
# q.task_done()

# The following example uses a queue to exchange numbers from 0...19. 
# Each thread invokes the worker method.
# Inside the infinite loop the thread is waiting until items are available due to the blocking q.get() call.
# When items are available, they are processed (i.e. just printed here), and then q.task_done() tells the queue that processing is complete.
# In the main thread, 10 daemon threads are created. This means that they automatically die when the main thread dies, and thus the worker method and infinite loop is no longer invoked. 
# Then the queue is filled with items and the worker method can continue with available items. At the end q.join() is necessary to block the main thread until all items have been gotten and proccessed.
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get() # blocks until the item is available
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} value is {value}")
# For each get(), a subsequent call to task_done() tells the queue
# that the processing on this item is complete.
# If all tasks are done, q.join() can unblock
        q.task_done() 

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target = worker, args = (q,lock))
        thread.daemon = True # dies when the main thread dies
        thread.start()
    # fill the queue with items
    for x in range(20):
        q.put(x)
    q.join() # Blocks until all items in the queue have been gotten and processed.
    print('main done')







