## Importamos la libreria turtle
import turtle
x = turtle.Screen()
x.bgcolor('black')
libreria = turtle.Turtle()
libreria.speed(15)

# Partes y secciones de la bandera

def blue_rectangle_below():
    libreria.color('sky blue')
    libreria.begin_fill()
    libreria.forward(300)
    libreria.right(90)
    libreria.forward(120)
    libreria.right(90)
    libreria.forward(600)
    libreria.right(90)
    libreria.forward(120)
    libreria.right(90)
    libreria.forward(300)
    libreria.end_fill()

def white_rectangle():
    libreria.color('white')
    libreria.begin_fill()
    libreria.left(90)
    libreria.forward(100) 
    libreria.left(90)
    libreria.forward(600)
    libreria.left(90)
    libreria.forward(100) 
    libreria.left(90)
    libreria.forward(300)
    libreria.end_fill()

def blue_rectangle_above():
    libreria.color('sky blue')
    libreria.begin_fill()
    libreria.forward(120)
    libreria.left(90)
    libreria.forward(600) 
    libreria.left(90)
    libreria.forward(120)
    libreria.left(90)
    libreria.forward(600)
    libreria.end_fill()
    print(turtle.pos())

def outline():
    libreria.color('black')
    libreria.right(90)
    libreria.forward(220)
    libreria.right(90)
    libreria.forward(600)
    libreria.right(90)
    libreria.forward(340)
    libreria.right(90)
    libreria.forward(600)
    libreria.right(90)
    libreria.forward(120)
    libreria.right(90)
    libreria.forward(170)

def sol_de_mayo():
    libreria.color('red', 'yellow')
    libreria.begin_fill()
    grados = 0
    for x in range(1, 40):
     for x in range(0, 4):
        libreria.forward(20)
        libreria.left(90)
     libreria.left(grados + 10)
    libreria.end_fill()
    
def letters():
    libreria.color('blue')
    libreria.write("FELICIDADES ARGENTINA CAMPEÓN DEL MUNDO 2022", 
    align="center", font=(None, 16, "bold"))

    

    ## Ejecucuion del lapiz

libreria.penup()
blue_rectangle_below()
libreria.forward(300)
white_rectangle()
libreria.forward(300)
libreria.left(90)
libreria.forward(100)
blue_rectangle_above()
outline()
libreria.penup()
libreria.goto(10,50)
libreria.pendown()
sol_de_mayo()
libreria.penup()
libreria.goto(0,-170)
letters()
libreria.goto(-5,-400)
### Listo
x.mainloop()

