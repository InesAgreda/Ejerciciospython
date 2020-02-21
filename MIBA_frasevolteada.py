#Maria Ines Barron Agreda
class palabra:
    def longi(self):
        txt = input ("Ingresa un texto en esta linea :  ")
        txtt = txt[::-1]

        print ('El texto original es: ' + txt)
        print('El texto al reves es: ' + txtt)

plint = palabra()
plint.longi()
