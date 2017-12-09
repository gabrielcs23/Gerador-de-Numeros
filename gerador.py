def random(x):
    vet = []
    a = pow(7, 5)
    m = pow(2, 48)
    c = 11
    for i in range(0, 500):
        x = (a*x+c) % m
        u = x/m
        vet.append(round(u, 3))
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
            file.write(str(anterior))
            file.write('\t')
            file.write(str(cont)+'\n')
            cont = 1
            anterior = elem
    file.write(str(anterior))
    file.write('\t')
    file.write(str(cont))
    file.close()


# ************* Main ************* #

seed = int(input("Seed: "))
array = random(seed)
output(array, input("Nome Arquivo: "))

