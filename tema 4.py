# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
from itertools import count

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []
print("Bine ai venit!")
print(progres)

while progres.count("_") > 0 and incercari_ramase > 0:
    litera = input("Alege o litera:")
    if not (len(litera) == 1 and litera.isalpha()):
        print("Alege doar o LITERA!!")
        continue
    elif litera in litere_incercate:
        print('Ai folosit deja aceasta litera, pune o litera noua!')
        continue
    if litera in cuvant_de_ghicit:
        for i, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[i] = litera
        litere_incercate.append(litera)

        print(f"""
Bravo!Ai ghicit o litera
literele ramase:{progres}
"""  )
        if "_" not in progres:
            print(f"Bravo ai ghicit cuvantul!")
            break
    else:
        incercari_ramase -= 1
        litere_incercate.append(litera)
        print(f"Nu ai ghicit, mai ai {incercari_ramase} incercari")

else:
    print(f"""

Imi pare rau! Nu mai ai incercari
Cuvantul era:{cuvant_de_ghicit}
""")





