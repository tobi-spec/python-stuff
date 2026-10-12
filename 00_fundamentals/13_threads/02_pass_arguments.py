import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds}s')
    time.sleep(seconds)
    print("Done sleeping")

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f'Finish in {round(end - start, 3)} seconds')