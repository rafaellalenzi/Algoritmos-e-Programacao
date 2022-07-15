class Polinomio:
    def __init__(self, coeficientes=[]):
        self.coe=coeficientes
        
    def __setitem__(self, grau, coeficiente):
        if grau<len(self.coe):
            self.coe[grau]=coeficiente
        else:
            self.coe+=[0]*(grau-len(self.coe))
            self.coe.append(coeficiente)
            
    def __getitem__(self,grau):
        return self.coe[grau]
        
    def grau(self):
        return len(self.coe)-1
        
    def __add__(self,other):
        r=[]
        if len(self.coe)>len(other.coe):
            other.coe+=[0]*(len(self.coe)-len(other.coe))
        elif len(self.coe)<len(other.coe):
            self.coe+=[0]*(len(other.coe)-len(self.coe))
        for i in range(len(self.coe)):
            r.append(self.coe[i]+other.coe[i])
        return Polinomio(r)
    
    def __sub__(self,other):
        r=[]
        if len(self.coe)>len(other.coe):
            other.coe+=[0]*(len(self.coe)-len(other.coe))
        elif len(self.coe)<len(other.coe):
            self.coe+=[0]*(len(other.coe)-len(self.coe))
        for i in range(len(self.coe)):
            r.append(self.coe[i]-other.coe[i])
        return Polinomio(r)
        
    def __mul__(self,other):
        r=[]
        r+=[0]*(len(self.coe)+len(other.coe))
        for i in range(len(self.coe)):
            for j in range(len(other.coe)):
                r[i+j]+=self.coe[i]*other.coe[j]
        return Polinomio(r)
        
    def avalia(self,x):
        r=0
        for i in range(len(self.coe)):
            r+=self.coe[i]*x**i
        return r
            
p = Polinomio ([1,2])
p[3] = 0.5
q = Polinomio ([0,-1,2])

print(p[0],p[1],p[2])

print(p.avalia(0))

print(p.avalia(3),q.avalia(3),(p+q).avalia(3),(p-q).avalia(3),(p*q).avalia(3))

print(((p+q)*(p-q)).avalia(0.5))
