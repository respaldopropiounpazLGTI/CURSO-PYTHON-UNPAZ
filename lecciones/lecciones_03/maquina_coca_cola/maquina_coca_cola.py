coca=50
#debo `pregunta!`
while True:
    try:
        print(f"cantidad adeudada {coca}")
        moneda=int(input("ingrese moneda : "))
        coca-=moneda
        #print(f"cantidad adeudada {coca}")
    except ValueError:
        print(" solo numeros enteros !!!")
        continue
    #aca hice un contador y bajando el precio no es necesartio el if /elif pero lo pongo abajo y despues preguntp al rpofesor 
    if moneda==50 or coca==0:
        print("monto justo gracias por su compra ")
        break
    if moneda==25:
        continue
    elif moneda==10:
        continue
    elif moneda==5:
        continue
    else:
        print("S")
        break #fui por la parte de un contador en esete caso descuenta los if /elif no son necesario pero entiendo creo que es por las ramificaciones 
    
    
   
        
    
        
        
        
    
    
    


        
        
        
    