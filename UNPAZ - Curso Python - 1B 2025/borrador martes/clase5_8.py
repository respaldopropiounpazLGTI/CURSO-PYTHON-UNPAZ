"""try: 
    x=int(input("ingerse numero "))
except ValueError:
    print(" no es una entero ")
else:
    print("x es  ", x)"""
    
"""import random
moneda=random.choice(["cara ","cruz"])
print(moneda)   
numero=random.randint(1,99)
print(numero)"""
""""""
""""
from random import choice
moneda=choice(["cara", "cruz"])
print(moneda)"""
""""
import statistics
print(statistics.mean([100,90]))"""
"""""
# pip install cowsay
import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.cow("hola, " + sys.argv[1])

#  https://flask.palletsprojects.com/en/stable/  """
nombre=[]

for _ in  range(3):
    nombres=input("ingerse nombre")
    nombre.append(nombres)
print(sorted(nombre))


