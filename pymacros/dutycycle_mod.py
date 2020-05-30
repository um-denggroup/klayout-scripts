import pya
import random
from itertools import product
import dcc

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw duty cycle modulation")

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
dc_l = [dc]
dl = dc_l[0]
dc_h = [dl + m for m in [-0.01, -0.02, -0.03]]
len_h = [lh / dbu for lh in [0.5, 1, 1.5, 2]]
# len_l = [ll / dbu for ll in [6, 8]]
n = 2
for i, w in enumerate(wid):
    for j, dh in enumerate(dc_h):
        for k, lh in enumerate(len_h):
            # ll = w - lh*2
            ll = w - lh
            dc_chain = dcc.create(w, p, dh, dl, lh, ll, n)
            dc_chain.transform(pya.Trans(0, False, (i + j*len(wid))*grid_dx , k*grid_dy))
            cell.shapes(li).insert(dc_chain)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()