print("==============================")
palabra = "Python"

for letra in palabra:
    print(letra) # Imprime cada letra de la palabra "Python" en una línea separada

print("==============================")

frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    print(fruta) # Imprime cada fruta de la lista en una línea separada

print("==============================")

frutas2 = ["mandarina", "fresa", "aguacate"]
for frutas in frutas2: # Recorre cada fruta en la lista frutas2
    if frutas == "fresa": # Si la fruta es "frsa"
        break # Detiene el bucle
    print(frutas) # Imprime cada fruta de la lista hasta encontrar "frsa", momento en el cual se detiene el bucle

print("==============================")

juegos = ["Mario Bros", "Zelda", "Metroid", "Donkey Kong"]
for juego in juegos:
    if juego == "Zelda":
        continue # Salta a la siguiente iteración del bucle si el juego es "Zelda"
    print(juego) # Imprime cada juego de la lista, excepto "Zelda"
else:
    print("Fin del bucle") # Se ejecuta al finalizar el bucle, a menos que se haya interrumpido con break

print("==============================")

for i in range(10): # Itera desde 0 hasta 9 por que range(10) genera números del 0 al 9
    print(i) # Imprime los números del 0 al 9

print("==============================")

for n in range(3, 5): # Itera desde 3 hasta 4, ya que el rango es exclusivo del valor final
    print(n) # Imprime 3 y 4

print("==============================")

for m in range (0,10,2): # Itera desde 0 hasta 8, con un paso de 2
    print(m) # Imprime los números pares del 0 al 8
    # El tercer parámetro de range() especifica el incremento entre cada número generado.

print("==============================")

# Bucle anidado

comidas = ["Pizza con piña", "Hamburguesa", "Pasta"]
adjetivos = ["Deliciosa", "Saludable", "Económica"]
#Primero se itera sobre cada adjetivo y luego sobre cada comida
for adjetivo in adjetivos:
    for comida in comidas:
        print(comida + "," + " " + adjetivo) # Imprime cada combinación de comida y adjetivo

print("==============================")

platillos = ["Pizza con piña", "Hamburguesa", "Pasta"]
adjetivos2 = ["Deliciosa", "Saludable", "Económica"]
#Primero se itera sobre cada platillo y luego sobre cada adjetivo
for platillo in platillos:
    for adjetivo2 in adjetivos2:
        print(platillo + "," + " " + adjetivo2) # Imprime cada combinación de platillo y adjetivo

"""
Como podemos ver en estos dos últimos ejemplos,
el orden de los bucles anidados afecta el resultado final.
En el primer caso, cada adjetivo se combina con todas las comidas,
mientras que en el segundo caso, cada platillo se combina con todos los adjetivos

"""

print("==============================")

for y in range(10):
    pass # El bucle itera de 0 a 9 pero no realiza ninguna acción debido a la instrucción pass