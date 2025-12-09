from pprint import pprint


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f'Time (ms): {(perf_counter() - start_time) * 1000}')
        return result
    return wrapper


@measure_time
def solution(lines: list[str]):
    tiles = [tuple(map(int, line.split(','))) for line in lines]
    
    max_area = float('-inf')
    n = len(tiles)

    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            if area > max_area:
                max_area = area
    
    print(max_area)


lines = read_input_file(file_path="input.txt")
solution(lines)