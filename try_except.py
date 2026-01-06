#Aqui mostrareremos un ejemplo de manejo de excepciones en Python utilizando try y except.
# El bloque try se utiliza para envolver el código que puede generar una excepción,
# mientras que el bloque except se utiliza para manejar la excepción si ocurre.

# La sintaxis básica es la siguiente:

try:
   numero = 10 / 0  # Esto generará una excepción de división por cero
except ZeroDivisionError: # Manejo de la excepción en el cual lo ideal es escribir el tipo de excepción
    print("Se ha producido una excepción. No se puede dividir por cero.")


try:
    print(x)
except NameError:
    print("La variable x no está definida.")
finally: # El bloque finally se ejecuta siempre, haya o no una excepción, en este caso aunque X estuviera definida el bloque finally se ejecutaria
    print("Este bloque se ejecuta siempre, haya o no una excepción.")

# También podemos manejar múltiples excepciones utilizando múltiples bloques except: