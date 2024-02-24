import random
from typing import Any, Callable

import httpx

HOST = "https://swapi.dev/api"


def trace(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(*args, **kwargs):
        print(f"call function {func.__name__}")
        print(f"with args: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        print("-----------------------\n")
        return result

    return new_func


@trace
def get_random(a: int, b: int) -> int:
    return random.randint(a, b)


get_random(2, 6)


def cache(cache_size: int = 100) -> Callable[..., Any]:
    def _cache(func: Callable[..., Any]) -> Callable[..., Any]:
        cache_: dict[str, Any] = {}
        call_counter = 0

        def wrapper(*args, **kwargs) -> dict[str, Any]:
            nonlocal call_counter
            call_counter += 1
            print(f"function {func.__name__} calling {call_counter} times")
            key = f"{args}_{kwargs}"
            result = cache_.get(key)
            if result is not None:
                return result
            result = func(*args, **kwargs)
            if len(cache_) >= cache_size:
                cache_.popitem()
            cache_[key] = result
            return result

        return wrapper

    return _cache


@cache(2)
def get_sw_object(
    object_type: str, object_id: int | None = None
) -> dict[str, Any]:
    url = f"{HOST}/{object_type}"
    if object_type is not None:
        url = f"{url}/{object_id}"
    return httpx.get(url).json()


print(get_sw_object("planets", 1))
