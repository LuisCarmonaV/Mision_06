#LuisAdrian Carmona Villalobos
#Progama que hace espirografos



import pygame
import  math


C1 = (100, 204, 88)
C2 = (120, 120, 120)
C3 = (0, 0, 255)
C4 = (255, 0, 255)
C5= (0, 0, 0)

ANCHO = 800
ALTO = 800


# Funcion para dibujar
def dibujar(r, Radio, l):

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(C5)

        for ang in range(0, 361 * (r//math.gcd(r, Radio)), 1):
            k = r / Radio
            x = int(Radio * ((1.4 - k) * math.cos(ang) + l * k * math.cos(((1.5- k) / k) * ang)))
            y = int(Radio * ((1.1 - k) * math.sin(ang) - l * k * math.sin(((1.5 - k) / k) * ang)))



            pygame.draw.circle(ventana, C4, (x * 2 + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, C1, (x * 2 + ANCHO // 2, ALTO // 2 - 2 * y), 1)
            pygame.draw.circle(ventana, C3, (x + ANCHO // 2, ALTO // 2 + y), 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def main():
    r = 23
    Radio = 60
    l = 2
    dibujar(r, Radio, l)



main()