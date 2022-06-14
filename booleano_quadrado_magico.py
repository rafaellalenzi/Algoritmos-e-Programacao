matriz=eval(input())
lista=[]
def somadiagprin(a):#soma da diagonal principal
    soma=0
    for i in range(len(a)):
        while i<len(a)-1:
            for j in range(len(a[i])):
                soma=soma+a[i][j]
                i=i+1
        return soma
def somadiagsec(a):#soma da diagonal secundária
    soma=0
    b=a[::-1]
    for i in range(len(b)):
        while i<len(b)-1:
            for j in range(len(b[i])):
                soma=soma+b[j][i]
                i=i+1
        return soma
def somalinhas(a):#soma de cada linha
    listasomali=[]
    for i in range(len(a)):
        soma=sum(a[i])
        listasomali.append(soma)#cada somatorio eh adicionado a essa lista
    return listasomali
def somacolunas(a):#soma de cada coluna
    listasomacol=[]
    for i in a:
        soma=sum(i)
        listasomacol.append(soma)#cada somatorio eh adicionado a essa lista
    return listasomacol
#comparacao entre as duas listas, que tem a mesma quantidade de valores(matrizes quadradas)
if somalinhas(matriz)==somacolunas(matriz) and somadiagprin(matriz)==somadiagsec(matriz):#comparacao entre o somatorio das diagonais
        print(True) #só retorna True se as duas expressões forem verdadeiras 
else:
    print(False)
