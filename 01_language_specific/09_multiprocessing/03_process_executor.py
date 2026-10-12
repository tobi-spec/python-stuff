import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds: int):
    print(f'sleeping {seconds}s')
    time.sleep(seconds)
    print("Done sleeping")

if __name__ == '__main__':
    with multiprocessing.Pool(10) as pool:
        results = []
        for seconds in range(10):
            result = pool.apply_async(do_something, (2,))
            results.append(result)

        pool.close()
        pool.join()

    end = time.perf_counter()
    print(f'Finish in {round(end - start, 2)} seconds')