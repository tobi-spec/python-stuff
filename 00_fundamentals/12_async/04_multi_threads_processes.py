import time
import asyncio
from concurrent.futures import ProcessPoolExecutor


def fetch_data(param: int) -> str:
    print(f'fetch data for {param}...', flush=True)
    time.sleep(param) # synchronous wait in asynchronous function
    print(f'finished with {param}', flush=True)
    return f'Result of {param}'

async def main():
    # since function is not async it must be handled by a thread or a process
    # running threads concurrently
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("Thread 1 completely")
    result2 = await task2
    print("Thread 2 completely")


    loop = asyncio.get_running_loop()

    # running processes concurrently
    with ProcessPoolExecutor() as executor:
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1
        print("Fetched 1 completely")
        result2 = await task2
        print("Fetched 2 completely")

    return [result1, result2]

if __name__ == '__main__':
    t1 = time.perf_counter()

    result = asyncio.run(main())
    print(result)

    t2 = time.perf_counter()
    print(f"finished in {t2 - t1} seconds")

