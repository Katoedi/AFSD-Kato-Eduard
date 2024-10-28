meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO


istoric_comenzi = []
contor_comenzi = [0, 0, 0]
while studenti and comenzi:
    student = studenti.pop()
    comanda = comenzi.pop()
    if student and comanda:
        print(f'{student} a comandat {comanda}.')
        tavi.pop()
        istoric_comenzi.append(comanda)

        #contor_comenzi.append
print(istoric_comenzi)
meniu = meniu.remove(istoric_comenzi)
print(meniu)

