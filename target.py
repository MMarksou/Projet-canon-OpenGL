#!/usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################
###    Bibliothéque pour la création du canon
##############################################################

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from random import uniform
from math import cos, sin

#############################################################
#variables globales

pos = [] #position de la target
hit = False
tx, tz = 0.0, 0.0


#############################################################
# Fonctions pour la création de la cible et savoir si elle est touchée

def create_target():
    """la cible sur le terrain target"""
    glColor3f(0.8, 0.0, 0.0)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidCube(0.25)

def display_target():
    """Fonction d'affichage de la cible"""
    global tx, tz, pos

    glScalef(0.8,0.8,0.8) #réduire le cube à une taille convenable
    if pos == []:
        pos = [0.0,0.3,0.0]
        pos[0], pos[2] = random_pos_target()
    glTranslatef(pos[0],pos[1],pos[2])
    create_target()

def visual_trigger():
    """ change aléatoirement la couleur de l'arrière plan si ça touche ou non"""
    r = uniform(0,1.0)
    g = uniform(0,1.0)
    b = uniform(0,1.0)
    glClearColor(r,g,b,1.0)

def random_pos_target():
    """génère aléatoirement la position de la cible sur le terrain cible"""
    x = uniform(3.1,4.2)
    z = uniform(-1.2,1.2)
    return x, z

def hit_target(x,y,z):
    """Fonction qui renvoie true si la cible est touchée"""
    global pos

    tmp = False

    #si le boulet se trouve entre les coordonnées si dessous, il touche la cible
    if(pos[0]-0.15625 <= x and x <= pos[0]+0.15625):
        if(pos[1]-0.3 <= y and y <= pos[1]+0.3):
            if(pos[2]-0.15625 <= z and z <= pos[2]+0.15625):
                pos = []
                tmp = True
                visual_trigger()
    return tmp


def keyboard_target(key):
    """fonction de contrôle de la cible"""
    global tx, tz

    if key == b'5':
        pos[0] -= 0.2

    if key == b'2':
        pos[0] += 0.2

    if key == b'1':
        pos[2] -= 0.2

    if key == b'3':
        pos[2] += 0.2
