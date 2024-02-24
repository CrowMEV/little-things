from typing import Any, Iterator, Sequence

import httpx

HOST = "https://swapi.dev/api"


class MyRange:
    def __init__(self, start: int, end: int, interval: int) -> None:
        self.start = start
        self.end = end
        self.interval = interval
        self.cursor: int | None = None

    def __iter__(self):
        self.cursor = self.start - self.interval
        return self

    def __next__(self) -> int:

        self.cursor = self.cursor + self.interval
        if self.cursor > self.end:
            raise StopIteration
        return self.cursor


class StarWarsIterator:
    HOST_ = "https://swapi.dev/api"

    def __init__(self, sw_obj: str) -> None:
        self.sw_obj = sw_obj
        self.cursor: int | None = None

    def __iter__(self):
        self.cursor = 0
        return self

    def get_object(self) -> dict[str, Any]:
        return httpx.get(f"{self.HOST_}/{self.sw_obj}/{self.cursor}").json()

    def __next__(self) -> dict[str, Any]:
        self.cursor += 1
        sw_obj = self.get_object()
        if sw_obj.get("message") == "not found":
            raise StopIteration
        return sw_obj


def chunked(seq: Sequence[Any], chunk_size: int) -> Iterator[Sequence[Any]]:
    for i in range(0, len(seq), chunk_size):
        yield seq[i : i + chunk_size]


def sw_api_gen(sw_obj: str) -> Iterator:
    next_page = f"{HOST}/{sw_obj}"
    while next_page:
        main_obj = httpx.get(next_page).json()
        for sw_obj in main_obj["results"]:
            yield sw_obj
        next_page = main_obj["next"]
