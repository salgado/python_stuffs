name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hora = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split(" ")
        horas = words[6].split(":")
        chave = horas[0]
        hora[chave] = hora.get(chave, 0) + 1

l_hora = hora.items();
l_hora.sort()
for k, v in l_hora:
    print k, v