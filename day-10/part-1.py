from pprint import pprint


MAX_DEPTH = 10


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
    min_pressure = 0

    for line in lines:
        target_end_idx = line.index(']')
        target = line[1:target_end_idx]

        joltage_start_idx = line.index('{')
        buttons_strip = line[target_end_idx+2:joltage_start_idx-1]

        buttons = []
        for button_str in buttons_strip.split(' '):
            button = button_str.strip('()')
            buttons.append(list(map(int, button.split(','))))
        
        queue = [(0, None, '.'*len(target))]
        visited = set()

        while queue:
            buttons_pressed, last_pressed, state = queue.pop(0)

            if buttons_pressed >= MAX_DEPTH:
                continue

            if state==target:
                min_pressure += buttons_pressed
                break

            for i in range(len(buttons)):
                if last_pressed is not None and last_pressed==i:
                    continue

                final_state = ''
                button = buttons[i]

                for j in range(len(state)):
                    if j not in button:
                        final_state += state[j]
                    else:
                        if state[j]=='.':
                            final_state += '#'
                        else:
                            final_state += '.'

                if final_state not in visited:
                    visited.add(final_state)
                    queue.append((buttons_pressed+1, i, final_state))
    
    print(min_pressure)


lines = read_input_file(file_path="input.txt")
solution(lines)