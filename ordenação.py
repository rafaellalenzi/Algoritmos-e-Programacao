v=eval(input())
def Ordenacao(a):
    min=0#partindo do index 0
    for i in range(len(a)):#percorrendo todos os index do vetor
        if a[i]<a[min]:
            min=i#o index min passa a ser o menor elemento do vetor
    a[0],a[min]=a[min],a[0]#danca das cadeiras
    if len(a)>=2:#se o tamanho de a for menor que 2 não tem por que continuar
        a[1:]=Ordenacao(a[1:])#recurssao 
    return a 
    
print(Ordenacao(v))
