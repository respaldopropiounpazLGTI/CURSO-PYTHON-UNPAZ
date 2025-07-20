"""Einstein
Incluso si no has estudiado física (recientemente o nunca!), podrías haber oído que
E = mc², donde E representa energía , m representa masa
 y c representa la velocidad de la luz 300,000,000 metros por segundo), según Albert Einstein et
al. Esencialmente, la fórmula significa que masa y energía son equivalentes.
En un archivo llamado einstein.py, implementa un programa en Python que
solicite al usuario la masa como un entero (en kilogramos) y luego muestre el
número equivalente de Joules como un entero. Asume que el usuario ingresará un
entero.
Demostración
$ python einstein.py
m: 50
E: 4500000000000000000
$
E=mc², establece que la energía (E) es igual a la masa (m) multiplicada por el cuadrado de la velocidad de la luz (c²)
"""
def eistein():
    masa=int(input("ingrese masa "))#pido entrada en entero despues igualo masa y enercia como sice el enunciado son iguales 
    energia=masa
    velocidad_luz=(300000000**2)
    cuenta=masa*velocidad_luz
    print("número equivalente de Joule",cuenta)
#es muy confuso !!!!!!!!!
eistein()