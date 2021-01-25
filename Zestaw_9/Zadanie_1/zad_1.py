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

#print(s_m.insert_sort(s_m.random_list(10)))
print(s_m.nearly_sorted(10))
