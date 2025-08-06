coca=50
monedad_aceptadas=25,10,5
while True:
    print(f"monto adeudado {coca}")
    try:
        moneda=int(input("ingrese moneda "))
    except ValueError:
        print(" solo enteros ")
        continue
    if moneda!=monedad_aceptadas:
        print("solo monedas 25,10 y 5 centavos  ")
        continue
    else:
        coca-=moneda
        
        
    #debo preguntar al profesor!!!     