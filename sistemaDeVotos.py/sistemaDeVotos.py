from os import system

# Lista de candidatos

candidatos = ["Milei", "Massa", "Bullrich", "Scuiaretti, Bregman"]

# votos de candidatos

milei = 0
massa = 0
bullrich = 0
Schiaretti = 0
bregman = 0

# Pantalla de inicio

print("Bienvenido al nuevo sistema de votos Argentina 2023")

while True:
    inicio = input("Ingrese V para votar, C para ver los candidatos, R para ver los resultados o S para salir: ")

    if inicio.lower() == "v":
      voto = input("Elijí tu candidato:  Milei, Massa, Bullrich, Schiaretti o Bregman: ")

      if voto.lower() == "milei":
        nuevoVoto = 1
        milei = nuevoVoto + milei
        print("Gracias pr tu voto")
      elif voto.lower() == "massa":
         nuevoVoto = 1
         massa = nuevoVoto + massa
         print("Gracias pr tu voto")
      elif voto.lower() == "bullrich":
         nuevoVoto = 1
         bullrich = nuevoVoto + bullrich
         print("Gracias pr tu voto")
      elif voto.lower() == "schiaretti":
         nuevoVoto = 1
         Schiaretti = nuevoVoto + Schiaretti
         print("Gracias pr tu voto")
      elif voto.lower() == "bregman":
         nuevoVoto = 1
         bregman = nuevoVoto + bregman
         print("Gracias pr tu voto")
      else:
         print("Debe elegir un candidato")
         voto = input("Ingrea Milei, Massa, Bullrich, Schiaretti o Bregman: ")
    elif inicio.lower() == "r":
       print("Votos a Milei: " + str(milei))
       print("Votos a Massa: " + str(massa))
       print("Votos a Bullrich: " + str(bullrich))
       print("Votos a Schiaretti: " + str(Schiaretti))
       print("Votos a Bregman: " + str(bregman))
    elif inicio.lower() == "c":
       print(candidatos)
    elif inicio.lower() == "s":
       print("Fue un placer ayudarte. Hasta pronto.")
       system("Cls")
       break
    else:
       print("Seleccione una opción correcta")




