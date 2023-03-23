from itertools import cycle, islice


# region interleave
# https://stackoverflow.com/questions/3678869/pythonic-way-to-combine-interleave-interlace-intertwine-two-lists-in-an-alte

def round_robin(*iterables):
    """round_robin('ABC', 'D', 'EF') --> A D E B F C"""
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))

# endregion
