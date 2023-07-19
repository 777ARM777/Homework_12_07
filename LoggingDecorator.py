def LoggingDec(original_func):
    import logging
    print(original_func.__name__)
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"Function: {original_func.__name__}")
        logging.info(f"Ran with args: {args}, and kwargs {kwargs}")
        return original_func(*args, **kwargs)
    return wrapper


@LoggingDec
def foo(a, b, c):
    return a + b + c


foo(1, 2, 3)
