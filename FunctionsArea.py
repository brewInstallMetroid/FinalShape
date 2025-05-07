import math as m

#TODO: Add/finish coding surface area and 3d shapes area functions AND ADD TYPE HINTING

def circle(radius):
    radius = float(radius)
    if radius <= 0:
        raise TypeError
    else:
        return m.pi * m.pow(radius, 2)

def triangle(base, height):
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise TypeError
    else:
        return (0.5 * base) * height

def rectangle(x, y):
    x = float(x)
    y = float(y)
    if x <= 0 or y <= 0:
        raise TypeError
    else:
        return x * y

def square(x):
     x = float(x)
     if x <= 0:
         raise TypeError
     else:
        return m.pow(x, 2)


def rectangular_prism(x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    return 1

def rectangular_prism_surface_area(x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    return 1


def cone(radius, height, slant):
    radius = float(radius)
    height = float(height)
    slant = float(slant)
    return 1

def cone_surface_area(radius, height, slant):
    radius = float(radius)
    height = float(height)
    slant = float(slant)
    return 1


def pyramid(base, height, slant):
    base = float(base)
    height = float(height)
    slant = float(slant)
    return 1

def pyramid_surface_area(base, height, slant):
    base = float(base)
    height = float(height)
    slant = float(slant)
    return 1