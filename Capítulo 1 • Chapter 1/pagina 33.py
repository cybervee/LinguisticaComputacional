numeros = [1, 1, 2]
conjunto = set(numeros)
print(conjunto)

pares = {2, 4, 6, 8}
primos = {2, 3, 5, 7, 11, 13, 17, 19, 23}
print(primos | pares)
print(primos & pares)
print(primos - pares)
print(pares - primos)
