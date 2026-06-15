def add(a, b):
    return a + b

def process(items):
    if not isinstance(items, list) or not all(isinstance(item, (int, float)) for item in items):
        raise ValueError('Input must be a list of numbers')
    total = 0
    for item in items:
        total += ite
    return tota