#Instalar as bibliotecas (no terminal)
# pip install PyOpenGL PyOpenGL_accelerate pygame numpy

#Importando as bibliotecas
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_quadrados(cor):
    glColor3fv(cor)
    glBegin(GL_QUADS)
    glVertex3f(-0.4, -0.4, 0.0)
    glVertex3f(0.4, -0.4, 0.0)
    glVertex3f(0.4, 0.4, 0.0)
    glVertex3f(-0.4, 0.4, 0.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('4. Concatenacao e Pilha')

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    angulo_1 = 0.0
    angulo_2 = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -7.0)

        #Objeto 01
        glPushMatrix()
        glScalef(0.5, 0.5, 1.0)
        desenhar_quadrados((1.0, 1.0, 0.0))
        glPopMatrix()

        #Objeto 02 [PRIMEIRO A translação e DEPOIS a rotação]
        glPushMatrix()
        glTranslatef(-2.2, 0.0, 0.0)
        glRotatef(angulo_1, 0.0, 0.0, 1.0)
        desenhar_quadrados((0.0, 1.0, 0.5))
        glPopMatrix()

        #Objeto 03 [PRIMEIRO A rotação e DEPOIS a translação]
        glPushMatrix()
        glRotatef(angulo_2, 0.0, 0.0, 1.0)
        glTranslatef(2.0, 0.0, 0.0)        
        desenhar_quadrados((0.2, 0.6, 1.0))
        glPopMatrix()


        angulo_1 += 1.5
        angulo_2 -= 5
        pygame.display.flip()
        pygame.time.wait(15)

if __name__ == '__main__':
    main()