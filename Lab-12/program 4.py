class Shape:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == "circle":
            radius = self.dimensions[0]
            return 3.14 * radius ** 2
        elif self.shape_type == "rectangle":
            length, width = self.dimensions
            return length * width
        elif self.shape_type == "square":
            side = self.dimensions[0]
            return side ** 2
        else:
            raise ValueError("Unknown shape type")

    def perimeter(self):
        if self.shape_type == "circle":
            radius = self.dimensions[0]
            return 2 * 3.14 * radius
        elif self.shape_type == "rectangle":
            length, width = self.dimensions
            return 2 * (length + width)
        elif self.shape_type == "square":
            side = self.dimensions[0]
            return 4 * side
        else:
            raise ValueError("Unknown shape type")


# Example usage
shape1 = Shape("circle", 5)
shape2 = Shape("rectangle", 4, 6)
shape3 = Shape("square", 3)
print(f"Circle Area: {shape1.area()}, Perimeter: {shape1.perimeter()}")
print(f"Rectangle Area: {shape2.area()}, Perimeter: {shape2.perimeter()}")
print(f"Square Area: {shape3.area()}, Perimeter: {shape3.perimeter()}")
