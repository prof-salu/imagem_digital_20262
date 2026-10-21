#Instalar as bibliotecas (no terminal)
# pip install PyOpenGL PyOpenGL_accelerate pygame numpy

#Importando as bibliotecas
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_piramide():
    glBegin(GL_TRIANGLES)
    #Frente vermelho
    glColor3f(1, 0, 0); glVertex3f(0, 1, 0); glVertex3f(-1, -1, 1); glVertex3f(1, -1, 1);
    #Direita Verde
    glColor3f(0, 1, 0); glVertex3f(0, 1, 0); glVertex3f(1, -1, 1); glVertex3f(1, -1, -1);
    #Tras azul
    glColor3f(0, 0, 1); glVertex3f(0, 1, 0); glVertex3f(1, -1, -1); glVertex3f(-1, -1, -1);
    #Esquerda amarelo
    glColor3f(1, 1, 0); glVertex3f(0, 1, 0); glVertex3f(-1, -1, -1); glVertex3f(-1, -1, 1);
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('setas=Translacao | R=Rotacao | W/S=Escala')

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    tx, ty = 0.0, 0.0
    angulo = 0.0
    escala = 1.0

    print('Controles: Setas (Transladar) | R (Rotacionar) | W/S (Escalonar)')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            keys = pygame.key.get_pressed()
            #Translação
            if keys[pygame.K_LEFT]: tx -= 0.05
            if keys[pygame.K_RIGHT]: tx += 0.05
            if keys[pygame.K_UP]: ty += 0.05
            if keys[pygame.K_DOWN]: ty -= 0.05

            #Rotação
            if keys[pygame.K_r]: angulo += 2.0

            #Escala
            if keys[pygame.K_w]: escala += 0.02
            if keys[pygame.K_s]: escala -= 0.02

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            #Posicionamento no mundo
            glTranslatef(tx, ty, -6.0)
            glRotatef(angulo, 0.0, 1.0, 0.0)
            glScalef(escala, escala, escala)

            desenhar_piramide()

            pygame.display.flip()
            pygame.time.wait(15)

if __name__ == '__main__':
    main()
