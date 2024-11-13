import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Sistema Solar Mejorado")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Texto en la parte superior
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, 250)
text.write("Este es el sistema solar", align="center", font=("Arial", 24, "bold"))

# Dibujar órbitas como círculos
orbits = [100, 150, 200, 250]  # Distancias de las órbitas
for orbit in orbits:
    orbiter = turtle.Turtle()
    orbiter.hideturtle()
    orbiter.speed(0)
    orbiter.color("white")
    orbiter.penup()
    orbiter.goto(0, -orbit)
    orbiter.pendown()
    orbiter.circle(orbit)

# Crear el Sol
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)  # Tamaño del sol
sun.penup()
sun.goto(0, 0)

# Crear planetas
planets = [
    {"color": "gray", "distance": 100, "size": 0.6},   # Primer planeta
    {"color": "orange", "distance": 150, "size": 0.8},  # Segundo planeta
    {"color": "blue", "distance": 200, "size": 0.7},    # Tercer planeta
    {"color": "red", "distance": 250, "size": 0.5},     # Cuarto planeta
]

for planet_info in planets:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(planet_info["color"])
    planet.shapesize(planet_info["size"])
    planet.penup()
    planet.goto(planet_info["distance"], 0)

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
