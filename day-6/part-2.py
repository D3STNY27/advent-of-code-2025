from pprint import pprint
from functools import reduce


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip('\n') for line in lines]


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
    *digit_lines, operators_line = lines
    operators = operators_line.split()

    grid = [list(row) for row in digit_lines]
    R, C = len(grid), len(grid[0])

    # Find columns with no digits and replace with '0'
    for c in range(C):
        if any(grid[r][c].isdigit() for r in range(R)):
            for r in range(R):
                if grid[r][c]==' ':
                    grid[r][c]='0'

    rows = [''.join(r).split() for r in grid]

    columns = list(zip(*rows))
    total_sum = 0

    for col_values, operator in zip(columns, operators):
        # Create numbers again but replace '0' with "" (empty character)
        numbers = [
            int("".join(row[i] for row in col_values).replace('0', ''))
            for i in range(len(col_values[0]))
        ]

        result = sum(numbers) if operator=="+" else reduce(lambda x, y: x*y, numbers, 1)
        total_sum += result
    
    print(total_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)