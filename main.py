#!/usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################
###    Fichier pour la création de terrain
##############################################################

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import field as fl
import canon as ca
import canonball as cb
import target as tg

#############################################################
# Variables globales

cx,cy,cz = 0.0, 0.0, 0.0 #position cam temporaire
ox,oy,oz = 0.0, 0.0, 0.0 #position actuelle cam

px,py,pz = -3.0, 3.0, 0.0 #emplacement initial de la scène

#############################################################
def init():
    global quadric

    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH)
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL) #FILL = remplir,

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.7, 0.7, 0.7, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.2, 0.2, 0.2, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (-1.0, 1.0, 1.0, 0.0)) # initialise et place la lumière 0

    glEnable(GL_COLOR_MATERIAL)

def reshape(width, height):

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    gluLookAt(-2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) #se placer dans 'lunivers'

    glMatrixMode(GL_MODELVIEW)

def display():
    global cx, cz, cy, ox, oy, oz, quadric, reset

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # glClearColor(0.8,0.7,0.4,1.0)

    # glColor4f (1.0, 1.0, 1.0, 1.0)
    glLoadIdentity()

    #mouvement caméra

    glTranslatef(1.5,0.0,0.0)
    glRotatef(oy, 0.0, 1.0, 0.0)
    glTranslatef(-1.5,0.0,0.0)

    glTranslatef(1.5,0.0,0.0)
    glRotatef(oz, 0.0, 0.0, 1.0)
    glTranslatef(-1.5,0.0,0.0)

    glPushMatrix()

    fl.display_field()

    glPopMatrix()

    glPushMatrix()

    glScalef(0.2,0.2,0.2) #réduire la taille du canon
    glTranslatef(0.0, 1.3, 0.0) #canon dessus le sol
    glRotatef(90,0.0,-1.0,0.0) #bouche du canon vers la cible
    ca.display_canon(quadric)

    glPopMatrix()

    glutSwapBuffers()


def keyboard(key, x, y):
    """fonction de contrôle de direction"""

    global cx, cz, cy, ox, oy, oz, px, py, pz

    #caméra rotation sur le côté
    if key == b'k':
        oy = (oy - 10) % 360
    elif key == b'm':
        oy = (oy + 10) % 360

    #caméra rotation dessus dessous
    if key == b'o' and oz > -28.0:
        oz = oz - 0.5

    elif key == b'l' and oz < 45.0: #restriction de caméra
        oz = oz + 0.5

    #caméra reset
    if key == b'r':
        oz, oy = 0.0, 0.0
        gluLookAt(-2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    ca.mouv_canon(key, x, y)
    tg.keyboard_target(key)

    glutPostRedisplay()  # indispensable en Python

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

    glutCreateWindow('Canon game')
    glutReshapeWindow(1080,720)

    glutReshapeFunc(reshape) #définit la fonction de scène
    glutDisplayFunc(display)#définit la fonction d'affichage
    glutKeyboardFunc(keyboard) #définit la fonction des prises de commande par clavier

    init()

    glutMainLoop()

#############################################################

if __name__ == '__main__':
    main()
