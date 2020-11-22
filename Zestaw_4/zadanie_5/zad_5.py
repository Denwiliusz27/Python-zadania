def check_numbers(L, left, right):
    if left < 0:
        left = 0
    if right >= len(L):
        right = len(L) - 1

    return left, right


def reverse_iteratively(L: list, left: int, right: int):
    if not left < right:
        left, right = right, left

    left, right = check_numbers(L, left, right)

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return L


def reverse_recursively(L: list, left: int, right: int):
    left, right = check_numbers(L, left, right)

    if left < right:
        L[left], L[right] = L[right], L[left]
        L = reverse_recursively(L, left + 1, right - 1)

    return L


if __name__ == '__main__':
    lista = ["ala", "marek", 3, "a", 87.3, "ZERO", " ", "kuba", 99, True]
    lista1 = lista.copy()
    print(lista)
    print("Lista odwrocona iteracyjnie: ", reverse_iteratively(lista, 0, len(lista) - 1))
    print("Lista odwrocona rekurencyjnie: ", reverse_recursively(lista1, 0, len(lista1) - 1))
