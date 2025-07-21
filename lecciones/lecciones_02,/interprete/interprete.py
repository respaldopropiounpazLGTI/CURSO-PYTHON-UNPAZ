entreda=input(" ingrese expresion matematica por ejemplo --> #_+_# con espacios ")# entiendo que en el pdf se debe ingresar  1+1 con espacios 
#si no da error siempre este ejercio me volvio loco!!! jajja
x ,y ,z =entreda.split()
print(x) #solo verifico que sea lo que busco 
print(y)
print(z)
valor1=int(x)
lo_que_pide_el_usuario=str(y)
valor2=int(z)
print(type(valor1)) #otra ver verifico que sea lo que estoy esperando !!! paso a paso por que es re dificil!!! jajajajaj 
print(type(lo_que_pide_el_usuario))
print(type(valor2))
if lo_que_pide_el_usuario=="+":
    suma=valor1+valor2
    flotante=float(suma)
    print(f"la suma es :{flotante}")## jajajaj que bueno no lopuedo cree!! lo logre!!! jajajajaj 
elif lo_que_pide_el_usuario=="-":
    resta=valor1-valor2
    flotante=float(resta)
    print(f" la resta es : {flotante}")
elif lo_que_pide_el_usuario=="*":
    multi=valor1*valor2
    flotante=float(multi)
    print(" la multiplicacion es : ",flotante)
elif lo_que_pide_el_usuario=="/":
    if valor2==0:
        print(" no se puede dividir por 0 el resultadio da error ")
    else:
        divi=valor1/valor2
        print(f" la division es {divi}")
else:
    print("error interprete valores o expresion errorea ") #al fin me volvio loco!! jaja   