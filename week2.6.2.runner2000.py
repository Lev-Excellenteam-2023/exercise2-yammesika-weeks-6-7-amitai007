import time


# region runer - this 2000

def timer(func, *args, **kwargs):
    """
    The timer function measures the execution time of a given function with the provided arguments.

    Parameters:
    func (function): The function to be timed.
    args (tuple): The positional arguments to be passed to the function.
    kwargs (dict): The keyword arguments to be passed to the function.

    Returns:
    result (any): The return value of the function.

    """
    start = time.perf_counter()  # Get the starting time in seconds.
    result = func(*args, **kwargs)  # Call the function with the provided arguments.
    end = time.perf_counter()  # Get the ending time in seconds.
    elapsed_time = end - start  # Calculate the elapsed time.
    print(f"{func.__name__} took {elapsed_time:.6f} seconds")  # Print the elapsed time to the console.
    return result  # Return the result of the function.

# endregion
