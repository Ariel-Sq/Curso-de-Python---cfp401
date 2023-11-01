productos = {
  "coca": 500,
  "fernet": 2000,
  "hielo": 200
}

print("Hola este es tu carro de compras")
print(productos)

carro = []

producto = input("Elegir producto: ")

if (producto == "coca" or producto == "fernet" or producto == "hielo"):
		carro.append(producto)
else:
		print("Disculpas, este producto no está disponible")

continuar = input("¿Elegir otro producto? si / no: ")

while continuar == "si":
    producto = input("Elegir producto: ")
    carro.append(producto)
    continuar = input("¿Elegir otro producto? si / no: ")
    while continuar != "si" and continuar != "no":
        print("Elija si o no")
        continuar = input("¿Elegir otro producto? si / no: ")

print("Productos agregados")
print(carro[:])

cuenta = 0

for prod in carro:
	cuenta = cuenta + productos[prod] 
	

print("Tu total es: " + str(cuenta))
x = input("Presiona una tecla para finalizar")