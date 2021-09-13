class Cola: 
    def __init__(self):
        self.cola = []
        self.top = 0
        
    def insertar(self,dato):
        self.items.append(dato)
        return dato
    
    def vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False
        
    def eliminar(self):
        if self.vacia():
            return None
        else:
            return self.items.pop(0)
        
    def mostrar(self):
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.items[top]))

cola1 = Cola()
cola1.insertar('Hector','Juan','Miguel')
cola1.insertar('Andrea')
cola1.insertar(True)
cola1.mostrar()
posicion = int(input("Ingrese posicion para obtener el elemento "))
resp = cola1.mostrar()
if resp == None:
    print("Posicion no valida, verifique la cola...!!!")
else:
    print("El elemento de la posicion:{} es:{}".format(posicion,resp))     
