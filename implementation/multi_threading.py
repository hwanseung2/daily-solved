import time
import threading

def loop():
    for i in range(50000000):
        pass

# Single Thread
start = time.time()
loop()
loop()
end = time.time()
print('[Single Thread] total time : {}'.format(end - start))

# Multi Thread
start = time.time()
thread1 = threading.Thread(target=loop)
thread2 = threading.Thread(target=loop)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print('[Multi Thread] total time : {}'.format(end - start))

# import time
# import threading

# def sleep_for_2s():
#     time.sleep(2)

# # Single Thread
# start = time.time()
# sleep_for_2s()
# sleep_for_2s()
# end = time.time()
# print('[Single Thread] total time : {}'.format(end - start))

# # Multi Thread
# start = time.time()
# thread1 = threading.Thread(target=sleep_for_2s)
# thread2 = threading.Thread(target=sleep_for_2s)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# end = time.time()
# print('[Multi Thread] total time : {}'.format(end - start))

