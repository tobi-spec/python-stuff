import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds: int) -> str:
    print(f'sleeping {seconds}s')
    time.sleep(seconds)
    return f'Done sleeping {seconds}s'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, secs) for secs in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

end = time.perf_counter()
print(f'Finish in {round(end - start, 3)} seconds')