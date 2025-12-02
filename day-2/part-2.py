def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        line = input_file.readline()
        return line.strip().split(',')


def solution(lines: list[str]):
    invalid_sum = 0

    for line in lines:
        start, end = line.split('-')

        n_start, n_end = len(start), len(end)
        digit_range = list(range(n_start, n_end+1))
        unique_invalids = set()

        if len(digit_range) == 1:
            n = digit_range.pop()

            for prefix in range(1, n//2 + 1):
                left_start = int(start[:prefix])
                left_end = int(end[:prefix])

                while left_start <= left_end:
                    invalid_number = str(left_start) * (n//prefix)

                    if int(start) <= int(invalid_number) <= int(end):
                        unique_invalids.add(int(invalid_number))
                    
                    left_start += 1
        else:
            for i in range(len(digit_range)):
                n = digit_range[i]

                for prefix in range(1, n//2 + 1):
                    if i==0:
                        left_start = int(start[:prefix])
                        left_end = int('9'*prefix)
                    
                    elif i==len(digit_range)-1:
                        left_start = 1
                        left_end = int(end[:prefix])
                    
                    else:
                        left_start = 1
                        left_end = int('9'*prefix)
        
                    while left_start <= left_end:
                        invalid_number = str(left_start) * (n//prefix)

                        if int(start) <= int(invalid_number) <= int(end):
                            unique_invalids.add(int(invalid_number))
                        
                        left_start += 1
        
        invalid_sum += sum(unique_invalids)
    
    print(invalid_sum)


lines = read_input_file(file_path="input.txt")
solution(lines)