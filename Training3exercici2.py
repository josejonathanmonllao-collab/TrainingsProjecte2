#Escriu un programa que llegeixi tres nombres diferents i ens digui quin és el major
num1 = int(input("Ficar el primer numero: "))
num2 = int(input("Ficar el segon numero: "))
num3 = int(input("Ficar el tercer numero: "))
#Comprova quin numero es el més gran
if num1 > num2 and num1 > num3:
    print("El primer numero és el major.")
elif num2 > num1 and num2 > num3:
    print("El segon numero és el major.")
else:
    print("El tercer numero és el major.")
