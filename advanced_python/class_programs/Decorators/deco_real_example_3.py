import time


def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_called = [0.0]

        def wrapper(*args, **kwargs):
            elapsed = time.clock() - last_called[0]
            wait_required = min_interval - elapsed
            if wait_required > 0:
                time.sleep(wait_required)
            last_called[0] = time.clock()
            return func(*args, **kwargs)

        return wrapper

    return decorate


@rate_limited(1)  # Limit to 1 call per second
def print_number(num):
    print(num)


for i in range(3):
    print_number(i)
