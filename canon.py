#!/usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################
###    Bibliothéque pour la création du canon
##############################################################

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import cos, sin
import canonball as cb

#############################################################
#variables globales

barrel = 0.0
pos = [0.0,0.0,0.0]
c_rot, c_move = 0.0, 0.0
wr, wl = 0.0,0.0
quadric = None
quadric1 = None

#############################################################
# Fonctions pour la création et contrôle du canon

def create_barrel(quadric):
    """création du fut du canon avec un tube"""

    # glScalef(1.0,0.09,1.0) #transformer le cube en parallépipède rectangle
    # glTranslatef(1.5, 0.0, 0.0)#translation par rapport à l'origine
    glRotatef(180,0.0,1.0,0.0)
    glTranslatef(0.0,0.0,-0.30)
    glColor3f(0.7, 0.6, 0.0)
    glColorMaterial(GL_FRONT, GL_AMBIENT)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.2,0.0,0.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.3, 0.3, 0.3))
    gluCylinder(quadric, 0.15, 0.12, 1.0, 32, 32)
    gluSphere(quadric, 0.15, 32, 32)

def create_wheel_r(quadric):
    """creation de la roues droite du canon avec des tores"""

    glColor3f(0.5, 0.2, 0.0)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidTorus(0.07, 0.19, 40, 50)
    glRotatef(90,0.0,1.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)

def create_wheel_l(quadric):
    """creation de la roues gauche du canon avec des tores"""

    glColor3f(0.5, 0.2, 0.0)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidTorus(0.07, 0.19, 40, 50)
    glRotatef(90,0.0,1.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)

def display_canon(quadric):
    """affichage du canon sur le terrain"""
    global c_rot, pos, barrel, wr, wl

    glTranslatef(pos[0],pos[1],pos[2])
    glRotatef(c_rot,0.0,-1.0,0.0)

    glPushMatrix()
    #création du fut
    glRotatef(barrel,1.0,0.0,0.0)
    create_barrel(quadric)
    glPopMatrix()

    #création de la roue droite
    glPushMatrix()
    glRotatef(90,0.0,1.0,0.0)
    glTranslatef(0.0,-0.25,0.25)
    glRotatef(wr,0.0,0.0,1.0)
    create_wheel_r(quadric)
    glPopMatrix()

    #création de la roue gauche
    glPushMatrix()
    glRotatef(90,0.0,1.0,0.0)
    glTranslatef(0.0,-0.25,-0.25)
    glRotatef(wl,0.0,0.0,1.0)
    create_wheel_l(quadric)
    glPopMatrix()

    glPushMatrix()
    cb.display_canonball(quadric, barrel)
    glPopMatrix()



def mouv_canon(key, x, y):
    """fonction de contrôle de direction pour le canon"""

    global barrel, c_move, c_rot, pos, wr, wl

    #relever/baisser le fut du canon
    if key == b'a' and barrel < 90:
        barrel = (barrel + 0.5) % 360
    if key == b'e' and barrel > 0:
        barrel = (barrel - 0.5) % 360

    #mouvement avant/arrière canon
    if key == b'z':
        tmp1 = pos[0] + sin(c_rot*3.1415/180)*0.08
        tmp2 = pos[2] - cos(c_rot*3.1415/180)*0.08
        if tmp1 > -4.8 and tmp1 < 4.8 and tmp2 > -2.2 and tmp2 < 2.2:
            pos[0] = tmp1
            pos[2] = tmp2
        wr = (wr + 7) % 360
        wl = (wl - 7) % 360

    if key == b's':
        tmp1 = pos[0] - sin(c_rot*3.1415/180)*0.08
        tmp2 = pos[2] + cos(c_rot*3.1415/180)*0.08
        if tmp1 > -4.8 and tmp1 < 4.8 and tmp2 > -2.2 and tmp2 < 2.2:
            pos[0] = tmp1
            pos[2] = tmp2
        wr = (wr - 7) % 360
        wl = (wl + 7) % 360

    #rotation droite et gauche du canon
    if key == b'q':
        c_rot = (c_rot - 2) % 360
        wr = (wr + 7) % 360

    if key == b'd':
        c_rot = (c_rot + 2) % 360
        wl = (wl - 7) % 360

    cb.fire(key)

    glutPostRedisplay()  # indispensable en Python









#############################################################
#fonction test

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

def reshape(width, height):

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)

    # glLoadIdentity()

    gluLookAt(6.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glMatrixMode(GL_MODELVIEW)

def display():
    global quadric

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor4f (1.0, 1.0, 1.0, 1.0)
    glLoadIdentity()

    glPushMatrix()

    display_canon(quadric)

    glPopMatrix()

    glutSwapBuffers()

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

    glutCreateWindow('test canon')
    glutReshapeWindow(1080,720)

    glutReshapeFunc(reshape) #définit la fonction de scène
    glutDisplayFunc(display)#définit la fonction d'affichage
    glutKeyboardFunc(mouv_canon) #définit la fonction des prises de commande par clavier

    init() # A DEFINIR !!!!!!

    glutMainLoop()
