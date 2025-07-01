import numpy as np
from numpy import sin, cos, atan2, sqrt 
import warnings
def cartesian_to_cylindrical(coords):
    """
    Following ISO 31-11 definition of rho, phi and z and https://en.wikipedia.org/wiki/Cylindrical_coordinate_system

    :param coord: cartesian coordinate 
    :type coord: tuple, list of numpy array of size 3
    :return: cylindrical coordinate
    :rtype: list
    """
    coords = np.asarray(coords)
    x, y, z = coords
    rho = sqrt(x**2 + y**2)
    if x == 0 and y == 0:
        warnings.warn("phi is indeterminate with x == 0 and y == 0")
        return [rho, 0, z]
    else:
        return [rho, atan2(y,x), z]
    
# Aliases
cart2cyl = cartesian_to_cylindrical

def cylindrical_to_cartesian(coords):
    """
    Following ISO 31-11 definition of rho, phi and z and https://en.wikipedia.org/wiki/Cylindrical_coordinate_system

    :param coord: cylindrical coordinate 
    :type coord: tuple, list of numpy array of size 3
    :return: cartesian coordinate
    :rtype: list
    """
    coords = np.asarray(coords)
    rho, phi, z = coords

    return [rho*cos(phi), rho*sin(phi), z]

# Aliases
cyl2cart = cylindrical_to_cartesian

def spherical_to_cartesian(coords):
    """
    Following ISO 31-11 definition of r, theta and phi and https://en.wikipedia.org/wiki/Spherical_coordinate_system

    :param coord: spherical coordinate 
    :type coord: tuple, list of numpy array of size 3
    :return: cartesian coordinate
    :rtype: list
    """
    coords = np.asarray(coords)
    r, theta, phi = coords
    return [r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta)]

# Aliases
spher2cart = spherical_to_cartesian

def cartesian_to_spherical(coords):
    """
    Following ISO 31-11 definition of r, theta and phi and https://en.wikipedia.org/wiki/Spherical_coordinate_system

    :param coord: cartesian coordinate 
    :type coord: tuple, list of numpy array of size 3
    :return: spherical coordinate
    :rtype: list
    """
    coords = np.asarray(coords)
    x, y, z = coords

    r = sqrt(x**2+y**2+z**2)
    theta = atan2(sqrt(x**2+y**2),z)
    phi = atan2(y,x)
    return [r,theta,phi]

# Aliases
cart2spher = cartesian_to_spherical

def spherical_to_cylindrical(coords):
    coords = np.asarray(coords)
    r, theta, phi = coords
    """
    Following ISO 31-11 definition of r, theta and phi and rho, phi, z

    :param coord: spherical coordinate 
    :type coord: tuple, list of numpy array of size 3
    :return: cylindrical coordinate
    :rtype: list
    """
    rho = r*sin(theta)
    z = r*cos(theta)
    return [rho, phi, z]

# Aliases
spher2cyl = spherical_to_cylindrical

def cylindrical_to_spherical(coords):
    coords = np.asarray(coords)
    rho, phi, z = coords
    """
    Following ISO 31-11 definition of r, theta and phi and rho, phi, z

    :param coord: cylindrical coordinate with :math:`rho, phi [rad], z`.

    :type coord: tuple, list of numpy array of size 3
    :return: spherical coordinate with :math:`r \in [0, \inf), theta \in [0, \pi], \phi \in [0, 2\pi),`
    :rtype: list
    """
    ## 
    coords = np.asarray(coords)
    rho, phi, z = coords

    r = sqrt(rho**2+z**2)
    theta = atan2(rho,z)
    phi = atan2(rho*sin(phi),rho*cos(phi))
    return [r,theta,phi]

# Aliases
cyl2spher = cylindrical_to_spherical
