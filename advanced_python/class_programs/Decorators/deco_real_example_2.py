import logging


def log_func_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log_func_call
def add(x, y):
    return x + y


# Assuming logging is configured to display INFO level messages
print(add(5, 7))
