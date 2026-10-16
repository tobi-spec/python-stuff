import asyncio
import time


def sync_function(test_param: str) -> str:
    print("This function is synchron")
    time.sleep(0.1)
    return f'Sync Result {test_param}'

# Also known as coroutine
async def async_function(test_param: str) -> str:
    print("This function is synchron")
    await asyncio.sleep(0.1)
    return f'Async Result {test_param}'

async def main():
    sync_result = sync_function("Test")
    print(sync_result)

    print("------- future --------")
    loop = asyncio.get_running_loop()
    future = loop.create_future() # promise like object
    print(f'Empty future: {future}')
    future.set_result("Future Result: Test")
    future_result = await future
    print(future_result)

    print("------- coroutine -----")
    coroutine_obj = async_function("Test")
    print(coroutine_obj)
    coroutine_result = await coroutine_obj
    print(coroutine_result)

    # task wraps coroutine function
    print("-------- task -----")
    task = asyncio.create_task(async_function("Test"))
    print(task)
    task_result = await task
    print(task_result)

if __name__ == '__main__':
    asyncio.run(main())
