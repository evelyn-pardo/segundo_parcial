class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo 
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opcion=input("Elija opcion[1...{}]:".format(len(self.opciones)))

menu1=Menu("Menu Principal",["1) Calculadora","2)Numeros","3)Lista","4)Calculos","5)Salir"])
menu1.menu()

if opcion == "1":
        print("Calculadora")                   
elif opc == "2":
        print("Operaciones con Numeros")
        print("1) perfecto")
        print("2)Primo ")
        print("3)Salir ")
        opc2=input("Elija opcion[1...3]: ")
        if opc2 == "1":
            print("Nuevos Perfectos")
            num= int(input("Ingrese Numero:"))
            #llamar el metodo percfecto 
            print("El numero es pefecto")
elif opc == "3":
        print("Listas")
        
elif opc == "4":
        print("Cadena")
    
elif opc == "5":
        print("Salir")
else:
        print("Opcion no valida")      