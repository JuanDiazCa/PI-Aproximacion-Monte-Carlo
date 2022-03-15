import pygame
import random
import math

class MetodoMonteCarlo:
    def __init__(self, ancho, alto, color, colorPuntos):
        self.pantalla = pygame.display.set_mode((ancho,alto))
        pygame.time.Clock().tick(1)
        self.ancho = ancho
        self.color = color
        self.colorFuente = (255-color[0], 255-color[1], 255-color[2])
        self.colorPuntos = colorPuntos
        self.colorFuera = (255-colorPuntos[0], 255-colorPuntos[1], 255-colorPuntos[2])
        self.puntos = []
        self.PI = 0.0
        self.rect = pygame.Rect(0, 0, self.ancho, alto)
        
    def dibujar(self):
        pygame.draw.rect(self.pantalla, self.color, self.rect)
        self.dibujarPuntos()
        self.dibujarInfo()

    def dibujarPuntos(self):
        for i in range(len(self.puntos)):
            pos = (self.puntos[i][0], self.puntos[i][1])
            if self.getDistanciaCentro(pos) <= self.ancho/2:
                pygame.draw.circle(self.pantalla, self.colorPuntos, pos, 2)
            else:
                pygame.draw.circle(self.pantalla, self.colorFuera, pos, 2)

    def dibujarInfo(self):
        fuente = pygame.font.match_font('consolas')
        tipo_letra = pygame.font.Font(fuente,15)
        texto = tipo_letra.render("Puntos: " + str(len(self.puntos)), True, self.colorFuente)
        rect = texto.get_rect()
        rect.center = (int(self.ancho/2), int(self.ancho + 20))
        self.pantalla.blit(texto, rect)
        texto = tipo_letra.render("Aproximacion a PI: " + "{:.15f}".format(self.PI), True, self.colorFuente)
        rect = texto.get_rect()
        rect.center = (int(self.ancho/2), int(self.ancho + 40))
        self.pantalla.blit(texto, rect)

    def getDistanciaCentro(self, pos):
        return math.sqrt((pos[0] - self.ancho/2)**2 + (pos[1] - self.ancho/2)**2)
        
    def generarPunto(self):
        x = random.randint(0, self.ancho)
        y = random.randint(0, self.ancho)
        return (x, y)

    def calcularPI(self):
        self.PI = 0.0
        for i in range(len(self.puntos)):
            if self.getDistanciaCentro(self.puntos[i]) <= self.ancho/2:
                self.PI += 1.0
        self.PI = self.PI / len(self.puntos)
        self.PI = self.PI * 4.0

    def calcular(self):
        self.puntos.append(self.generarPunto())
        self.calcularPI()
        self.dibujar()

    def loop(self):
        pygame.init()
        pygame.display.set_caption("Calculo de PI por metodo Monte Carlo")
        while True:
            self.calcular()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.image.save(self.pantalla, "pantallazos/"+"p"+str(len(self.puntos))+"pi"+str(int(self.PI*10000))+".png")
            pygame.display.update()