def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def update_position(position: int, direction: str, rotation: int) -> int:
    full_rotations = rotation // 100
    rotation %= 100

    new_position = (position + rotation) if direction=="R" else (position - rotation)

    if new_position >= 100:
        return new_position % 100, (1 + full_rotations)
    
    if new_position < 0 and position != 0:
        return new_position % 100, (1 + full_rotations)
    
    if new_position < 0:
        return new_position % 100, full_rotations
    
    if new_position == 0:
        return new_position, 1 + full_rotations
    
    return new_position, full_rotations


def solution(lines: list[str]):
    position = 50
    zero_count = 0

    for line in lines:
        direction, rotation = line[0], int(line[1:])
        new_position, zero_crossings = update_position(position, direction, rotation)

        zero_count += zero_crossings
        position = new_position
    
    print(zero_count)


lines = read_input_file(file_path="input.txt")
solution(lines)