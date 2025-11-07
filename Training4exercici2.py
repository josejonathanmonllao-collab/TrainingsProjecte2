#Escriu un programa que llegeixi una seqüència de notes (valors de 0 a 10) i finalitzarà la seqüència amb el valor -1. Quan finalitzi ens ha d'indicar si "Hi ha hagut alguna nota que té un 10" o "No hi ha cap 10".: ")
nota = float(input("Introdueix una nota (de 0 a 10) o -1 per finalitzar: "))
num10 = False
while True:
    nota = float(input("Introdueix una nota (de 0 a 10) o -1 per finalitzar: "))
    if nota == -1:
        break
    if nota == 10:
        num10 = True
if num10:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")