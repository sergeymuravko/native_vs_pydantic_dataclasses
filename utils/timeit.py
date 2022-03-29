import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time
        print(f'Execution time {execution_time:.12f} seconds')
        return result
    return timeit_wrapper


@timeit
def calculate_sum(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    calculate_sum(1, 3)
    calculate_sum(2, 4)
