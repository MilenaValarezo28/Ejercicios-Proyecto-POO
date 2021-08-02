class Basico:
    def numerosN(self,n):
        acu=0
        i=0
        while i <= n:
           # print(i)
            acu += 1
            i += 1
            print(i)
        print("programa finalizado!")
#suma numeros 1 al 100
    # def SumaE(self):
    #     suma= 0
    #     for i in range(1 , 100 + 1):
    #         suma+= i*2
    #         print("La suma de los numeros es: {}".format(suma))

    #3)Comprobar si un numero es multiplo de otro
    def multiplo(self, numero, multiplo):
        if (numero % multiplo)== 0: 
            print("{} es multiplo de {}".format(multiplo, numero))
        else: 
            print("{}  es multiplo de {}".format(multiplo, numero))
        # for i in range(1,13):
        #     res = numero * i
        #     print("{}x{}={}".format(numero, i, res))
        #4)divisor de un numero

    def divisoresNumero(self, numero):
        lista = []
        for i in range(1, numero):
            aux = numero % i
            if aux == 0:
                lista.append(i)
            else:
                pass
        print("Los divisores del numero {} son : ".format(numero))
        print(lista)

#numer primo opcion 5
    def primo(self, numero):
        count = 0
        for i in range(1,numero):
            aux = numero % i
            if aux == 0:
                count += 1
        if count == 2:
            print("El numero {} es primo".format(numero))
            return True
        else:
            print("El numero {} no es primo".format(numero))
            return False

    #8)numero perfecto
    def numeroPerfecto(self, numero):
        suma = 0 
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        if suma == numero:
            print("El numero es perfecto")
        else:
            print("El numero no es perfecto")

class Intermedio(Basico):

#2)	Sumar los números de 1 a n aplicando polimorfismo
    def numeros(self,n):
        acum = 0
        i = 1
        while i <= n:
            acum += i
        print("La suma de los numeros es : {}".format(acum))

    #6)	Factorial de cualquier numero
    def Factorial(self, numero):
        fact = 0
        for i in range(1, numero + 1):
            fact += fact * i
        print("El factorial es: {}".format(fact))

    #7)	Fibonacci de una serie de n números
    def Fibonacci(self, n):
        a=0
        b=1
        if n==0:
            print(a)
        elif n==1:
            print(a, end=' , ')
            print(b)
        else:
            print(a, end=' , ')
            print(b, end=' , ')
            for i in range(n-2):
                c= a+b
                if i == n-3:
                    print(c)
                else:
                    print(c, end=' , ')
                    a=b
                    b=c
       # números primos gemelos entre 2 números
    def PrimosGemelos(self, num1, num2):

        if super().primo(num1) == True:
            pass
        else:
            print("El numero {} no es primo".format(num1))

        if super().primo(num2) == True:
            pass
        else:
            return ("El numero {} no es primo".format(num2))

        if num1 > num2:
            aux = num1 - num2
        else:
            aux = num2 - num1

        if aux == 2:
            return ("Los numeros {} ; {} son primos gemelos".format(num1, num2))
        else:
            return ("Los numeros {} ; {} no son primos gemelos".format(num1, num2))

    #10)numeros amigos
    def amigos(self, num1, num2):
        vectA=  []
        vectB = []
        sumatoriaA= 0
        sumatoriaB= 0
        for i in range(1, num1):
            if num1 % i == 0:
                vectA.append(i)
        for i in range(1, num2):
            if num2 % i == 0:
                vectB.append(i)
        for k in vectA:
            sumatoriaA = sumatoriaA + k
        for k in vectB:
            sumatoriaB = sumatoriaB + k
        if sumatoriaA == num2 and sumatoriaB == num1:
            print("Son amigos")
        else: 
            print("No son amigos")


Object = Basico()  # Creacion de objeto

#Llamada de la funciones con el objeto
Object.numerosN(8)
Object.multiplo(4,2)
Object.divisoresNumero(6)
Object.primo(9)
Object.numeroPerfecto(25)

# Creacion de objecto 2
Obj = Intermedio()
#Llamada de las funciones con el segundo objeto
Obj.numeros(9)
Obj.Factorial(4)
Obj.Fibonacci(9)
Obj.PrimosGemelos(101,200)
Obj.amigos(80,300) 