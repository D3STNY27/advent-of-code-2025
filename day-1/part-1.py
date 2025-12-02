def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def update_position(position: int, direction: str, rotation: int) -> int:
    if direction == "R":
        return (position + rotation) % 100
    
    if direction == "L":
        return (position - rotation) % 100
    
    return position


def solution(lines: list[str]):
    position = 50
    zero_count = 0

    for line in lines:
        direction, rotation = line[0], int(line[1:])
        position = update_position(position, direction, rotation)

        if position == 0:
            zero_count += 1
    
    print(zero_count)


lines = read_input_file(file_path="input.txt")
solution(lines)