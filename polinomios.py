class Polinomio:

    def __init__(self, coeficientes=[]):
        self.coeficiente=coeficientes #recebendo os coeficientes como uma lista de inteiros

    def __setitem__(self, grau, coeficiente): #adapta os coeficientes para o grau dado
        if grau<len(self.coeficiente):
            self.coeficiente[grau]=coeficiente
        elif grau>len(self.coeficiente):
            self.coeficiente+=[0]*(grau-len(self.coeficiente))
            self.coeficiente.append(coeficiente)
        else:#se o tamanho da lista de coeficientes for igual ao valor do grau
            self.coeficiente.append(coeficiente)

    def __getitem__(self,grau):
        return self.coeficiente[grau] #a posição corresponde ao grau, posição 3 -> grau 3

    def grau (self):
        return len(self.coeficiente)-1 #retorna o grau do polinômio (-1 por causa do x^0)

    def __mul__(self,p):
        r=[]
        a=[]
        if len(self.coeficiente)>len(p.coeficiente):
            p.coeficiente+=[0]*(len(self.coeficiente)-len(p.coeficiente))
        elif len(self.coeficiente)<len(p.coeficiente):
            self.coeficiente+=[0]*(len(p.coeficiente)-len(self.coeficiente))#faz com que os polinomios tenham o mesmo tamanho
        for i in range(len(self.coeficiente)):
            for j in range(len(p.coeficiente)):
                r.append(self.coeficiente[i]*p.coeficiente[j])
                if len(r) == len(self.coeficiente):
                    a.append(Polinomio(r).avalia(x))
                    r = []
        return Polinomio(a)
        
    def __add__(self,p):
        r=[]
        if len(self.coeficiente)>len(p.coeficiente):
            p.coeficiente+=[0]*(len(self.coeficiente)-len(p.coeficiente))
        elif len(self.coeficiente)<len(p.coeficiente):
            self.coeficiente+=[0]*(len(p.coeficiente)-len(self.coeficiente))#faz com que os polinomios tenham o mesmo tamanho
        for i in range(len(self.coeficiente)):
            r.append(self.coeficiente[i]+p.coeficiente[i])#soma cada index de um com cada index do outro
        return Polinomio(r)

    def __sub__(self,p):
        r=[]
        if len(self.coeficiente)>len(p.coeficiente):
            p.coeficiente+=[0]*(len(self.coeficiente)-len(p.coeficiente))
        elif len(self.coeficiente)<len(p.coeficiente):
            self.coeficiente+=[0]*(len(p.coeficiente)-len(self.coeficiente))#faz com que os polinomios tenham o mesmo tamanho
        for i in range(len(self.coeficiente)):
            r.append(self.coeficiente[i]-p.coeficiente[i])#subtrai cada index de um com cada index do outro
        return Polinomio(r)

    def avalia (self,x):
        r=0
        for i in range(len(self.coeficiente)):
            r+=self.coeficiente[i]*x**i 
        return r
        
p=Polinomio(eval(input()))   
q=Polinomio(eval(input()))
x=eval(input())

print(p.avalia(x),q.avalia(x),(p+q).avalia(x),(p-q).avalia(x),(p*q).avalia(x))
