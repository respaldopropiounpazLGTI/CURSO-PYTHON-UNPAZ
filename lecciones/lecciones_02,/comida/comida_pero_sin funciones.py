tiempo=input("ingrese horario en formato #:## o ##:## inclusive ")
#desayunar entre las 7:00  y las 8:00,
#almorzar  entre las 12:00 y las 13:00, 
#cenar     entre las 18:00 y las 19:00 si no es ninguna no pone nada 
horas,minutos=tiempo.split(":")
print(horas)
print(minutos)
hora_pasado_a_float=float(horas)
min_a_float=float(minutos)
print(type(hora_pasado_a_float))
print(type(min_a_float))
if hora_pasado_a_float >=7 and hora_pasado_a_float <=8 and min_a_float >=00 and min_a_float<=59:#tomo en cuenta la hora y los minutos 
    print(" desayuno ")
elif hora_pasado_a_float>=12 and hora_pasado_a_float<=13 and min_a_float>=00 and min_a_float<=59:
    print("almuerzo ")
elif hora_pasado_a_float >=18 and hora_pasado_a_float<=19 and min_a_float>=00 and min_a_float<=59:
    print("cenar ")
