import random as rand
import json #importerar ett bibliotek för att kunna läsa ordlistan

with open("ordlista.jsonl", "r", encoding="utf-8") as file: #öppnar textfilen på rätt sätt
    ordlista = [line.strip().upper() for line in file] #lägger till alla ord från textfilen i en pythonlista

möjliga_bokstäver = [] #lista över alla tecken i ordlistan
for k in ordlista: #loopen lägger till alla tecken från ordlistan i listan möjliga_bokstäver
    for l in k:
        if not l.upper() in möjliga_bokstäver: #gör att varje tecken bara läggs till en gång
            möjliga_bokstäver.append(l.upper()) #gör bokstäverna stora och lägger till i möjliga_bokstäver

while True: #spelloop
    svar_sträng = ordlista[rand.randint(0, len(ordlista) - 1)].upper() #slumpar fram ett svar ur ordlistan
    svar = []
    for i in svar_sträng: #lägger till alla tecken från svaret i listan svar
        svar.append(i)
    svar_synlig = [] #skapar en lista för de bokstäver som man har gissat rätt på
    for i in range(len(svar)): #lägger till asterisker för alla bokstäver man inte ännu gissat rätt på
        svar_synlig.append("*")
    felgissningar = "" #den sträng som ska skrivas ut efter varje försök för att visa vilka tecken som är fel
    felgissningar_kvar = 10
    
    if len(svar) == 1: #skriver bokstav/bokstäver beroende på hur många tecken svaret är
        print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstav.") #skriver ut instruktioner
    else: 
        print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstäver.")

    while felgissningar_kvar > 0: #loopen kör så länge man har försök kvar
        while True: #säker inmatning
            gissning = input("\nAnge en gissning -> ").upper() #gissningen med stora bokstäver
            if len(gissning) == 1: #kollar att gissningen bara är ett tecken
                if gissning in felgissningar or gissning in svar_synlig: #om man försöker gissa samma sak två gånger
                    print("Prova något nytt. ", end=" ")
                elif not gissning in möjliga_bokstäver: #om tecknet inte förekommer i ordlistan
                    print("Tecknet finns inte i något ord i svenska ordboken. ", end=" ")
                else: #om allt stämmer lämnar programmet inmatningsloopen
                    break
            else:
                print("Gissningen bör vara ett tecken. ", end="")
        if not gissning in svar: #om gissningen är fel
            felgissningar += gissning #lägg till den i strängen felgissningar
            felgissningar_kvar -= 1 #minska antal försök kvar med 1
        else: #om gissningen är rätt
            j = 0 #räknevariabel för att kolla platsen i svar_synlig
            for i in svar: #för varje tecken i svar
                if i == gissning: #om gissningen finns i svar
                    svar_synlig[j] = gissning #byt ut asterisken mot gissningen (som är rätt)
                j += 1
            if svar == svar_synlig: #om man har hittat alla tecken i svaret
                break #lämnar felgissningsloopen
        print(f"Du har nu {felgissningar_kvar} st. felgissningar kvar.") #skriver antal felgissningar kvar
        print(f"Felgissningar: {felgissningar}") #skriver vilka felgissningar man har gissat tidigare
        print("".join(svar_synlig)) #skriver svaret med de bokstäver man har hittat

    if svar == svar_synlig: #om man har hittat hela svaret
        print(f"{''.join(svar)}\n") #skriver svaret
        print("Du överlevde!")
    else: #om man fick slut på försök
        print("\nDu förlorade :-(")
        print(f"Ordet var {''.join(svar)}") #skriver svaret
    while True: #säker inmatning på om man vill spela igen (rad 62-71)
        igen = input("Vill du spela igen? (j/n) ").lower()
        if igen == "j":
            igen = True
            break
        elif igen == "n":
            igen = False
            break
        else:
            continue
    if not igen: #lämnar spelloopen om spelaren inte vill fortsätta
        break
print("Programmet avslutades normalt.")
