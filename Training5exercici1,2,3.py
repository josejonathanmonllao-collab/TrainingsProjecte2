def T1ex1():
    print("Hola, Mon")
def T2ex1():
    # Demanar la mida del lateral
        costat = float(input("Introdueix la mida del costat del quadrat: "))

    # Calcular l'àrea
        area = costat * costat

    # Aquí tenim el resultat
        print("L'àrea del quadrat és:", area)
def T2ex2():
    num1 = int(input("Introdueix el primer nombre: "))
    num2 = int(input("Introdueix el segon nombre: "))

    # Calculem les operacions
    suma = num1 + num2
    resta = num1 - num2
    multiplicacio = num1 * num2
    divisio = num1 / num2
    # Mostra els resultats
    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicació:", multiplicacio)
    print("Divisió:", divisio)
def T2ex3():
    # Demanem tres paraules
    paraula1 = input("Escriu la primera paraula: ")
    paraula2 = input("Escriu la segona paraula: ")
    paraula3 = input("Escriu la tercera paraula: ")

    # Creem una frase
    frase = paraula1 + " " + paraula2 + " " + paraula3

    # Frase final
    print("La frase és:", frase)
def T2ex4():
     # Demanem que els dos nombres siguin amb decimals
    x = float(input("Introdueix el primer nombre amb decimals: "))
    y = float(input("Introdueix el segon nombre amb decimals: "))

    # Convertim a enters
    numero1 = int(x)
    numero2 = int(y)

    # Mostrem el resultat
    print("El primer nombre com a enter és:", numero1)
    print("El segon nombre com a enter és:", numero2)
def T3ex1():
     # Escriu un programa que demani l'edat per teclat i ens mostri un missatge que digui "Ets major d'edat" si el valor és igual o major a 18, o bé, "Ets menor d'edat" sí el valor és inferior a 18.
    x = int(input("Ficar la teva edat: "))
    # Comprova si la persona es major o menor d'edat
    if x >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")
def T3ex2():
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
def T3ex3():
    #Escriu un programa que llegeixi per teclat un nombre i ens digui si és positiu o negatiu (considerem el zero com a positiu).
    x = int(input("Ficar un numero: "))
    #Comprova si el nombre es positiu o negatiu
    if x >= 0:
        print("El numero es positiu.")
    else:
        print("El numero es negatiu.")
def T4ex1():
    #Realitza un programa que mostri tots els nombres parells que hi ha entre 1 i 200.
    numero = 0
    while numero <= 200:
        # Mostrara tots els numeros parells entre 1 i 200
        print(numero)
        numero += 2
def T4ex2():
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
def T4ex3():
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
while True:
    print("\nTots els exercicis disponibles de Python: ")
    print("1. T1ex1 - Hola, Mon")
    print("2.1. T2ex1 - Àrea del quadrat")
    print("2.2. T2ex2 - Operacions bàsiques")
    print("2.3. T2ex3 - Crear una frase")
    print("2.4. T2ex4 - Convertir decimals a enters")
    print("3.1. T3ex1 - Major o menor d'edat")
    print("3.2. T3ex2 - Trobar el nombre major")
    print("3.3. T3ex3 - Positiu o negatiu")
    print("4.1. T4ex1 - Nombres parells entre 1 i 200")
    print("4.2. T4ex2 - Notes amb 10")
    print("4.3. T4ex3 - Nombres negatius")   
    exercicis = input("Introdueix el número de l'exercici que vols executar (1-4.3) o 'sortir' per acabar: ")
    match exercicis:
        case '1':
            T1ex1()
        case '2.1':
            T2ex1() 
        case '2.2':
            T2ex2()
        case '2.3':
            T2ex3()
        case '2.4':   
            T2ex4()
        case '3.1':
            T3ex1()
        case '3.2':
            T3ex2()
        case '3.3':
            T3ex3()
        case '4.1':
            T4ex1()
        case '4.2':
            T4ex2()
        case '4.3':
            T4ex3() 
        case 's':
            print("Adeu!")
            break  
        case _:
            print("Error.")