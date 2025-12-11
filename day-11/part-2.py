from collections import defaultdict


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as f:
        return [line.strip() for line in f.readlines()]


def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"Time (ms): {(perf_counter() - start) * 1000}")
        return result
    return wrapper


@measure_time
def solution(lines):
    connections = defaultdict(set)

    for line in lines:
        src, dst = line.split(': ')
        
        for dst_server in dst.split(' '):
            connections[src].add(dst_server.strip())

    start_node, end_node = 'svr', 'out'
    fft_node, dac_node = 'fft', 'dac'

    cache = {}
    def recurse(src, dst, visited):
        if src == dst:
            return 1

        cache_key = (src, dst)
        if cache_key in cache:
            return cache[cache_key]

        visited.add(src)
        paths_count = 0

        for neighbour in connections[src]:
            if neighbour not in visited:
                paths_count += recurse(neighbour, dst, visited)

        visited.remove(src)

        cache[cache_key] = paths_count
        return cache[cache_key]


    # Piece-Wise Calculations
    src_to_fft = recurse(start_node, fft_node, set())
    src_to_dac = recurse(start_node, dac_node, set())

    fft_to_dac = recurse(fft_node, dac_node, set())
    dac_to_fft = recurse(dac_node, fft_node, set())

    fft_to_out = recurse(fft_node, end_node, set())
    dac_to_out = recurse(dac_node, end_node, set())

    # Count Total Paths
    total_paths = (src_to_fft * fft_to_dac * dac_to_out) + (src_to_dac * dac_to_fft * fft_to_out)
    print(total_paths)


lines = read_input_file("input.txt")
solution(lines)
