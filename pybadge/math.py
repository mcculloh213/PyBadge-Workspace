def minmax(value: int or float, minimum: int or float, maximum: int or float):
    assert minimum < maximum, "Illegal min/max values!"
    return max(minimum, min(value, maximum))
