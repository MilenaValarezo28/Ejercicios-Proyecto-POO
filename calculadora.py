from math import pi

class Calculadora:
    def __init__(self, numero1,numero2):
        self.num1= numero1
        self.num2= numero2

    def Suma(self):
        return self.num1 + self.num2
    def Resta(self):
        return self.num1 - self.num2
    def Multiplicacion(self):
        multi= self.num1 * self.num2
        print("{}*{}={}".format(self.num1,self.num2,multi))
    def Division(self):
        return self.num1 / self.num2

class CalEstandar(Calculadora):
    def __init__(self,numero1,numero2):
        super().__init__(numero1,numero2)

    def Multiplicacion(self):
        return self.num1 * self.num2

    def Exponente(self):
        return self.num1 ** self.num2

    def ValorAbsoluto(self,numero):
        if numero < 0:
            numero = numero*-1
            return numero 

class CalCientifica(Calculadora):
    def __init__(self,numero1,numero2):
        super().__init__(numero1,numero2)

    def Circunferencia(self):
        r= 0
        Cir= 2*pi*r
        print("{}*{}*{}={}".format(2,pi,r,Cir))

    def AreaCirculo(self):
        r= 0
        Acirculo= pi*r**2
        print("{}*{}**{}={}".format(pi,r,2,Acirculo))

    def AreaCuadrado(self):
        l1= 0
        Acuadrado= l1**4
        print(Acuadrado(l1))


# cal= Calculadora(4,8)
# cal= Multiplicacion()
calEst = CalEstandar(4,8)
print(calEst.Multiplicacion())
calCient = CalCientifica(2,4)
print(calCient.Circunferencia())
 
