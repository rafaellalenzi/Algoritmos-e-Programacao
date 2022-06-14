class Matriz:    
    def __init__(self,n,m,v):
        self.n = n  
        self.m = m  
        self.v = [] 
        for i in range(n): #organiza a lista recebida em uma matriz nxm
            self.v.append([])
        for i in range(n):
            for x in v[i*m:]:
                self.v[i].append(x)
                if len(self.v[i])>=m:break
    def __add__(self,other):#operação de adição 
        r=[]
        for i in range(self.n):
            j=[a+b for a,b in zip(self.v[i],other.v[i])]
            r.append(j)
        return r
    def __sub__(self,other):#operação de subtração
        r=[]
        for i in range(self.n):
            j=[a-b for a,b in zip(self.v[i],other.v[i])]
            r.append(j)
        return r
    def __mul__(self,other):#operação de multiplicação conforme as regras de mult de matrizes
        r=[]
        for i in range(len(self.v)):
            multiplicação=[]
            for j in range(len(other.v[0])):
                mult=0
                for k in range(len(self.v[0])):
                    mult+=self.v[i][k]*other.v[k][j]
                multiplicação.append(mult)
            r.append(multiplicação)
        return r
    def __repr__(self):
        return list(self.v)
z = input() 
for i in range(len(z)):#funciona como um organizador de input 
    if z[i] == "+" or z[i] == "-" or z[i] == "*":
        a = "Matriz"+z[:i]#maneira de convocar a classe 
        b = "Matriz"+z[i+1:]
        r = a+z[i]+b
        break
print(eval(r))#eval para permitir que o operador seja reconhecido como tal e não como str
