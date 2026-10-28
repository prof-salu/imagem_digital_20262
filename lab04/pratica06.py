import math
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_grade_chao():
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_LINES)
    for i in range(-10, 11):
        glVertex3f(i, -1.0, -10); glVertex3f(i, -1.0, 10)
        glVertex3f(-10, -1.0, i); glVertex3f(10, -1.0, i)
    glEnd()

def desenhar_monolito():
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.7, 1.0) # Frente
    glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1); glVertex3f(1, 2, 1); glVertex3f(-1, 2, 1)
    glColor3f(1.0, 0.5, 0.2) # Trás
    glVertex3f(-1, -1, -1); glVertex3f(-1, 2, -1); glVertex3f(1, 2, -1); glVertex3f(1, -1, -1)
    glColor3f(0.2, 1.0, 0.4) # Direita
    glVertex3f(1, -1, -1); glVertex3f(1, 2, -1); glVertex3f(1, 2, 1); glVertex3f(1, -1, 1)
    glColor3f(0.9, 0.9, 0.2) # Esquerda
    glVertex3f(-1, -1, -1); glVertex3f(-1, -1, 1); glVertex3f(-1, 2, 1); glVertex3f(-1, 2, -1)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Pratica 6: gluLookAt (Setas=Azimuth/Elevation | W/S=Dolly | Q/E=Roll)")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    # Parâmetros esféricos da Câmera ao redor do Ponto Focal (0, 0, 0)
    azimuth = 0.0      # Giro horizontal ao redor do foco
    elevation = 0.3    # Elevação vertical
    distancia = 8.0    # Dolly (distância até o ponto focal)
    roll = 0.0         # Giro do vetor View Up

    print("Controles: Setas Esq/Dir (Azimuth) | Setas Cima/Baixo (Elevation) | W/S (Dolly) | Q/E (Roll)")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  azimuth -= 0.03
        if keys[pygame.K_RIGHT]: azimuth += 0.03
        if keys[pygame.K_UP]:    elevation = min(1.4, elevation + 0.02)
        if keys[pygame.K_DOWN]:  elevation = max(-0.2, elevation - 0.02)
        if keys[pygame.K_w]:     distancia = max(3.0, distancia - 0.1)
        if keys[pygame.K_s]:     distancia = min(20.0, distancia + 0.1)
        if keys[pygame.K_q]:     roll -= 0.03
        if keys[pygame.K_e]:     roll += 0.03

        # Calcula a Posição da Câmera (eyeX, eyeY, eyeZ)
        eye_x = distancia * math.cos(elevation) * math.sin(azimuth)
        eye_y = distancia * math.sin(elevation)
        eye_z = distancia * math.cos(elevation) * math.cos(azimuth)

        # Calcula o vetor View Up (upX, upY, upZ) considerando o Roll
        up_x = math.sin(roll)
        up_y = math.cos(roll)
        up_z = 0.0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Posiciona a câmera olhando sempre para o Ponto Focal (0, 0, 0)
        gluLookAt(eye_x, eye_y, eye_z,  0.0, 0.0, 0.0,  up_x, up_y, up_z)

        desenhar_grade_chao()
        desenhar_monolito()

        pygame.display.flip()
        pygame.time.wait(15)

if __name__ == "__main__":
    main()