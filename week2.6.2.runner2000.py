# region runer - this 2000

import time


def timer(func, *args, **kwargs):
    """
    Measure the execution time of a given function with the provided arguments.
    
    Args:
        func (function): The function to be timed.
        *args (tuple): The positional arguments to be passed to the function.
        **kwargs (dict): The keyword arguments to be passed to the function.
    
    Returns:
        any: The return value of the function.
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    elapsed_time = end - start
    print(f"{func.__name__} took {elapsed_time:.6f} seconds")
    return result

# endregion

def main():
    # Example usage of timer function
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    n = 30
    result = timer(fib, n)
    print(f"fib({n}) = {result}")


if __name__ == "__main__":
    main()

