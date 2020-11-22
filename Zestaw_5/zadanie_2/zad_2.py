import functools


def pamiec(func):
    dictionary = {0: 0, 1: 1}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[0] not in dictionary:
            dictionary[args[0]] = wrapper(args[0] - 1) + wrapper(args[0] - 2)

        return dictionary[args[0]]

        # tu powinien być kod tworzący słownik (element - wartość), który jest sprawdzany
        # do obliczeń wyrazów ciągu - które by były wyliczane rekurencyjnie i wpisywane
        # do słownika tylko gdy wcześniej nie były obliczone
        # normalnie bez buforowania by było return func(*args, **kwargs)

    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(10):
        print(fibonacci(i))

