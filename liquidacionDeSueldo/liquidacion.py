# Mensaje de inicio

msj=print("Sistema de liquidación")

#Defino las variables principales que necesito para calcular el sueldo

empleado = input("Ingrese nombre del Empleado: ")
horas_Trabajadas = int(input("Horas trabajadas: "))
valor_de_hora = 2000
descuentos = 0.14

# Creo la funcion para liquidar

def liquidacion(horas, valor):
  bruto = horas_Trabajadas * valor_de_hora
  aportes = bruto * descuentos
  total = bruto - aportes
  return print("El sueldo neto es de " + str(total))


# Llamo a la función y la muestro en la consola

print(liquidacion(horas_Trabajadas, valor_de_hora))


x= input("Presione una tecla para finalizar")

