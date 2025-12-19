# Operadores de asignación

x = 5

x = x + 3  # Asignación simple
print(x)  # Salida: 8

x += 3  # Asignación con suma
print(x)  # Salida: 11

x -= 6  # Asignación con resta
print(x)  # Salida: 5

x *= 3  # Asignación con multiplicación
print(x)  # Salida: 15

x /=3  # Asignación con división
print(x)  # Salida: 5.0

x %= 2  # Asignación con módulo
print(x)  # Salida: 1.0

print("==========================")

y = 20

y //= 2  # Asignación con división entera
print(y)  # Salida: 10
y **= 3  # Asignación con potencia
print(y)  # Salida: 1000

print("==========================")

# WARLUS (morsa) := operador de asignación de expresión (Python 3.8+)

print(z:= 3) # Asignación y salida inmediata
print(z) # Salida: 3