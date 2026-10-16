import time
import asyncio



async def fetch_data(param: int) -> str:
    print(f'fetch data for {param}...')
    await asyncio.sleep(param)
    print(f'finished with {param}')
    return f'Result of {param}'

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Fetched 1 completely")
    result2 = await task2
    print("Fetched 2 completely")
    return [result1, result2]

t1 = time.perf_counter()
result = asyncio.run(main())
print(result)
t2 = time.perf_counter()
print(f"finished in {t2 - t1} seconds")

