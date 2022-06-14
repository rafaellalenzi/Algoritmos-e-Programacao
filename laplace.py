matriz_inserida = eval(input())
def determinante_matriz3(m):
    #uso da regra de sarrus
    return m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1] - m[0][2]*m[1][1]*m[2][0] - m[0][0]*m[1][2]*m[2][1] - m[0][1]*m[1][0]*m[2][2]

def matriz_reduzida(matriz,i):
    b=[row[:i] + row[i+1:] for row in matriz[1:]]
    return b #redução das matrizes feita no teorema de laplace

def determinante_laplace(matriz):#calculo de determinante de matriz nxn
    
    if len(matriz) == 3:
        return determinante_matriz3(matriz) #uma matriz 3x3 permite a aplicação da regra de sarrus

    else:
        a = 0
        for y in range(len(matriz)):#para andar pelas colunas
            a += matriz[0][y]*((-1)**y)*determinante_laplace(matriz_reduzida(matriz,y))#operação com os cofatores, terminando laplace
        return a
    

print (determinante_laplace(matriz_inserida))
