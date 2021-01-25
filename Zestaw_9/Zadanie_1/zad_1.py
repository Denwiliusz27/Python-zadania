"""
ZADANIE 11.1
Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
(a) różne liczby int od 0 do N-1 w kolejności losowej,
(b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
(c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
(d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
(e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).
"""

import sort_module as s_m


def main():
    print("a) kolejnosc losowa: ", s_m.random_list(10))
    print("b) prawie posortowana: ", s_m.nearly_sorted(10))
    print("c) prawie posortowana w odwrotnej kolejnosci: ", s_m.nearly_sorted_reverse(10))
    print("d) rozklad Gaussa: ", s_m.random_gauss(10))
    print("e) lista z powtorzeniami: ", s_m.list_with_repeats(10))

if __name__ == '__main__':
    main()
