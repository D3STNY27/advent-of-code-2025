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
    R, C = len(lines), len(lines[0])
    splitters = {}

    beam = None
    for r in range(R):
        for c in range(C):
            if lines[r][c] == 'S':
                beam = c

            if lines[r][c] == '^':
                if r not in splitters:
                    splitters[r] = set()

                splitters[r].add(c)
    

    beams = set([beam])
    splits = 0

    for r in range(1, R):
        if r not in splitters:
            continue

        new_beams = set()
        while beams:
            beam = beams.pop()
            
            if beam not in splitters[r]:
                new_beams.add(beam)
            else:
                new_beams.add(beam-1)
                new_beams.add(beam+1)
                splits += 1
        
        beams = new_beams

    print(splits)


lines = read_input_file(file_path="input.txt")
solution(lines)