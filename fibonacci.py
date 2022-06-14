n = int(input())
#valores iniciais de a, b para sequência de fibonacci
a, b = 0, 1
#lista vazia para inserir os valores
lista=[]
while a <= n: #loop que possibilita que o teto seja o num do input
    lista.append(a) #adição de cada novo valor a lista
    a, b = b, a+b #execução da sequência
    
print(lista)
print(sum(lista)) #soma dos valores da lista
