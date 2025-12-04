from sortedcontainers import SortedList
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
    
    # Populate Sorted Container
    sorted_adj_list = SortedList()
    for key, value in adj_map.items():
        sorted_adj_list.add((len(value), key))

    # Remove Rolls
    removed_rolls = 0
    while sorted_adj_list:
        num_adjacent_cells, (r, c) = sorted_adj_list.pop(0)
        if num_adjacent_cells >= 4:
            break

        removed_rolls += 1
        for ar, ac in adj_map[(r, c)]:
            if (r, c) in adj_map[(ar, ac)]:
                # Update Container
                sorted_adj_list.remove((len(adj_map[(ar, ac)]), (ar, ac)))
                adj_map[(ar, ac)].remove((r, c))
                sorted_adj_list.add((len(adj_map[(ar, ac)]), (ar, ac)))
    
    print(removed_rolls)


lines = read_input_file(file_path="input.txt")
solution(lines)