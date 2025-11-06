# Escriu un programa que demani l'edat per teclat i ens mostri un missatge que digui "Ets major d'edat" si el valor és igual o major a 18, o bé, "Ets menor d'edat" sí el valor és inferior a 18.
x = int(input("Ficar la teva edat: "))
# Comprova si la persona es major o menor d'edat
if x >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")