x = 5
y = 3
z = 1

if x > y and x > z: # if es una estructura condicional que evalúa si una condición es verdadera
    print("x es mayor a y y x es mayor a z")
elif x == y: # elif permite evaluar una segunda condición si la primera es falsa
    print("x es igual a y")
else: # else se ejecuta si ninguna de las condiciones anteriores es verdadera
    print("Ninguna se cumple")

    # Se puede comparar múltiples variables usando operadores lógicos como 'and' y 'or'

a = "Python"
b = "Javascript"
c = "Python"

if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")

if a == c:
    if a != b: # anidando condiciones if dentro de otro if
         print("a es igual a c y a no es igual a b")
    else:
        print("Saliendo por un else interno")
else:
    print("a no es igual a c")

e = 10
f = 10

if e == f:
    pass  # pass es una declaración que no hace nada, se usa como un marcador de posición