def ValidationDecorator(original_func):
    def wrapper(*args, **kwargs):
        k = args + tuple(kwargs.values())
        for i in k:
            if not isinstance(i, int):
                raise ValueError(f"{i} must be integer")
            if i < 0 or i > 10:
                raise ValueError(f"{i} must be between 0 and 10 but got {i}")
        return original_func(*args, **kwargs)
    return wrapper


@ValidationDecorator
def mul(a, b, c):
    return a * b * c


try:
    print(mul(8, 8, 15))
except ValueError as ve:
    print(str(ve))
