ingreso_o_no_mayuscula = input("Ingrese nombre de variable en formato camel case o no !!!   ")
variable_contenedora=""#variable vacia
for i in range(len(ingreso_o_no_mayuscula)):  #bucle for cantidad led de letras lend devuelve numero de letra 
    letra = ingreso_o_no_mayuscula[i]#posiciioin  i 012345 etc

    if letra.isupper():#si letra esta en mayuscila hacer pone _ y convierte a minuscula
        variable_contenedora += "_" + letra.lower()
    else:
        variable_contenedora += letra # si no hay nada 

print(f"La palabra en snake case es: {variable_contenedora}") #imprime 
# como falte me perdi la clase no sabia issuper  todo lo demas si !!! 
#debo consultar 