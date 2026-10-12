import time
import threading

start = time.perf_counter()

def do_something():
    print("sleeping 1s")
    time.sleep(1)
    print("Done sleeping")

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.perf_counter()
print(f'Finish in {round(end - start, 3)} seconds')