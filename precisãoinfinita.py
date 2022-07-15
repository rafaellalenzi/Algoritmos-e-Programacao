class NumeroDecimal:
    
    def __init__(self, valor = None, expoente = None, v = ""):
        
        if v != "":
            if "." in v:
                self.virgula = v.index(".")
                self.valor = v.replace(".", "")
                self.expoente = len(self.valor) - self.virgula
                self.valor = int(self.valor)
            else:
                self.valor = eval(v)
                self.expoente = 0
        elif (valor != None) and (expoente != None):
            self.expoente = expoente
            self.valor = valor
    
    def __add__(self,other):
        
        if self.expoente == other.expoente:
            re = self.valor + other.valor
        elif self.expoente > other.expoente:
            zeros = self.expoente - other.expoente
            novabase = eval(str(other.valor)+"0"*zeros)
            r = self.valor + novabase
        else:
            zeros = other.expoente - self.expoente
            novabase = eval(str(self.valor)+"0"*zeros)
            r = other.valor + novabase
            
        return NumeroDecimal(r, max(self.expoente, other.expoente))
        
    def __sub__(self,other):
        
        if self.expoente == other.expoente:
            r = self.valor - other.valor
        elif self.expoente > other.expoente:
            zeros = self.expoente - other.expoente
            novabase = eval(str(other.valor)+"0"*zeros)
            r = self.valor - novabase
        else:
            zeros = other.expoente - self.expoente
            novabase = eval(str(self.valor)+"0"*zeros)
            r = other.valor - novabase
            
        return NumeroDecimal(r, max(self.expoente, other.expoente))
        
    def __repr__(self):
        
        valorstr = str(self.valor)
        valorstr = valorstr[:len(valorstr)-self.expoente] + "," + valorstr[len(valorstr)-self.expoente:]
        return(valorstr)

entrada=input()
if "+" in entrada:#soma
    entrada.index("+")
    elem = entrada.split("+")
    a = elem[0]
    b = elem[1]
    a = NumeroDecimal(v = a)
    b = NumeroDecimal(v = b)
    print(a+b)

elif "-" in entrada:#subtração
    entrada.index("-")
    elem = entrada.split("-")
    a = elem[0]
    b = elem[1]
    a = NumeroDecimal(v = a)
    b = NumeroDecimal(v = b)
    print(a-b)
