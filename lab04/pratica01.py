#Instalar as bibliotecas (no terminal)
# pip install PyOpenGL PyOpenGL_accelerate pygame numpy

#Importando as bibliotecas
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

#Sistema de coordenadas de objetos
VERTICES = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), #face traseira
    (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1),     #face frontal
)

FACES = (
    (0, 1, 2, 3), (3, 2, 6, 7), (7, 6, 5, 4),
    (4, 5, 1, 0), (1, 5, 6, 2), (4, 0, 3, 7),
)

CORES = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (1, 1, 0), (1, 0, 1), (0, 1, 1),
)

def desenhar_cubo():
    glBegin(GL_QUADS)
    for i, face in enumerate(FACES):
        glColor3fv(CORES[i])
        for vertice in face:
            glVertex3fv(VERTICES[vertice])
    glEnd()

def main():
    pygame.init()
    #Sistema de coordenadas do dispositivo
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('Z-Buffer (pressione Z para ligar e desligar)')

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50)
    glMatrixMode(GL_MODELVIEW)

    #Por padrao oz-buffer vem desativado
    z_buffer = True
    glEnable(GL_DEPTH_TEST)

    angulo = 0.0
    print('Pressione "Z" para ativar/desativar o z-buffer')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                z_buffer = not z_buffer
                if z_buffer:
                    glEnable(GL_DEPTH_TEST)
                    print('Z-Buffer ATIVADO')
                else:
                    glDisable(GL_DEPTH_TEST)
                    print('Z-Buffer DESATIVADO')
        
        #Limpa o buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)
        glRotatef(angulo, 1.0, 1.0, 0.0)
        angulo += 1

        desenhar_cubo()

        pygame.display.flip()
        pygame.time.wait(15)

if __name__ == '__main__':
    main()




