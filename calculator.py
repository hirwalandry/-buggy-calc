def add(a, b):
    return a + b

def process(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    total = 0
    for item in items:
        if not isinstance(item, (int, float)):
            raise ValueError("All items in the list must be numeric")
        total += item
    return tot



