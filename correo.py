correo= input("Escribe tu correo: ")

correos = []

if "@gmail.com" in correo:
    correos.append(correo)
    print("Correo agregado")
else:
    print("Correo incorrecto")

x= input("presiona una tecla para terminar")

