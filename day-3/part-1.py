def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    joltage = 0

    for line in lines:
        bank = [(int(line[i]), i) for i in range(len(line))]

        max_len = len(line)
        bank.sort(key=lambda x: x[0], reverse=True)

        # Find 1st Maximum
        a, a_idx = bank.pop(0)
        if a_idx == max_len - 1:
            na, na_idx = bank.pop(0)
            bank.insert(0, (a, a_idx))
            a, a_idx = na, na_idx
        
        b = None

        # Find 2nd Maximum
        for e, e_idx in bank:
            if e_idx > a_idx:
                b = e
                break
        
        joltage += 10*a + b
    
    print(joltage)


lines = read_input_file(file_path="input.txt")
solution(lines)