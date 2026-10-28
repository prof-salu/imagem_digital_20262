#Instalar as bibliotecas (no terminal)
# pip install PyOpenGL PyOpenGL_accelerate pygame numpy

#Importando as bibliotecas
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_objeto():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.8, 1.0)
    glVertex3f(0.2, 0.2, 0.0)
    glVertex3f(0.6, 0.2, 0.0)
    glVertex3f(0.2, 1.8, 0.0)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(0.2, 0.2, 0.0)
    glVertex3f(1.4, 0.2, 0.0)
    glVertex3f(0.2, 0.7, 0.0)
    glEnd()

def desenhar_eixos():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0); glVertex3f(-3, 0, 0); glVertex3f(3, 0, 0)
    glColor3f(0, 1, 0); glVertex3f(0, -3, 0); glVertex3f(0, 3, 0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('3. Reflexao 3D')

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)

        #0. Eixos de vizualização
        desenhar_eixos()

        #1. Objeto original
        desenhar_objeto()

        #2. Reflexão YZ
        glPushMatrix()
        glScalef(-1.0, 1.0, 1.0)
        desenhar_objeto()
        glPopMatrix()

        #3. Reflexao XZ
        glPushMatrix()
        glScalef(1.0, -1.0, 1.0)
        desenhar_objeto()
        glPopMatrix()

        #4. Reflexao YZ e XZ
        glPushMatrix()
        glScalef(-1.0, -1.0, 1.0)
        desenhar_objeto()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(30)

if __name__ == '__main__':
    main()