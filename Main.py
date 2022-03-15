import MetodoMonteCarlo as mc

ancho = 500
alto = ancho + 60
color = (0, 0, 0)
colorPuntos = (211, 65, 18)

if __name__ == '__main__':
    mc.MetodoMonteCarlo(ancho, alto, color, colorPuntos).loop()