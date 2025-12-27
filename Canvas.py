import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math


class Canvas:
    """A class to represent a canvas where shapes can be displayed."""
    
    def __init__(self, width=800, height=600, background_color='white', title='Canvas'):
        """
        Initialize a Canvas with dimensions and properties.
        
        Args:
            width: Width of the canvas in pixels (default: 800)
            height: Height of the canvas in pixels (default: 600)
            background_color: Background color of the canvas (default: 'white')
            title: Title of the canvas window (default: 'Canvas')
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.title = title
        self.shapes = []  # List to store shapes on the canvas
    
    def add_shape(self, shape):
        """
        Add a shape to the canvas.
        
        Args:
            shape: A Circle or Rectangle object to add to the canvas
        """
        self.shapes.append(shape)
    
    def remove_shape(self, shape):
        """
        Remove a shape from the canvas.
        
        Args:
            shape: The shape to remove
        """
        if shape in self.shapes:
            self.shapes.remove(shape)
    
    def clear(self):
        """Remove all shapes from the canvas."""
        self.shapes = []
    
    def display(self):
        """Display the canvas with all its shapes using matplotlib."""
        fig, ax = plt.subplots(figsize=(self.width/100, self.height/100))
        ax.set_facecolor(self.background_color)
        
        # Draw all shapes
        for shape in self.shapes:
            if isinstance(shape, Circle):
                circle = mpatches.Circle(
                    (shape.x, shape.y),
                    shape.radius,
                    facecolor=shape.fill,
                    edgecolor=shape.stroke,
                    linewidth=shape.stroke_width
                )
                ax.add_patch(circle)
            elif isinstance(shape, Rectangle):
                rectangle = mpatches.Rectangle(
                    (shape.x, shape.y),
                    shape.width,
                    shape.height,
                    facecolor=shape.fill,
                    edgecolor=shape.stroke,
                    linewidth=shape.stroke_width
                )
                ax.add_patch(rectangle)
        
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.set_title(self.title, fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def get_shape_count(self):
        """Return the number of shapes on the canvas."""
        return len(self.shapes)
    
    def __str__(self):
        """String representation of the Canvas."""
        return f"Canvas(width={self.width}, height={self.height}, shapes={len(self.shapes)})"


class Circle:
    """A class to represent a circle with position and graphical attributes."""
    
    def __init__(self, radius, x=0, y=0, fill='blue', stroke='black', stroke_width=2):
        """
        Initialize a Circle.
        
        Args:
            radius: The radius of the circle
            x: X-coordinate of the circle's center (default: 0)
            y: Y-coordinate of the circle's center (default: 0)
            fill: Color to fill the inside (default: 'blue')
            stroke: Color of the boundary line (default: 'black')
            stroke_width: Width of the boundary line (default: 2)
        """
        self.radius = radius
        self.x = x
        self.y = y
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
    
    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle(radius={self.radius}, pos=({self.x},{self.y}), fill={self.fill})"


class Rectangle:
    """A class to represent a rectangle with position and graphical attributes."""
    
    def __init__(self, width, height, x=0, y=0, fill='red', stroke='black', stroke_width=2):
        """
        Initialize a Rectangle.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            x: X-coordinate of the rectangle's bottom-left corner (default: 0)
            y: Y-coordinate of the rectangle's bottom-left corner (default: 0)
            fill: Color to fill the inside (default: 'red')
            stroke: Color of the boundary line (default: 'black')
            stroke_width: Width of the boundary line (default: 2)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, pos=({self.x},{self.y}), fill={self.fill})"


# Test the Canvas class
if __name__ == "__main__":
    print("=== Testing Canvas Class ===\n")
    
    # Create a canvas
    canvas = Canvas(width=600, height=400, background_color='lightgray', title='My Art Canvas')
    print(f"Created: {canvas}\n")
    
    # Create some shapes
    circle1 = Circle(radius=50, x=150, y=200, fill='yellow', stroke='orange', stroke_width=3)
    circle2 = Circle(radius=30, x=300, y=250, fill='lightblue', stroke='blue', stroke_width=2)
    rect1 = Rectangle(width=80, height=60, x=400, y=150, fill='lightgreen', stroke='darkgreen', stroke_width=2)
    rect2 = Rectangle(width=100, height=40, x=100, y=100, fill='pink', stroke='red', stroke_width=3)
    
    # Add shapes to canvas
    canvas.add_shape(circle1)
    canvas.add_shape(circle2)
    canvas.add_shape(rect1)
    canvas.add_shape(rect2)
    
    print(f"Canvas now has {canvas.get_shape_count()} shapes")
    print("\nShapes on canvas:")
    for i, shape in enumerate(canvas.shapes, 1):
        print(f"  {i}. {shape}")
    
    # Display the canvas
    print("\nDisplaying canvas...")
    canvas.display()
    
    # Test removing a shape
    print("\nRemoving circle2...")
    canvas.remove_shape(circle2)
    print(f"Canvas now has {canvas.get_shape_count()} shapes")
    
    # Test clearing the canvas
    print("\nClearing canvas...")
    canvas.clear()
    print(f"Canvas now has {canvas.get_shape_count()} shapes")
