#Instalar as bibliotecas (no terminal)
# pip install PyOpenGL PyOpenGL_accelerate pygame numpy

#Importando as bibliotecas
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def desenhar_cubo(cor):
    glColor3fv(cor)
    vertices = (
        (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
        (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1),
    )
    arestas = (
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7),
    )
    glBegin(GL_LINES)
    for aresta in arestas:
        for v in aresta:
            glVertex3fv(vertices[v])
    glEnd()

def configurar_projecao(usar_perspectiva, largura, altura):
    aspecto = largura / altura
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    if usar_perspectiva:
        #Objetos distantes ficam menores
        glFrustum(-aspecto, aspecto, -1.0, 1.0, 1.5, 30)
    else:
        #Projecao ortografica (ignora o efeito de profundidade em Z)
        glOrtho(-3.0 * aspecto, 3.0 * aspecto, -3.0, 3.0, 1.5, 30)
    glMatrixMode(GL_MODELVIEW)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('5. Projecao de cameras')

    glEnable(GL_DEPTH_TEST)
    glLineWidth(2.0)

    usar_perspectiva = True
    configurar_projecao(usar_perspectiva, display[0], display[1])
    print('Pressione "P" para alternar entre as projeções.')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                usar_perspectiva = not usar_perspectiva
                configurar_projecao(usar_perspectiva, display[0], display[1])
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        #Cubo 1 Z=-4 (proximo a camera)
        glPushMatrix()
        glTranslatef(-1.5, 0.0, -4.0)
        glRotatef(20, 1, 1, 0)
        desenhar_cubo((0.0, 1.0, 1.0))
        glPopMatrix()

        #Cubo 2 Z=-12 (distante da camera)
        glPushMatrix()
        glTranslatef(-1.5, 0.0, -12.0)
        glRotatef(20, 1, 1, 0)
        desenhar_cubo((0.0, 1.0, 0.3))
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(20)

if __name__ == '__main__':
    main()