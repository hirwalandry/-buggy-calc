def add(a, b):
    return a + b


def process(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
def add(a, b):
    return a + b


def process(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    total = 0
    for item in items:
        total += item
    return total
