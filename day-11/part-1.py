from pprint import pprint
from collections import defaultdict


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
    connections = defaultdict(set)

    for line in lines:
        src, dst = line.split(': ')
        
        for dst_server in dst.split(' '):
            connections[src].add(dst_server.strip())
    
    all_paths = 0
    start_node, end_node = 'you', 'out'
    queue = [start_node]

    while queue:
        node = queue.pop()

        if node == end_node:
            all_paths += 1
            continue

        for neighbour in connections[node]:
            queue.append(neighbour)
    
    print(all_paths)


lines = read_input_file(file_path="input.txt")
solution(lines)