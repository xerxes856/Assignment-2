import math

class Rectangle:
    """A class to represent a rectangle with width and height."""
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate and return the area of the rectangle.
        
        Returns:
            The area (width * height)
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        
        Returns:
            The perimeter (2 * (width + height))
        """
        return 2 * (self.width + self.height)
    
    def diagonal(self):
        """
        Calculate and return the length of the diagonal of the rectangle.
        Uses the Pythagorean theorem: sqrt(width^2 + height^2)
        
        Returns:
            The length of the diagonal
        """
        return math.sqrt(self.width**2 + self.height**2)
    
    def bounding_box(self):
        """
        Return the bounding box of the rectangle.
        For a rectangle, the bounding box is the same as its dimensions.
        
        Returns:
            A tuple containing (width, height)
        """
        return (self.width, self.height)
    
    def __str__(self):
        """String representation of the Rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


# Test the Rectangle class
if __name__ == "__main__":
    print("=== Testing Rectangle Class ===\n")
    
    # Create a rectangle
    rect = Rectangle(5, 3)
    print(f"Created: {rect}")
    print()
    
    # Test area method
    print(f"Area: {rect.area()}")
    print(f"Calculation: {rect.width} × {rect.height} = {rect.area()}")
    print()
    
    # Test perimeter method
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Calculation: 2 × ({rect.width} + {rect.height}) = {rect.perimeter()}")
    print()
    
    # Test diagonal method
    print(f"Diagonal: {rect.diagonal():.2f}")
    print(f"Calculation: √({rect.width}² + {rect.height}²) = {rect.diagonal():.2f}")
    print()
    
    # Test bounding_box method
    print(f"Bounding Box: {rect.bounding_box()}")
    print()
    
    # Test with another rectangle
    print("=== Testing with another rectangle ===\n")
    rect2 = Rectangle(10, 7)
    print(f"Created: {rect2}")
    print(f"Area: {rect2.area()}")
    print(f"Perimeter: {rect2.perimeter()}")
    print(f"Diagonal: {rect2.diagonal():.2f}")
    print(f"Bounding Box: {rect2.bounding_box()}")
