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
    rolls_to_remove = 0

    def is_valid_roll(r, c):
        nonlocal R, C, lines
        roll_count = 0

        for dr, dc in DIRECTIONS:
            rn, cn = (r + dr), (c + dc)

            if rn < 0 or cn < 0 or rn >= R or cn >= C:
                continue
        
            if lines[rn][cn]=='.':
                continue
        
            roll_count += 1
    
        return roll_count < 4
    

    roll_cells = []
    for r in range(R):
        for c in range(C):
            if lines[r][c]=='.':
                continue

            roll_cells.append((r, c))
    

    while roll_cells:
        r, c = roll_cells.pop()

        if is_valid_roll(r, c):
            rolls_to_remove += 1
    
    print(rolls_to_remove)


lines = read_input_file(file_path="input.txt")
solution(lines)