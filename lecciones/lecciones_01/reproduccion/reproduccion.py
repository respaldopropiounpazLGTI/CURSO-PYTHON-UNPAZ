"""Velocidad de reproducción
Algunas personas tienen la costumbre de dar conferencias hablando bastante
rápido, y sería bueno ralentizarse, al estilo de la velocidad de reproducción de 0.75
de YouTube, o incluso haciendo que hagan pausas entre palabras.
En un archivo llamado reproduccion.py, implementa un programa en Python que
solicite al usuario una entrada y luego muestre esa misma entrada, reemplazando
cada espacio con ... (es decir, tres puntos).
Pistas
●​ Recuerda
que
input
devuelve
docs.python.org/3/library/functions.html#input.​
●​ Recuerda
un
que un str viene con bastantes
docs.python.org/3/library/stdtypes.html#string-methods.
str,según
métodos,según
Demostración
$ python reproduccion.py
Esto es curso de Python
Esto...es...curso…de…Python.
$"""
palabra=input("ingrese parrafo ").replace(" ","...")
print(" la palabra con replace es ",palabra)