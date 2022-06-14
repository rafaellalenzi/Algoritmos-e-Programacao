v=eval(input())
x=int(input())
i=0
j=len(v)-1 
def BuscaBinaria(i,j): #argumentos i,j pq eles que variam na busca 
    if i>j: return -1 
    m=(i+j)//2
    if v[m]<x: 
        i=m+1
        return BuscaBinaria(i,j)
    if v[m]>x: 
        j=m-1
        return BuscaBinaria(i,j)
    if v[m]==x:
        return m
print(BuscaBinaria(i,j))
