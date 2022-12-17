# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:10:13 2022

@author: Andres
"""
# Logo de windows
# Importamos turtle
from turtle import *
## Establecemos la velocidad de dibujo
speed(1)
width(4)
## Configuramos el color de fondo
bgcolor('black')
## Establecemos el color azul del logo
color('blue')

begin_fill()
penup()

## Movimiento de turtle al punto de partida
goto(-50,60)
pendown()
# Ir a la parte superior derecha
goto(100,100)
# Ir a la parte inferior izquierda
goto(100,-100)
# Ir a la parte inferior izquierda
goto(-50,-60)
# Ir al punto de partida
goto(-50,60)

end_fill()
penup()

## Establecer color negro
color('black')
## Cambiar el tamaño de la ventana
width(10)

## Cortamos el logo
## Comenzando desde el medio izquierdo
goto(-50,0)
pendown()
## Terminamos en el centro derecho
goto(100, 0)
penup()

###Cortamos la forma en dos mitades verticalmente
## A partir de la mitad superiorg
goto(25,80)
pendown()
## Terminamos en la parte inferior central
goto(25,-80)

### Listo
done()