from pprint import pprint
from functools import cache

def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        return [line.strip() for line in input_file]


def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"Time (ms): {(perf_counter() - start) * 1000}")
        return result
    return wrapper


@measure_time
def solution(lines: list[str]):
    R, C = len(lines), len(lines[0])

    splitters = {}
    beam = None

    for r in range(R):
        for c in range(C):
            if lines[r][c] == 'S':
                beam = c

            if lines[r][c] == '^':
                if r not in splitters:
                    splitters[r] = set()

                splitters[r].add(c)


    @cache
    def recurse(r: int, c: int) -> int:
        nonlocal R, C

        if r == R:
            return 1

        if (r not in splitters) or (c not in splitters[r]):
            return recurse(r+1, c)

        return recurse(r+1, c-1) + recurse(r+1, c+1)


    print(recurse(1, beam))


lines = read_input_file("input.txt")
solution(lines)