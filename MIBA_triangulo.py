#Maria Ines Barron Agreda
class areatriangulo:
    def triangulo(self):
        print ("Calcular area del triangulo")
        b=input("Dame la base del triangulo: ")
        a=input("Dame la altura del triangulo: ")
        area=int (b) * int (a) / 2.0
        print ("El área es: " + str (area))
        
calcular = areatriangulo()
calcular.triangulo()  
