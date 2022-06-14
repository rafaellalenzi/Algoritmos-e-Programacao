n1=int(input())
n2=int(input())
def divisão(a,b):
    if a>=b:
        return divisão(a-b,b)+1#divisão é uma subtração repetidas vezes
    else:#se a<b, uma divisão inteira da 0
        return 0 
print(divisão(n1,n2))
