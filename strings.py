# strings.py
# Este archivo demuestra diferentes formas de definir cadenas en Python.
print("Hola,'mundo'")
print('Hola, "mundo"')

ingles = "I'm Alfonso and I'm learning Python"

multiples = """Esto es una cadena
que abarca múltiples líneas.
Puedes escribir tanto como quieras 
aquí."""

print(ingles)
print(multiples)

# Método length() para obtener la longitud de una cadena

palabra = "Murciélago"
print ("La longitud de la palabra es:", len(palabra)) # Imprime la longitud de la cadena 'palabra'

texto = "Estoy en un curso de fundamentos de Python"
estaIncluida = "Python" in texto #Python es CASE SENSITIVE, así que distingue mayúsculas y minúsculas

print(estaIncluida)  # Imprime True si 'Python' está en 'texto', de lo contrario False

noEstaIncluida = "Javascript" not in texto
print(noEstaIncluida)  # Imprime True si 'Javascript' no está en

Mayusculas = texto.upper()
print(Mayusculas)  # Imprime "texto" en mayúsculas.

Minusculas = texto.lower()
print(Minusculas)  # Imprime "texto" en minúsculas.

espacios = "   Hola Mundo   "
sinEspacios = espacios.strip()
print(sinEspacios)  # Imprime "Hola Mundo" sin espacios al inicio y al final.