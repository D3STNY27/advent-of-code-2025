from pprint import pprint
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as f:
        return [line.strip() for line in f]


def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Time (ms): {(perf_counter() - start_time) * 1000:.2f}")
        return result
    return wrapper


@measure_time
def solution(lines):
    total_min_presses = 0

    for line in lines:
        buttons_start_idx = line.index('(')
        joltage_start_idx = line.index('{')
        buttons_segment = line[buttons_start_idx:joltage_start_idx-1].split()

        buttons = [list(map(int, button_str.strip('()').split(','))) for button_str in buttons_segment]
        joltage = list(map(int, line[joltage_start_idx+1:-1].split(',')))

        P = len(joltage)
        B = len(buttons)

        A_eq = np.zeros((P, B), dtype=float)
        for j, btn in enumerate(buttons):
            for p in btn:
                A_eq[p, j] = 1.0

        b_eq = np.array(joltage, dtype=float)
        c = np.ones(B, dtype=float)

        bounds = Bounds([0]*B, [np.inf]*B)
        integrality = np.ones(B, dtype=int)
        constraints = LinearConstraint(A_eq, b_eq, b_eq)
        result = milp(c=c, integrality=integrality, bounds=bounds, constraints=[constraints])

        if not result.success:
            continue

        counts = [int(round(x)) for x in result.x]
        total_min_presses += sum(counts)

    print(total_min_presses)


lines = read_input_file("input.txt")
solution(lines)
