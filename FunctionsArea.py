import math as m


def circle(radius) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a circle
    :param radius: the user's circle radius
    :return: the area of the user's circle
    """
    radius = float(radius)
    if radius <= 0:
        raise ValueError
    else:
        return m.pi * m.pow(radius, 2)


def triangle(base, height) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a triangle
    :param base: the user's triangle base
    :param height: the user's triangle height
    :return: the area of the user's triangle
    """
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise ValueError
    else:
        return (0.5 * base) * height


def rectangle(x, y) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a rectangle
    :param x: the user's rectangle width
    :param y: the user's rectangle height
    :return: the area of the user's rectangle
    """
    x = float(x)
    y = float(y)
    if x <= 0 or y <= 0:
        raise ValueError
    else:
        return x * y


def square(x) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a square
    :param x: the user's square width
    :return: the area of the user's square
    """
    x = float(x)
    if x <= 0:
        raise ValueError
    else:
        return m.pow(x, 2)


def rectangular_prism(x, y, z) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a rectangular prism
    :param x: the user's rect. prism width
    :param y: the user's rect. prism length
    :param z: the user's rect. prism height
    :return: the area of the user's rectangular prism
    """
    x = float(x)
    y = float(y)
    z = float(z)
    if x <= 0 or y <= 0 or z <= 0:
        raise ValueError
    else:
        return x * y * z


def rectangular_prism_surface_area(x, y, z) -> float:
    """
    This function calculates the surface area of the user's shape
    if the user's shape is a rectangular prism
    :param x: the user's rect. prism width
    :param y: the user's rect. prism length
    :param z: the user's rect. prism height
    :return: the surface area of the user's rectangular prism
    """
    x = float(x)
    y = float(y)
    z = float(z)
    if x <= 0 or y <= 0 or z <= 0:
        raise ValueError
    else:
        return x * y * 4 + y * z * 2


def cone(radius, height, slant) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a cone
    :param radius: the user's cone radius
    :param height: the user's cone height
    :param slant: the user's cone slant height (unused here)
    :return: the area of the user's cone
    """
    radius = float(radius)
    height = float(height)
    if radius <= 0 or height <= 0:
        raise ValueError
    else:
        return (1/3) * m.pi * m.pow(radius, 2) * height


def cone_surface_area(radius, height, slant) -> float:
    """
    This function calculates the surface area of the user's shape
    if the user's shape is a cone
    :param radius: the user's cone radius
    :param height: the user's cone height
    :param slant: the user's cone slant height
    :return: the surface area of the user's cone
    """
    radius = float(radius)
    height = float(height)
    slant = float(slant)
    if radius <= 0 or height <= 0 or slant <= 0:
        raise ValueError
    else:
        return m.pi * m.pow(radius, 2) + m.pi * radius * slant


def pyramid(base, height, slant) -> float:
    """
    This function calculates the area of the user's shape
    if the user's shape is a pyramid
    :param base: the user's pyramid base length
    :param height: the user's pyramid height
    :param slant: the user's pyramid slant height (unused here)
    :return: the area of the user's pyramid
    """
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise ValueError
    else:
        return (1/3) * m.pow(base, 2) * height

def pyramid_surface_area(base, height, slant) -> float:
    """
    This function calculates the surface area of the user's shape
    if the user's shape is a pyramid
    :param base: the user's pyramid base length
    :param height: the user's pyramid height
    :param slant: the user's pyramid slant height
    :return: the surface area of the user's pyramid
    """
    base = float(base)
    height = float(height)
    slant = float(slant)
    if base <= 0 or height <= 0 or slant <= 0:
        raise ValueError
    else:
        return m.pow(base, 2) + 2 * base * slant