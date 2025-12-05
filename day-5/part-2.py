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


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        _, last_merged_end = merged[-1]

        if current_start <= last_merged_end:
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            merged.append([current_start, current_end])

    return merged


@measure_time
def solution(lines: list[str]):
    idx_break = lines.index('')
    ingredient_ranges = [list(map(int, line.split('-'))) for line in lines[:idx_break]]

    # Create Disjoint Ranges (Merge)
    merged_ingredient_ranges = merge_ranges(ingredient_ranges)  

    fresh_ingredients = 0
    for start, end in merged_ingredient_ranges:
        fresh_ingredients += (end - start + 1)
    
    print(fresh_ingredients)


lines = read_input_file(file_path="input.txt")
solution(lines)