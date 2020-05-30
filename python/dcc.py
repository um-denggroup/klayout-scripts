import pya
import sg

def create(w, p, dc1, dc2, len1, len2, n1, ps=0, ending=True):
    """Create a square grating with alternating duty cycle.

    w:      length in x-direction
    p:      period of grating
    dc1:    duty cycle 1
    dc2:    duty cycle 2
    len1:   length of each dc1 section
    len2:   length of each dc2 section
    n1:     number of dc1 & dc2 section pairs
    ps:     phase shift between sections of different duty cycle (0 to 1)
    ending: the grating ends with a dc1 section
    """
    dcc = pya.Region()
    for i in range(n1):
        dcc.insert(sg.create((w//p+0.5)*p, len1, 0, p, dc1).transform(
                   pya.Trans(0, False, 0, i*(len1+len2))))
        dcc.insert(sg.create((w//p+0.5)*p, len2, 0, p, dc2).transform(
                   pya.Trans(0, False, ps*p, (i+0.5)*(len1+len2))))
    if ending == True:
        dcc.insert(sg.create((w//p+0.5)*p, len1, 0, p, dc1).transform(
                pya.Trans(0, False, 0, n1*(len1+len2))))
        dcc.transform(pya.Trans(0, False, 0, -dcc.bbox().center().y))
    return dcc