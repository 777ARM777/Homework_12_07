class LoggedInError(Exception):
    pass


def auth_dec(original_func):
    def wrapper(*args, **kwargs):
        if not is_logged_in():
            raise LoggedInError("You are not logged in")
        return original_func(*args, **kwargs)
    return wrapper


def is_logged_in():
    pass


@auth_dec
def foo():
    print("Hello world")


try:
    foo()
except LoggedInError as le:
    print(str(le))
