meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO


istoric_comenzi = []
contor_comenzi = []
while studenti and comenzi:
    student = studenti.pop()
    comanda = comenzi.pop()
    if student and comanda:
        print(f'{student} a comandat {comanda}.')
        tavi.pop()
        istoric_comenzi.append((student, comanda))
        contor_comenzi.append(comanda)
print(istoric_comenzi)
meniu.remove(comanda)
print(meniu)
print(f""" 
S-au comandat {comanda.count('papanasi')} papanasi.
S-au comandat {comanda.count('guias')} guiasuri.
S-au comandat {comanda.count('ceafa')} cefe.
          """)
print(f'Mai exista {len(tavi)} tavi disponibile.')
if 'papanasi' in meniu:
    print("Mai sunt papanasi disponibili.")
else:
    print("Nu mai sunt papanasi disponibili.")

if 'ceafa' in meniu:
    print("Mai este ceafa disponibilă.")
else:
    print("Nu mai este ceafa disponibilă.")

if 'guias' in meniu:
    print("Mai este guias disponibil.")
else:
    print("Nu mai este guias disponibil.")
pret = 0
for x in contor_comenzi:
    if x == 'papanasi':
        pret += 7
    elif x == 'ceafa':
        pret += 10
    elif x == 'guias':
        pret += 5
print(f"Cantina a incasa {pret} de lei. ")
produse_7lei = []
for i in preturi:
    nume_produs = i[0]
    pret = i[1]
    if pret <= 7:
        produse_7lei.append((nume_produs, pret))
print(f'Produsele sub 7 lei sunt: {produse_7lei}')


