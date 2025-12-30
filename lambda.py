# Lambda es una función anónima en Python que se utiliza para crear funciones pequeñas y de una sola línea.
# La sintaxis básica de una función lambda es la siguiente:
# lambda argumentos: expresión

X = lambda a: a + 10
print(X(5))  # Salida: 15 porque esta remplaza 'a' con 5 y suma 10

Y = lambda c, d : c + d
print(Y(3, 5))  # Salida: 8 porque esta remplaza 'c' con 3 y 'd' con 5 y suma ambos valores

# Las funciones lambda son útiles cuando se necesitan funciones pequeñas y rápidas, especialmente como argumentos para otras funciones.

def mifuncion(n):
    return lambda f : f * n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5))  # Salida: 10 porque multiplica 5 por 2, porque 'n' es 2
print(triplicador(5))  # Salida: 15 porque multiplica 5 por 3 , porque 'n' es 3