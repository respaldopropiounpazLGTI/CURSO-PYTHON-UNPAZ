saludo=input(" pide al usuario un saludo :").lower().replace(" ","")
if  saludo=="hola":
    print("$ 0 ")
elif saludo[0]=="h" or not "hola":
    print("devuelve $20 ")
else:
    print("devuelve $100")
#se debe consultar para tener una seguridad de la logica 


