class Lista: 
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
        
    def append(self,dato): 
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            return True
        else:
            return False
            
    def obtener (self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]   
        
    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            
            listaAux = []
            for ind in range (pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]]
            self.longitud -=1
            self.lista = listaAux
            return [self.lista,eliminado]
    
    #busca un dato en la lista y retorna la posicion de ese valor en la lista
    def buscar(self,valor):
        pass
    
    #busca un dato con el metodo buscar y si no lo encuentra lo inserta en la lista   
    def insertar(self,dato):
        pass
    
    #busca el dato con el metodo buscar y si lo encuentra lo elimina de la lista
    def eliminar(self,dato):
        pass       
    
          
    def mostrar(self):  
        print("{:2}{:9} {}".format("","lista","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:3}".format(ele,pos))
                              
lista1 = Lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
lista1.mostrar()
posicion = int(input("Ingrese posicion para obtener el elemento "))
resp = lista1.obtenerEliminado(posicion)
if resp == None:
    print("Posicion no valida, verifique la lista...!!!")
else:
    print("El elemento de la posicion:{} es:{}".format(posicion,resp))