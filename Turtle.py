import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing with Turtles")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create a turtle
t = turtle.Turtle()
t.speed(3)  # Set drawing speed (1=slow, 10=fast, 0=instant)


def draw_triangle(turtle_obj, x, y, size, color):
    """
    Draw an equilateral triangle.
    
    Args:
        turtle_obj: The turtle object
        x: X-coordinate of starting position
        y: Y-coordinate of starting position
        size: Length of each side
        color: Fill color
    """
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    
    turtle_obj.fillcolor(color)
    turtle_obj.begin_fill()
    
    for _ in range(3):
        turtle_obj.forward(size)
        turtle_obj.left(120)
    
    turtle_obj.end_fill()


def draw_pentagon(turtle_obj, x, y, size, color):
    """
    Draw a regular pentagon.
    
    Args:
        turtle_obj: The turtle object
        x: X-coordinate of starting position
        y: Y-coordinate of starting position
        size: Length of each side
        color: Fill color
    """
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    
    turtle_obj.fillcolor(color)
    turtle_obj.begin_fill()
    
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.left(72)  # 360/5 = 72 degrees
    
    turtle_obj.end_fill()


def write_text(turtle_obj, x, y, text, font_size=20, color="black"):
    """
    Write text on the screen.
    
    Args:
        turtle_obj: The turtle object
        x: X-coordinate of text position
        y: Y-coordinate of text position
        text: The text string to write
        font_size: Size of the font
        color: Color of the text
    """
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    turtle_obj.write(text, align="center", font=("Arial", font_size, "bold"))


# Main drawing code
print("Drawing with Turtles!")
print("=" * 40)

# Set turtle pen properties
t.pensize(2)
t.pencolor("black")

# Draw a triangle
print("Drawing triangle...")
draw_triangle(t, -200, 100, 100, "red")

# Draw a pentagon
print("Drawing pentagon...")
draw_pentagon(t, 100, 100, 80, "green")

# Write some text
print("Writing text...")
t.color("darkblue")
write_text(t, 0, -150, "Welcome to Turtle Graphics!", font_size=24, color="darkblue")
write_text(t, 0, -200, "Triangle & Pentagon", font_size=16, color="purple")

# Hide the turtle when done
t.hideturtle()

print("\nDrawing complete!")
print("Click on the window to close it.")

# Keep the window open until clicked
screen.exitonclick()
