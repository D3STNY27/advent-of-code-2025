from pprint import pprint


DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1)
]


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
    R, C = len(lines), len(lines[0])
    
    adj_map = {}
    for r in range(R):
        for c in range(C):
            if lines[r][c]=='.':
                continue

            if (r, c) not in adj_map:
                adj_map[(r, c)] = set()

            for dr, dc in DIRECTIONS:
                rn, cn = (r + dr), (c + dc)

                if rn < 0 or rn >= R or cn < 0 or cn >= C:
                    continue

                if lines[rn][cn]=='.':
                    continue

                if (rn, cn) not in adj_map:
                    adj_map[(rn, cn)] = set()
                
                adj_map[(rn, cn)].add((r, c))

    # Initial Rolls To Remove
    rolls_to_remove = set()
    for key, value in adj_map.items():
        if len(value) >= 4:
            continue

        rolls_to_remove.add(key)

    # Remove Rolls (while there are rolls to remove)
    removed_rolls = 0
    while rolls_to_remove:
        r, c = rolls_to_remove.pop()
        removed_rolls += 1

        for ar, ac in adj_map[(r, c)]:
            if (r, c) in adj_map[(ar, ac)]:

                # Update Adjacent Mappings & Queue Rolls which are ready to remove
                adj_map[(ar, ac)].remove((r, c))
                if len(adj_map[(ar, ac)]) < 4:
                    rolls_to_remove.add((ar, ac))
    
    print(removed_rolls)


lines = read_input_file(file_path="input.txt")
solution(lines)