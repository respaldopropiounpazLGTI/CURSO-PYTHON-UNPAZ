pregunta=input("¿Cuál es la respuesta a la gran pregunta sobre la vida, el universo y todo lo demás? ")
if  pregunta=="42":
    print("SI")
elif pregunta.lower()=="cuarenta y dos":
    print("SI")
elif pregunta.lower().replace(" ","")=="cuarentaidos":
    print("SI")
else:
    print("NO")
    

