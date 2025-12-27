import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Circle:
    """A class to represent a circle with graphical attributes."""
    
    def __init__(self, radius, fill='blue', stroke='black', stroke_width=2):
        """
        Initialize a Circle with radius and graphical attributes.
        
        Args:
            radius: The radius of the circle
            fill: Color to fill the inside of the circle (default: 'blue')
            stroke: Color of the boundary line (default: 'black')
            stroke_width: Width of the boundary line (default: 2)
        """
        self.radius = radius
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
    
    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """Calculate and return the diameter of the circle."""
        return 2 * self.radius
    
    def __str__(self):
        """String representation of the Circle."""
        return f"Circle(radius={self.radius}, fill={self.fill}, stroke={self.stroke})"


class Rectangle:
    """A class to represent a rectangle with graphical attributes."""
    
    def __init__(self, width, height, fill='red', stroke='black', stroke_width=2):
        """
        Initialize a Rectangle with width, height and graphical attributes.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            fill: Color to fill the inside of the rectangle (default: 'red')
            stroke: Color of the boundary line (default: 'black')
            stroke_width: Width of the boundary line (default: 2)
        """
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def diagonal(self):
        """Calculate and return the diagonal of the rectangle."""
        return math.sqrt(self.width**2 + self.height**2)
    
    def bounding_box(self):
        """Return the bounding box of the rectangle."""
        return (self.width, self.height)
    
    def __str__(self):
        """String representation of the Rectangle."""
        return f"Rectangle(width={self.width}, height={self.height}, fill={self.fill}, stroke={self.stroke})"


def visualize_shapes(shapes):
    """
    Visualize a list of shapes using matplotlib.
    
    Args:
        shapes: List of Circle and/or Rectangle objects to visualize
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    x_offset = 0
    
    for shape in shapes:
        if isinstance(shape, Circle):
            circle = mpatches.Circle(
                (x_offset + shape.radius, shape.radius),
                shape.radius,
                facecolor=shape.fill,
                edgecolor=shape.stroke,
                linewidth=shape.stroke_width
            )
            ax.add_patch(circle)
            x_offset += shape.radius * 2 + 2
            
        elif isinstance(shape, Rectangle):
            rectangle = mpatches.Rectangle(
                (x_offset, 0),
                shape.width,
                shape.height,
                facecolor=shape.fill,
                edgecolor=shape.stroke,
                linewidth=shape.stroke_width
            )
            ax.add_patch(rectangle)
            x_offset += shape.width + 2
    
    ax.set_xlim(-1, x_offset)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Shape Visualization', fontsize=14, fontweight='bold')
    plt.show()


# Test the classes with graphical attributes
if __name__ == "__main__":
    print("=== Testing Circle with Graphical Attributes ===\n")
    
    circle1 = Circle(3, fill='lightblue', stroke='darkblue', stroke_width=3)
    print(circle1)
    print(f"Area: {circle1.area():.2f}")
    print(f"Circumference: {circle1.circumference():.2f}")
    print()
    
    print("=== Testing Rectangle with Graphical Attributes ===\n")
    
    rect1 = Rectangle(5, 3, fill='lightcoral', stroke='darkred', stroke_width=2)
    print(rect1)
    print(f"Area: {rect1.area()}")
    print(f"Perimeter: {rect1.perimeter()}")
    print()
    
    print("=== Creating Multiple Shapes for Visualization ===\n")
    
    shapes = [
        Circle(2, fill='yellow', stroke='orange', stroke_width=3),
        Rectangle(4, 3, fill='lightgreen', stroke='darkgreen', stroke_width=2),
        Circle(1.5, fill='pink', stroke='purple', stroke_width=2),
        Rectangle(3, 5, fill='lightblue', stroke='blue', stroke_width=3)
    ]
    
    for i, shape in enumerate(shapes, 1):
        print(f"Shape {i}: {shape}")
    
    print("\nVisualizing shapes...")
    visualize_shapes(shapes)
