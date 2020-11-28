import functools


def pamiec(func):
    dictionary = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[0] not in dictionary:
            dictionary[args[0]] = func(args[0])

        return dictionary[args[0]]

    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(100):
        print("fib(", i, ") =", fibonacci(i))
