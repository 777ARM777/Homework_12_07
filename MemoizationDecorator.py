cache = {}


def MemoizationDecorator(original_func):
    def wrapper(*args, **kwargs):
        k = (args, tuple(kwargs.keys()))
        if k not in cache:
            cache[k] = original_func(*args, **kwargs)
            # print(cache)
        return cache[k]

    return wrapper


@MemoizationDecorator
def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


print(fib(10))
print(fib(6))
print(fib(20))
