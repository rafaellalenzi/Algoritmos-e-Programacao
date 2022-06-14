num=eval(input())
def divisores(r):
    div=set([])#cria set vazio para add os divisores 
    for n in range(1,r+1):
        if r%n==0:#so eh divisor se o resto for 0
            div.add(n)#add n para o set 
    return div

def divisorescomuns(a):
    divis=divisores(a[0])#o primeiro sete eh ref para os outros
    for i in range(len(a)):
        divis=divis.intersection(divisores(a[i]))#interseccao 
    return divis

print(divisorescomuns(num))
