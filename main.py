import random as rand
import json

with open("ordlista.jsonl", "r", encoding="utf-8") as file:
    ordlista = [line.strip().upper() for line in file]
möjliga_bokstäver = []
for k in ordlista:
    for l in k:
        if not l.upper() in möjliga_bokstäver:
            möjliga_bokstäver.append(l.upper())

while True:
    svar_sträng = ordlista[rand.randint(0, len(ordlista) - 1)].upper()
    svar = []
    for i in svar_sträng:
        svar.append(i)
    svar_synlig = []
    for i in range(len(svar)):
        svar_synlig.append("*")
    felgissningar = ""
    felgissningar_kvar = 10

    if len(svar) == 1:
        print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstav.")
    else:
        print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstäver.")

    while felgissningar_kvar > 0:
        while True:
            gissning = input("\nAnge en gissning -> ").upper()
            if len(gissning) == 1:
                if gissning in felgissningar or gissning in svar_synlig:
                    print("Prova något nytt. ", end=" ")
                elif not gissning in möjliga_bokstäver:
                    print("Tecknet finns inte i något ord i svenska ordboken. ", end=" ")
                else:
                    break
            else:
                print("Gissningen bör vara ett tecken. ", end="")
        if not gissning in svar:
            felgissningar += gissning
            felgissningar_kvar -= 1
        else:
            j = 0
            for i in svar:
                if i == gissning:
                    svar_synlig[j] = gissning
                j += 1
            if svar == svar_synlig:
                break
        print(f"Du har nu {felgissningar_kvar} st. felgissningar kvar.")
        print(f"Felgissningar: {felgissningar}")
        print("".join(svar_synlig))

    if svar == svar_synlig:
        print(f"{''.join(svar)}\n")
        print("Du överlevde!")
    else:
        print("\nDu förlorade :-(")
        print(f"Ordet var {''.join(svar)}")
    if not input("Vill du spela igen? (j/n) ") == "j":
        break
print("Programmet avslutades normalt.")