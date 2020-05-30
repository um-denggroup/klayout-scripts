import pya
import random
from itertools import product
import dcc

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw phase shift")

ly = lv.active_cellview().layout()
cell = lv.active_cellview().cell
li = lv.current_layer.current().layer_index()
dbu = ly.dbu

grating_period = [p / dbu for p in [0.324, 0.330, 0.336, 0.342, 0.348]]
grating_dc = [0.62, 0.66, 0.70, 0.74, 0.78]

p = grating_period[2]
dc = grating_dc[1]

grid_nx = len(grating_period)
grid_ny = len(grating_dc)
grid_dx = 20 / dbu
grid_dy = 30 / dbu

wid = [w / dbu for w in [6, 8]]
pshift = [0.125, 0.25, 0.375, 0.5]
n = 1
for i, w in enumerate(wid):
    for j, ps in enumerate(pshift):
        dc_chain = dcc.create(w, p, dc, dc, w, w, n, ps, False)
        dc_chain.transform(pya.Trans(0, False, i*grid_dx , j*grid_dy))
        cell.shapes(li).insert(dc_chain)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()