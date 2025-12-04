def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_maximum_number(line: str) -> str:
    digits_to_remove = len(line) - 12
    stack = [] 

    for digit in line:
        while digits_to_remove and stack and stack[-1] < digit:
            stack.pop()
            digits_to_remove -= 1

        stack.append(digit)

    return ''.join(stack[:12])


def solution(lines: list[str]):
    joltage = 0

    for line in lines:
        number = int(get_maximum_number(line))
        joltage += number
    
    print(joltage)


lines = read_input_file(file_path="input.txt")
solution(lines)