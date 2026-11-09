import random as rand

ordlista = ["cykelhjul", "mobilmast", "test", "skola", "ö"]
svar_sträng = ordlista[rand.randint(0, len(ordlista) - 1)]
svar = []
for i in svar_sträng:
    svar.append(i)
svar_synlig = []
for i in range(len(svar)):
    svar_synlig.append("*")
felgissningar = ""
felgissningar_kvar = 10

print(svar)
print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstäver.")

while felgissningar_kvar > 0:
    while True:
        gissning = input("Ange en gissning -> ")
        if len(gissning) == 1:
            if gissning in felgissningar:
                print("Prova något nytt. ", end=" ")
            else:
                break
        else:
            print("Gissningen bör vara ett tecken. ", end="")
    if not gissning in svar:
        felgissningar += gissning
        print(f"Du har nu {felgissningar_kvar} st. felgissningar kvar.")
        felgissningar_kvar -= 1
        print(f"Felgissningar: {felgissningar}")
    print("".join(svar_synlig))