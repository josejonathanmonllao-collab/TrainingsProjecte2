#Escriu un programa que llegeixi 10 nombres, quan acabi ha d'indicar si "hi havia almenys un nombre negatiu" o "no hi ha cap nombre negatiu".
numero_negatiu = False
for i in range(10):
    nombre = float(input("Fica un numero: "))
    if nombre < 0:
        numero_negatiu = True
if numero_negatiu:
    print("Hi havia almenys un numero negatiu")
else:
    print("No hi ha cap numero negatiu")   