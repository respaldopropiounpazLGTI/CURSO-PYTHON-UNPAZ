"""Haciendo caras
Antes de que existieran los emoji, existían los emoticones, donde texto como :) era una
cara feliz y texto como :( era una cara triste. ¡Hoy en día, los programas tienden a convertir
emoticones a emoji automáticamente!
En un archivo llamado caras.py, implementa una función llamada convertir que acepte
🙂
(también conocido como cara ligeramente sonriente) y cualquier :( convertido a 🙁
un str como entrada y devuelva esa misma entrada con cualquier :) convertido a
(también conocido como cara ligeramente fruncida). Todo el texto demás debe devolverse
sin cambios.
Luego, en ese mismo archivo, implementa una función llamada main que solicite al usuario
una entrada, llame a convertir con esa entrada, e imprima el resultado. Eres bienvenido,
pero no requerido, a solicitar explícitamente al usuario, como pasando un str propio como
argumento a input. Asegúrate de llamar a main al final de tu archivo.
Pistas
●​ Recuerda que input devuelve un str, según
docs.python.org/3/library/functions.html#input.​
●​ Recuerda que un str viene con bastantes métodos, según
docs.python.org/3/library/stdtypes.html#string-methods.​
●​ Un emoji es en realidad sólo un carácter, así que puedes citarlo como cualquier str,
🙂
como " ". Y puedes copiar y pegar el emoji de esta página en tu propio código
según sea necesario.​
Demostración
$ python caras.py
Hola :)
Hola
$ python caras.py
Adios :(
Adios
$"""
def convierte(texto):
    primercambio=texto.replace(":)"," 🙂")
    segundocambio=primercambio.replace(":("," 🙁")
    return segundocambio



def main():
    caras=input("ingrese el texto mas  la carita ")   
    obtendo=convierte(caras)
    print(obtendo)


# preguntar me confunde como se interpreta los parametros 
main()
   
