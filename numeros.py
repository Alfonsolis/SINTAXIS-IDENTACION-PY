x = 1
y = 2.5
z = 3j

# Imprimir los valores y sus tipos
print("Tipo de x:", type(x))
print("Tipo de y:", type(y))
print("Tipo de z:", type(z))

# Ejemplos adicionales de números en Python
positivo = 5.5
negativo = -3.5

imaginario = -2 + -3j

# Conversión de tipos numéricos
# Convertir x a float y y a int
xf = float(x)
print("x como float:", xf)
print("Tipo de xf:", type(xf))
# Convertir y a int
yi = int(y)
print("y como int:", yi)
print("Tipo de yi:", type(yi))

# ¿Podemos pasar de números complejos a otros tipos?
# No, esto generará un error
# zi = int(z)  # Descomentar esta línea generará un error

# Sin embargo, podemos convertir números complejos a cadenas
zs = str(z)
print("z como cadena:", zs)
print("Tipo de zs:", type(zs))

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print("enteroComplejo:", enteroComplejo)
print("Tipo de enteroComplejo:", type(enteroComplejo))
print("flotanteComplejo:", flotanteComplejo)
print("Tipo de flotanteComplejo:", type(flotanteComplejo))

import random  # noqa: E402
print(random.randrange(1,10)) # Imprime un número aleatorio entre 1 y 9, incluyendo el 1 pero excluyendo el 10.
