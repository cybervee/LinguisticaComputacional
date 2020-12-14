mutantes = ['Rita Lee', 'Arnaldo Baptista', 'Sérgio Dias']
primos = [2, 3, 5, 7, 11, 13, 17]
meses_e_dias = [['jan', 31], ['fev', 28], ['mar', 31]]

print(len(primos))
print(len(meses_e_dias))

print(mutantes[0][5:])
print(meses_e_dias[-1][0])
print(meses_e_dias[-1][0][0])

print(mutantes)
mutantes[2] = 'Sérgio Dias Baptista'
print(mutantes)

print(primos)
primos.append(19)
print(primos)
print(primos + [23])
