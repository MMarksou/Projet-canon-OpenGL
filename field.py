#!/usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################
###    Fichier pour la création de terrain
##############################################################

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import target as tg

#############################################################
#variables globales
cex, cez, cey = 6.0, 3.0, 0.0
ex, ey, ez = 1.0, 1.0, 1.0
quadric = None
cam = 0

#############################################################
# Fonctions pour la création des terrains

def create_field_canon():
    """Création du terrain contenant la cible"""

    glScalef(0.5,0.15,1.0) #transformer le cube en parallépipède rectangle
    glColor3f(0.0, 0.4, 0.1)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidCube(2)

def create_field_water():
    """Création du terrain fleuve"""

    glScalef(1.0,0.09,1.0) #transformer le cube en parallépipède rectangle
    glTranslatef(1.5, 0.0, 0.0)#translation par rapport à l'origine
    glTranslatef(0.0, -0.6, 0.0)
    glColor3f(0.0, 0.8, 0.9)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.1,0.3,0.9,1))
    glutSolidCube(2)

def create_field_target():
    """Création du terrain contenant le canon"""

    glScalef(0.5,0.15,1.0) #transformer le cube en parallépipède rectangle
    glTranslatef(6.0, 0.0, 0.0) #translation par rapport à l'origine
    glColor3f(0.0, 0.4, 0.1)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidCube(2)


def display_field():
    """fonction pour générer les différents types de terrain"""
    glPushMatrix()

    #création terrain cible
    create_field_target()
    glPopMatrix()

    #création terrain fleuve
    glPushMatrix()
    create_field_water()
    glPopMatrix()

    #création terrain canon
    glPushMatrix()
    create_field_canon()
    glPopMatrix()

    #création de la cible
    glPushMatrix()
    tg.display_target()
    glPopMatrix()

    






##################################################################
# Fonctions pour le test

def reshape(width, height):
    global ex, ey, ez, cex, cey, cez

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)

    # glLoadIdentity()

    gluLookAt(cex, cey, cez, ex, ey, ez, 0.0, 1.0, 0.0)

    glMatrixMode(GL_MODELVIEW)

def init():
    global quadric

    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH)
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL) #FILL = remplir,

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.1, 0.1, 0.1, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 5.0, 5.0, 1)) # initialise et place la lumière 0

    glEnable(GL_COLOR_MATERIAL)

def keyboard(key, x, y):
    """fonction de contrôle de direction"""

    global cex, cez, cey, ex, ey, ez,bi
    #caméra axe du z
    if key == b'o':
        cez = cez - 0.5
    elif key == b'l':
        cez = cez + 0.5

    #caméra rotation
    if key == b'i':
        cex = (cex - 10) % 360
    elif key == b'p':
        cex = (cex + 10) % 360

    #caméra translation
    if key == b'k':
        cey = cey + 0.5
    elif key == b'm':
        cey = cey - 0.5

    #caméra reset
    if key == b'r':
        cx = 6.0
        cy = 3.0
        cz = 0.0

    glutPostRedisplay()  # indispensable en Python

def display():

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor4f (1.0, 1.0, 1.0, 1.0)
    glLoadIdentity()

    display_field()

    glutSwapBuffers()


#############################################################

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

    glutCreateWindow('test terrain')
    glutReshapeWindow(1080,720)

    glutReshapeFunc(reshape) #définit la fonction de scène
    glutDisplayFunc(display)#définit la fonction d'affichage
    glutKeyboardFunc(keyboard) #événement clavier

    init()

    glutMainLoop()
