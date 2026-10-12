import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds: int):
    print(f'sleeping {seconds}s')
    time.sleep(seconds)
    print("Done sleeping")

if __name__ == '__main__':
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    end = time.perf_counter()
    print(f'Finish in {round(end - start, 2)} seconds')