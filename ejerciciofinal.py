class Proceso:
    def __init__(self):
        pass
    def retroceso(self, palabra):
        texto = ""
        for i in palabra:
            texto += i
            if i == "#":
                texto = texto[:-2]
        print(texto)

palabra = str(input("Introduzca el texto: "))

numerales = Proceso()

numerales.retroceso(palabra)
