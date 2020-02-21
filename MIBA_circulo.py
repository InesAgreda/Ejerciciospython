#Maria Ines Barron Agreda
class areacirculo:
  def circulo(self):
    print ("Calcula el area del circulo")
    radio=input("Dame radio del circulo: ")
    pi=3.1416
    area=float (pi) * int (radio) ** 2.0
    print("El área es: " + str (area))

area = areacirculo()
area.circulo()
