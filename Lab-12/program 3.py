class Solid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self):
        return self.length * self.width * self.height


solid = Solid(2, 3, 4)
print("Surface Area:", solid.surface_area())
print("Volume:", solid.volume())
