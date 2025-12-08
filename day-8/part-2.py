from pprint import pprint
from heapq import heappush, heappop
from collections import defaultdict


class DisjointSetUnion:
    def __init__(self):
        self.parent = {}
        self.size = {}


    def add(self, x):
        if x in self.parent:
            return
        
        self.parent[x] = x
        self.size[x] = 1


    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x


    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


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
    points = [tuple(map(int, line.split(','))) for line in lines]
    distances = []

    n = len(points)
    pid = 0
    pid_to_pair = {}

    # Initialize Single Point Circuits
    circuits = DisjointSetUnion()
    for p in points:
        circuits.add(p)

    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            
            d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
            heappush(distances, (d, pid))

            pid_to_pair[pid] = (points[i], points[j])
            pid += 1

    components = n
    while distances:
        _, pid = heappop(distances)
        p1, p2 = pid_to_pair[pid]

        if circuits.union(p1, p2):
            components -= 1

            if components==1:
                print(p1[0] * p2[0])
                break

lines = read_input_file(file_path="input.txt")
solution(lines)