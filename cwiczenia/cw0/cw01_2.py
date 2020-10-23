lista1 = ["apple", "banana", "cherry"]
lista2 = lista1  # .copy()
lista2[0] = "jablko"
print(lista1)
print(lista2)

#==================================================================

fruits = ["apple", "banana", "cherry", "APPLE", "BANANA", "CHERRY"]

for fruit in fruits:
    fruits[fruit] = fruit[::-1]

print(fruits)