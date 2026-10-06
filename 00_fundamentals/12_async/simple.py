import asyncio
from random import randint
from time import perf_counter

import requests

MAX_POKEMON = 150

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])

def http_get_sync(url: str):
    response = requests.get(url)
    return response.json()

async def get_random_pokemon_name_async() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await asyncio.to_thread(http_get_sync, pokemon_url)
    return str(pokemon["name"])


async def main() -> None:
    time_before = perf_counter()
    for i in range(10):
        pokemon_name = get_random_pokemon_name_sync()
        print(pokemon_name)
    print(f"Total time (synchronous): {perf_counter() - time_before}")

    time_before = perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name_async() for _ in range(10)])
    print(result)
    print(f"Total time (asynchronous): {perf_counter() - time_before}")

if __name__ == "__main__":
    asyncio.run(main())

