def random(x):
    vet = []
    a = 3
    m = 11
    c = 2
    for i in range(0, 100):
        x = (a*x+c) % m
        u = x/m
        vet.append(u)
    vet.sort()
    return vet


def output(vet, name):
    anterior = vet[0]
    file = open(name+".txt", "w")
    cont = 0
    for elem in vet:
        if anterior == elem:
            cont += 1
        else:
            # formato de impressão:
            # numero   ---->   qtd
            file.write(str(anterior))
            file.write("   ---->   ")
            file.write(str(cont)+'\n')
            cont = 1
            anterior = elem
    file.write(str(anterior))
    file.write("   ---->   ")
    file.write(str(cont)+'\n')
    file.close()


# ************* Main ************* #

seed = int(input())
array = random(seed)
output(array, "teste")

