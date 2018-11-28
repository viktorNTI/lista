import random

val = 0
meddelande = " "
ytterligarelistatest = [" ", " "]

while val !=5:
    try:
        val = int(input("(1) Skriv ut (2) Mata in (3) Rensa (4) Avsluta"))
    except: 
        print("Vänligen tryck (1), (2), (3) eller (4)")
    if val == 1: 
        f = open('log.txt', 'r')
        for line in f:
            print(line)
        f.close()

    elif val == 2:
        f = open('log.txt', 'a+')
        meddelande = (input("Lägg till i listan"))
        f.write(meddelande)
        f.close()
    
    elif val == 3: 

