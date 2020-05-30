import pya

def create(lx, ly, ang, p, dc):
    """Create a square grating.

    lx:     length in x-direction
    ly:     length in y-direction
    ang:    rotation angle (degrees)
    p:      period of grating
    dc:     duty cycle of grating
    """
    
    reg = pya.Region()
    reg.insert(pya.Box(- lx / 2, - ly / 2, lx / 2, ly / 2))
    gbar = pya.Region()
    greps = int((lx) // p)
    for k in range(greps):
        gbar.insert(pya.Box(p * (k + dc / 2), - ly, p * (k + (1 - dc / 2)), ly))
        gbar.insert(pya.Box(p * (- k - dc / 2), - ly, p * (- k - (1 - dc / 2)), ly))
    gbar.transform(pya.ICplxTrans(1, ang, False, 0, 0))
    reg.__iand__(gbar)
    return reg