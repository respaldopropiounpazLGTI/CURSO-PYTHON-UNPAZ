nombre=input("ingrese nombre del archivo y su extension  ").lower().strip()
if nombre.endswith(".jpg"):#se utiliza la funcion endswith evalua una cadena su terminacion devuelve true o falso osea print
    print("imagen/jpeg")
elif nombre.endswith(".gif"):
    print("imagen/gif")
elif nombre.endswith(".png"):
    print("imagen/png")
elif nombre.endswith(".pdf"):
    print("aplicacion/pdf")
elif nombre.endswith(".txt"):
    print("texto/txt")
elif nombre.endswith(".zip"):
    print("comprimido/zip")
elif nombre.endswith(" "):
    print("application/octet-stream ")
else:
    print("application/octet-stream ")
