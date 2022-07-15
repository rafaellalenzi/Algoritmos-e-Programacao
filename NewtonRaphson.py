class NewtonRaphson:
    def __init__(self, coeficientes=[]):
        self.coe=coeficientes
        
    def derivada(self):
        self.deriv=[]
        for i in range(len(self.coe)):
            self.deriv.append(self.coe[i]*i)
        del self.deriv[0]
        return NewtonRaphson(self.deriv)
        
    def avalia(self,x):
        r=0
        for i in range(len(self.coe)):
            r+=self.coe[i]*x**i
        return r

p=NewtonRaphson([3,2])
x0=2
n=1
x=[x0]+[0]*n
try:
    for i in range(1,n+1):
        x[i]=x[i-1]-(p.avalia(x[i-1])/p.derivada().avalia(x[i-1]))
        print(("%.2f"%p.avalia(x[n]),"%.2f"%x[n]))
except ZeroDivisionError:
    print("Abortado")
    
