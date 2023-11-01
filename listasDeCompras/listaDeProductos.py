productos = []

print("Hola este es tu carro de compras")

producto = input("Elegir producto: ")

productos.append(producto)

continuar = input("¿Elegir otro producto? si / no: ")

while continuar == "si":
    producto = input("Elegir producto: ")
    productos.append(producto)
    continuar = input("¿Elegir otro producto? si / no: ")
    while continuar != "si" and continuar != "no":
        print("Elija si o no")
        continuar = input("¿Elegir otro producto? si / no: ")

print("Productos agregados")
print(productos[:])









'''for i in productos:
    if (nuevoMsj == "si"):
        msj = input("Elegir productos: ")
        productos.append(msj)
        nuevoMsj = input("¿Elegir otro producto? si / no: ")
    elif (nuevoMsj == "no"):
        print("Productos agregados")
        print(productos[:])
    else:
        print("Por favor ingresa si o no")
        nuevoMsj = input("¿Elegir otro producto? si / no: ")



x = input("Presiona una tecla para finalizar")'''