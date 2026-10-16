import time



def fetch_data(param: int) -> str:
    print(f'fetch data for {param}...')
    time.sleep(param)
    print(f'finished with {param}')
    return f'Result of {param}'

def main():
    result1 = fetch_data(1)
    print("Fetched 1 completely")
    result2 = fetch_data(2)
    print("Fetched 2 completely")
    return [result1, result2]

t1 = time.perf_counter()
result = main()
print(result)
t2 = time.perf_counter()
print(f"finished in {t2 - t1} seconds")

