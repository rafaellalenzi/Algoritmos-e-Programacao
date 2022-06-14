x=eval(input())
n,a,b,c=x[0],x[1],x[2],x[3]
i=1
def seriematematica(i,r):
    r+=((-1)**(c+i))*((1+a*i))/((3*(b**i)))#formula da serie mat
    if i<n: return seriematematica(i+1,r)
    if i==n: return r #somatório de i até n
print(float('%.3f'%seriematematica(i,0)))#para imprimir 3 casas decimais
