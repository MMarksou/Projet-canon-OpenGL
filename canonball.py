#!/usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################
###    Fichier pour la création de l'obus
##############################################################

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from time import sleep
from math import cos, sin
from copy import deepcopy
import target as tg

#############################################################
#variables globales
quadric = None
boom = 0 #variable de mise à feu
di = 0 #distance par rapport au canon
t = 0.01 #le "temps"
hi = 0.0 #hauteur de la bouche du canon par rapport au 0.0,0.0
dc = 0.7 #distance boulet/centre
v = 20 #vitesse du boulet de canon
g = 9.81 #la gravité
velx = 0 #la vélocité en x
vely = 0 #la vélocité en y
pos_ball = [0.0,0.0,0.0]

#############################################################
# Fonctions pour la création et contrôle du canon

def create_canonball(quadric):
    """création de l'obus"""

    glScalef(0.05,0.05,0.05)
    glTranslatef(4.0, 0.25, 0.0)
    glColor3f(0.3, 0.3, 0.3)
    glColorMaterial(GL_FRONT, GL_AMBIENT)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.3,0.3,0.3))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.2, 0.2, 0.2))
    gluSphere(quadric, 2.0, 20, 20)


def display_canonball(quadric, angle):
    """affichage de l'obus"""
    global boom,di,dc,v,g,t,hi,vely, velx

    if boom == 1:
        if di == 0.0 and hi == 0.0:

            velx = v*cos(angle*3.1415/180)
            vely = v*sin(angle*3.1415/180)

        glTranslatef(-0.2,hi,di)
        create_canonball(quadric)

        a = [0]*16
        mat = list(glGetFloatv(GL_MODELVIEW_MATRIX,a))

        #calcul de trajectoire
        d = di - velx*t
        h = hi + (vely*t) - 1/2 * g * t ** 2

        di = d
        hi = h

        vely = vely - 9.8 * t

        #test de collision avec l'aide de la matrice globale
        if tg.hit_target(mat[12],mat[13],mat[14]) or hi <-1.0:
            boom = 0
            hi = 0.0
            di = 0.0

    glutPostRedisplay();

def fire(key):
    """fonction pour tirer l'obus"""
    global boom

    if key == b' ':
        boom = 1

    glutPostRedisplay()  # indispensable en Python
