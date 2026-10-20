import time
import asyncio


async def fetch_data(param: int) -> str:
    await asyncio.sleep(param)
    return f'Result of {param}'

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    print("Task 1 and 2 awaited results:", result1, result2)

    # gather coroutines
    coroutine = {fetch_data(i) for i in range(1, 3)}
    results = await asyncio.gather(*coroutine, return_exceptions=True)
    print(f"Coroutine Results: {results}")

    # gather tasks
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Task Results: {results}")

    # Task Group
    async with asyncio.TaskGroup() as tg:
        results = [tg.create_task(fetch_data(i)) for i in range(1, 3)]
        # All tasks are awaited when the context manager exits.
    print(f"Task Group Results: {[result.result() for result in results]}")

    return "Main Coroutine Done"



t1 = time.perf_counter()
result = asyncio.run(main())
print(result)
t2 = time.perf_counter()
print(f"finished in {t2 - t1} seconds")

