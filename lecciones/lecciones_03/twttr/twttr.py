# se que esta mal pero cumple la funcion la idea original es iterar con for 
#ahora lo hago asi despues modificio 
vocales="aeiou"
letra=input("ingrese cadena de texto : ").lower()
nuevo_texto=letra
for i in vocales:
    solo_muestra=i
    nuevo_texto=nuevo_texto.replace(i,"")
print(solo_muestra[0])#esto es solo para ver que hace claro pero solo muestra la ulyima letra ya que itera 
#igualmete no da por que itera y va de la a asta la u osea hace a,e,i,o,u pero lo hace tan rapido que solo muestra la u      
#igualmnte esto es solo curiosidad mia nada mas 
print(nuevo_texto)    