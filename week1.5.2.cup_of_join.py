# region Cup of join

def Cup_of_join(*args, sep='-'):
    """Accepts an unlimited number of lists, parameter sep.
        returns one list consisting of all the lists received as parameters,
        If the sep parameter is provided concatenates it as a member between any two lists.
        If it is not provided, the character "-" must be concatenated instead"""
    result = []
    if len(args) == 0:
        return None
    for arg in args:            # on every argument add the argument and a sep
        result.extend(arg)
        result.append(sep)
    result.pop()                # remove last separator
    return result

# endregion
