import random as rand

ordlista = ["cykelhjul", "mobilmast", "test", "skola", "ö"]
svar = list(ordlista[rand.randint(0, len(ordlista) - 1)].split())
print(svar)
print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstäver.")

for i in range(10):
    while True:
        gissning = input("Ange en gissning -> ")
        if len(gissning) < 2:
            input()