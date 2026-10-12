import time
import threading

start = time.perf_counter()

def do_something():
    print("sleeping 1s")
    time.sleep(1)
    print("Done sleeping")

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# outer wise script will run concurrently to the threads
t1.join()
t2.join()

end = time.perf_counter()
print(f'Finish in {round(end - start, 2)} seconds')