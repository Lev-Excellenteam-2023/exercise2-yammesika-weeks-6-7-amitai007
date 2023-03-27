import functools


# region decorator - this

class ParameterTypeError(TypeError):
    """Custom error to be raised if the parameter type is incorrect"""
    pass


def check_param_type(param_type):
    """Decorator factory that returns a decorator that checks if the function parameter is of the correct type."""

    def decorator(func):
        """The decorator function that checks the parameter type"""

        @functools.wraps(func)
        def wrapper(arg):
            """The wrapper function that wraps around the original function"""

            # Check if the argument passed to the function is of the correct type
            if not isinstance(arg, param_type):
                # Raise a custom error if the parameter type is incorrect
                raise ParameterTypeError(f"Expected parameter of type {param_type}, but got {type(arg)} instead.")

            # If the argument is of the correct type, call the original function with the argument
            return func(arg)

        return wrapper

    return decorator


# endregion

# region decorator suprize

def surprise_decorator(func):
    def wrapper(*args, **kwargs):
        print("Surprise!")

    return wrapper

# endregion
