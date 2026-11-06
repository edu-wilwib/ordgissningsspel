import random as rand

ordlista = ["cykelhjul", "mobilmast", "test", "skola", "ö"]
svar = ordlista[rand.randint(0, len(ordlista) - 1)]
print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(svar)} bokstäver.")