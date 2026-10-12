import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds: int) -> str:
    print(f'sleeping {seconds}s')
    time.sleep(seconds)
    return f'Done sleeping {seconds}s'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # starts all threads together and waits for all threads to finish
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


end = time.perf_counter()
print(f'Finish in {round(end - start, 3)} seconds')