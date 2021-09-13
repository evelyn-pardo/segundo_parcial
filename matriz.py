import os
class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz
        self.fila=fila
        self.col = col
            
    def ingresar(self):
        self.matriz = []
        for fila in range(self.fila):
            columnas=[]
            os.system("cls")
            for col in range(self.col):
                valor = input("Fila[{}] columna[{}]: ".format(fila,col))
                columnas.append(valor)
            self.matriz.append(columnas)
    
    def presentar(self):
        #os.system("cls")
        print("_______")
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col],end=" ")
            print()
        print("_______")
    
    def buscar(self,valor):
        enc = {}
        for fila in range(len(self.matriz)):
            for col in range (len(self.matriz[fila])):
                if self.matriz[fila][col] == (valor):
                    enc["fila"]= fila
                    enc["col"]= col
                    break
            if enc: breack
        return enc
        
    def buscarM(self,valor):
        enc = {}
        fila =0 
        band=True
        while fila < len(self.matriz) and band:
            col=0
            while col < len(self.matriz[fila]) and band:
                if self.matriz[fila][col] == valor:
                    enc["fila"]= fila
                    enc["columna"]= col
                    band=False
                else: col += 1
            fila += 1
        return enc
        
    def sumar(self,matriz2):
        matrizSuma = []
        for fila in range(self.fila):
            columnas=[]
            for col in range(self.col):
                valor = self.matriz[fila][col]+matriz2[fila][col]
                columnas.append(valor)
            matrizSuma.append(columnas)
        return matrizSuma


#numeros = [[10,20,30,23],[60,80,90],[25,35,55]]
numeros = []
#fila         0              1        2
#col = numero[0]
#print(numero[0],numero[0][1])
#print(col,col[1])
#mat = Matriz(numeros,3,3)
mat1 = Matriz([],2,2)
mat2 = Matriz(numeros,2,2)
mat1.ingresar()
mat2.ingresar()
mat1.presentar()
mat2.presentar()
mat1.sumar(mat2.matriz)
mat1.presentar()
#mat.ingresar()
#print(mat.buscar(8))
#mat.presentar()
#print(mat.buscar(55))
# resp = mat.buscarM(300)    
# if resp: print("El valor se encuentra en la siguiente coordenadas",resp) 
# else: print("no existe el valor en la matrizz")