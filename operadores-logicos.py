x = 5
y =3
z = 5

print(x == y) # False
print(x != y) # True
print(x > y)  # True
print(x < y)  # False
print(x >= y) # True
print(x > z)  # False
print(z >= z) # True
print(x <= z) # True

#Operadores lógicos

print(x > y and y > z) # False
print(x == y or y > z)  # False

v = True
f = False

print(not (v)) # False
print(not(f)) # True