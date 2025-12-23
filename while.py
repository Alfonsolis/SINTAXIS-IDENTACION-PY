i = 1

print("=====WHILE 1=====")

while i < 10:
    print(i)
    i += 1 # lo mismo que i = i + 1
    # Output esperado: 1, 2, 3, 4, 5, 6, 7, 8, 9

print("=====WHILE 2=====")

a = 1

while a <= 10:
    print(a) # Output esperado: 1, 2, 3, 4, 5, porque se detiene al llegar a 5
    if a == 5: # condición de ruptura
        break # salir del ciclo
    a += 1 # cuenta hacia arriba

print("=====WHILE 3=====")

b = 1
while b <= 10:
    b +=1   # lo mismo que b = b + 1
    print(b) # Output esperado: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 porque primero incrementa y luego imprime

print("=====WHILE 4=====")

c = 0

while c < 10:
    if c == 5:
        break
    c += 2
    print(c) # Output esperado: 2, 4, 6 porque se detiene al llegar a 5

print("=====WHILE 5=====")

d = 0

while d < 10:
    d += 1
    if d == 5:
        continue # saltar el resto del código y volver al inicio del ciclo
    print(d) # Output esperado: 1, 2, 3, 4, 6, 7, 8, 9, 10 porque se salta el 5

print("=====WHILE 6=====")

e = 0

while e < 10:
    e += 1
    if e == 5:
        continue
    print(e)
else:
    print("e dejo de ser menor que 10")