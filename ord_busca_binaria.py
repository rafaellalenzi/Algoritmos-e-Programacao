l = eval(input())

def BuscaBinaria(v,i,j,x):#funcao da busca binaria com modificacoes 
    print(v,i,j,x)
    m = (i+j)//2
    if i > j: 
        if v[i] >= x:
            v.insert(i, x)#insere x uma posicao antes de i
        if len(v) == 1: return v+[[]] #insere espaco vazio
        return v
    if i == j:
        v.insert(i,x)
        if type(v[i+1]) == int:#analizando somente os num
            if v[i]>v[i+1]:#se o anterior for igual ao posterior, inverte as posicoes
                v[i+1], v[i] = v[i], v[i+1]
        return v
    if v[m] <= x: 
        i=m+1
        return BuscaBinaria(v,i,j,x)
    if v[m] > x: 
        j=m-1
        return BuscaBinaria(v,i,j,x)

def Ordenacao(v,l):
    if len(l) <= 1: return l 
    for x in range(len(l)):
        if v[-1] != []:
            v += [[]]
        r = BuscaBinaria(v,0,len(v)-1, l[x])#i=0 j=n-1
    del r[-1]#ao final deleta o espaco vazio criado
    return r

print(Ordenacao([[]],l)) #vetor v: vetor vazio com espaco vazio
