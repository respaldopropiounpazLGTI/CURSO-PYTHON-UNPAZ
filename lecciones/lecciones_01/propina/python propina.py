
def main():
    dolares = dolar_a_float(input("Cuánto costó la comida? "))
    porcentaje = porcentaje_a_float(input("Qué porcentaje te gustaría dejar de propina? "))
    propina = dolares * porcentaje
    print(f"Dejar ${propina:.2f}")


def dolar_a_float(d):
    return float(d.replace('$', ''))

def porcentaje_a_float(p):
    return float(p.replace('%', '')) / 100


main()

"""""
Bueno, hemos escrito la mayor parte de una calculadora de propinas para ti.
Desafortunadamente, no tuvimos tiempo de implementar dos funciones:
●​ dolar_a_float, que debería aceptar un str como entrada (formateado
como $##.##, donde cada # es un dígito decimal), eliminar el $ inicial, y
devolver la cantidad como un float. Por ejemplo, dado $50.00 como
entrada, debería devolver 50.0.​
●​ porcentaje_a_float, que debería aceptar un str como entrada
(formateado como ##%, donde cada # es un dígito decimal), eliminar el %
final, y devolver el porcentaje como un float. Por ejemplo, dado 15% como
entrada, debería devolver 0.15.​"""