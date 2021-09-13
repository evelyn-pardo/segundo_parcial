class Calculadora:
    def init(self,numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
        
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        pass
    
    def multiplicacion(self):
        multi = self.num1*self.num2
        print("{}*{}={}".format(self.num1,self.num2,multi))
    
    def división(self):
        pass
cal = Calculadora(2,4)
s = cal.suma() 
print(s)