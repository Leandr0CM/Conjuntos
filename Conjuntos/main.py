arquivo = open("D:\Tarefas\Conjuntos\caso1.txt", "r") #digite o endereço do arquivo
n = int(arquivo.readline())


def leitura():
    conjunto = []
    pequeno = True
    texto = arquivo.readline().strip()

    i2 = -1

    for i in range(0, len(texto)):
        if pequeno:
            conjunto.append(texto[i])
            i2 += 1
        if i < len(texto)-1 and texto[i] not in (',', ' ') and texto[i + 1] not in (',', ' '):
            conjunto[i2] += texto[i + 1]
            pequeno = False
            i += 1
        if texto[i] == ',':
            pequeno = True
    conjunto = list(filter(lambda item: item not in (',', ' '), conjunto))
    return conjunto


def uniao(c1, c2):
    resu = c1
    for i in range(0, len(c2)):
        verifica = c2[i] in resu
        if not verifica:
            resu.append(c2[i])
    return resu


def intersec(c1, c2):
    resu = []
    for i in range(0, len(c1)):
        if c1[i] in c2:
            resu.append(c1[i])
    return resu


def diferenca(c1,c2):
    resu = c1
    for i in range(0, len(c2) ):
        if c2[i] in c1:
            resu.remove(c2[i])
    return resu


def produto(c1, c2):
    resu = []
    for i in range(len(c1)):
        for e in range(len(c2)):
            resu.append((c1[i], c2[e]))
    return resu


for i in range(0, n):
    operacao = arquivo.readline().strip()
    conjunto1 = leitura()
    conjunto2 = leitura()

    print("(", i+1, ")")
    print(operacao)
    print("A:", conjunto1)
    print("B:", conjunto2)

    if operacao == "U":
        resultado = uniao(conjunto1, conjunto2)
        print("resultado =", resultado, "\n")

    if operacao == "I":
        resultado = intersec(conjunto1, conjunto2)
        print("resultado =", resultado, "\n")

    if operacao == "D":
        resultado = diferenca(conjunto1, conjunto2)
        print("resultado =", resultado, "\n")

    if operacao == "C":
        resultado = produto(conjunto1, conjunto2)
        print("resultado =", resultado, "\n")

arquivo.close()
