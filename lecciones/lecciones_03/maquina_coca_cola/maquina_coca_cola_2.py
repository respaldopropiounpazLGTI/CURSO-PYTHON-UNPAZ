coca=50
while True:
    print(f"monto adeudado {coca}")
    try:
        moneda=int(input("ingrese moneda "))
    except ValueError:
        print(" solo enteros ")
        continue
    if moneda==30:
        print("solo monedas 25,10 y centavos  ")
        continue
    else:
        coca-=moneda
        
        
    #debo preguntar al profesor!!!     