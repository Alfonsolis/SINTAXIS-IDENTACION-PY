# Con Python podemos manejar archivos de texto de manera sencilla. Aquí hay un ejemplo básico de cómo
# abrir, leer, escribir y cerrar un archivo de texto.
# Abrir un archivo en modo escritura (crea el archivo si no existe)
#Pero, primero la sintaxis básica para abrir un archivo es:

# open(nombre, modo)
# Modos comunes:
# 'r' - lectura (read)
# 'w' - escritura (write) sobrescribe el archivo si ya existe
# 'a' - añadir (append)
# 'r+' - lectura y escritura (read and write)
# 'b' - modo binario (binary mode)
# 'x' - crear un nuevo archivo (create)
try:
    f = open("archivo_ejemplo.txt", "r") # Abrir archivo en modo lectura
    print(f.readline()) # Leer una línea del archivo
    f.close() # Cerrar el archivo
except FileNotFoundError:
    print("El archivo no existe.")

#Ahora veremos with, que es la forma recomendada de manejar archivos en Python, 
# ya que asegura que el archivo se cierre correctamente después de su uso.

try:
    with open("archivo.txt", "r", encoding="utf-8") as g: # Abrir archivo en modo lectura. El uncoding es opcional pero recomendado para evitar problemas con caracteres especiales
        print(g.readline()) # Leer una línea del archivo
        print(g.readline()) # Leer todas las líneas del archivo
except FileNotFoundError:
    print("El archivo aun no existe.")


try:
    with open("archivo.txt", "w", encoding="utf-8") as g: # Abrir archivo en modo escritura
        g.write("Hola, mundo ahora desde codigo Python!\n") # Escribir una línea en el archivo
        g.write("Segunda línea escrita desde Python.\n") # Escribir otra línea
    with open("archivo.txt", "r", encoding="utf-8") as g:
        print(g.readline())
        print(g.readline())
except FileNotFoundError:
    print("El archivo aun no existe.")


try:
    with open("archivo.txt", "a", encoding="utf-8") as g: # Abrir archivo en modo añadir
        g.write("Hola, mundo usando append!\n") # Escribir una línea en el archivo
        g.write("Esto no va a sobrescribir el archivo.\n") # Escribir otra línea
    with open("archivo.txt", "r", encoding="utf-8") as g:
        print(g.read()) # Leer todo el contenido del archivo con read()
except FileNotFoundError:
    print("El archivo aun no existe.")


try:
    with open("archivo2.txt", "r", encoding="utf-8") as d:
        print(d.read()) # Leer todo el contenido del archivo con read()
except FileNotFoundError:
    open("archivo2.txt", "x", encoding="utf-8") # Crear un nuevo archivo si no existe
    print("El archivo no existe. Se va a crear uno nuevo.")

try:
    with open("archivo2.txt", "a", encoding="utf-8") as d:
        d.write("Esto se escribe despues de crear el archivo.\n")
        d.write("Ahora esto ya existe en el archivo2.txt\n")
    with open("archivo2.txt", "r", encoding="utf-8") as d:
        print(d.read()) # Leer todo el contenido del archivo con read()
except FileNotFoundError:
    print("El archivo aun no existe.")