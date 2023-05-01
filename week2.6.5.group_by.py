# region group by - this 2

def group_by(func, iterable):
    """
    Returns a dictionary where the keys are the result of applying the input function
    on each item in the input iterable, and the values are a list of items from the
    input iterable that result in the same key.
    """
    return {func(item): [item] if func(item) not in result else result[func(item)].append(item) or result[func(item)] for item in iterable}
     # for item in iterable:
     #   key = func(item)  # Apply the input function on the item to get the key
     #   if key not in result:
     #       result[key] = [item]  # If key not in dictionary, add a new key-value pair
     #   else:
     #      result[key].append(item)  # If key already in dictionary, append item to existing value


# endregion

def main():
    data = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    result = group_by(len, data)
    print(result)

if __name__ == "__main__":
    main()
