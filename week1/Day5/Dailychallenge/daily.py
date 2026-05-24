import math
import turtle


class Circle:

    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Vous devez fournir un rayon ou un diametre.")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area():.2f})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


# --- Tests ---
c1 = Circle(radius=5)
c2 = Circle(radius=3)
c3 = Circle(diameter=10)
c4 = Circle(radius=7)

print("=== Affichage ===")
print(c1)
print(c2)

print("\n=== Addition ===")
c5 = c1 + c2
print(f"c1 + c2 = {c5}")

print("\n=== Comparaisons ===")
print(f"c1 > c2 : {c1 > c2}")
print(f"c1 < c2 : {c1 < c2}")
print(f"c1 == c3 : {c1 == c3}")

print("\n=== Tri d'une liste ===")
circles = [c4, c2, c1, c3]
circles_sorted = sorted(circles)
for c in circles_sorted:
    print(c)


# --- Bonus Turtle ---
def draw_circles(circles):
    screen = turtle.Screen()
    screen.title("Cercles tries")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)
    t.hideturtle()

    x = -300
    for c in circles:
        t.penup()
        t.goto(x, -c.radius)
        t.pendown()
        t.circle(c.radius)
        t.penup()
        t.goto(x, -c.radius - 20)
        t.write(f"r={c.radius}", align="center")
        x += c.radius * 2 + 30

    turtle.done()


draw_circles(circles_sorted)