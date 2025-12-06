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


@measure_time
def solution(lines: list[str]):
    operators = lines[-1].strip().split()
    answers = [None for _ in range(len(operators))]

    for line in lines[:-1]:
        numbers = list(map(int, line.strip().split()))
        
        for i in range(len(numbers)):
            if answers[i] is None:
                answers[i] = numbers[i]
            else:
                if operators[i] == '+':
                    answers[i] += numbers[i]
                else:
                    answers[i] *= numbers[i]
    
    print(sum(answers))


lines = read_input_file(file_path="input.txt")
solution(lines)