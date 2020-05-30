import numpy as np
import pya

def create(radius, npoints=32):
    """Create a circular-shaped region.

    radius:     radius of the circular area
    npoints:    the circular area is approximated by a polygon, hence the number of vertices
    """
    angles = np.linspace(0, 2*np.pi, num=npoints, endpoint=False)
    points = []
    for i, ang in enumerate(angles):
        points.append(pya.Point(radius*np.cos(ang), radius*np.sin(ang)))
    circle = pya.Region()
    circle.insert(pya.SimplePolygon(points))
    return circle

def create_ring(r1, r2, npoints=32):
    """Create a ring-shaped region.

    r1:         outer radius of the ring
    r2:         inner radius of the ring
    npoints:    the ring is approximated by a polygon, hence the number of vertices
    """
    ring = create(r1, npoints)
    center = create(r2, npoints)
    ring = ring - center
    return ring
