entrada=eval(input())
n=entrada[0]
m=entrada[1]#para a leitura correta da entrada (n,m)
l=[]
def lazyfibonacci(y):
    a, b = 0, 1
    while a <= y:#realiza a sequencia de fibonacci
        yield a
        a, b = b, a+b
for x in lazyfibonacci(n):
    if x > m:#so adiciona na lista numeros até o valor de m
     break
    else:
     l.append(x)
print(l)
