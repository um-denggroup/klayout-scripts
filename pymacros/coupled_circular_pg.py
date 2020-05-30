import pya
import random
import sg
import circ

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw coupled circular gratings")

ly = lv.active_cellview().layout()
cell = lv.active_cellview().cell
li = lv.current_layer.current().layer_index()
dbu = ly.dbu

grating_period = [p / dbu for p in [0.324, 0.330, 0.336, 0.342, 0.348]]
grating_dc = [0.62, 0.66, 0.70, 0.74, 0.78]
grating_length = 40 / dbu
grating_reps = 120

p = grating_period[2]
dc = grating_dc[1]

grid_nx = len(grating_period)
grid_ny = len(grating_dc)
grid_dx = 20 / dbu
grid_dy = 30 / dbu

circ_dia = [d / dbu for d in [4, 5, 6, 7, 8]]
circ_sep = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
pad = 2 / dbu

for i, d in enumerate(circ_dia):
    for j, s in enumerate(circ_sep):
        boundx = d
        boundy = d * (1 + s)
        grat = sg.create(boundx, boundy, 0, p, dc)
        gratp = sg.create(boundx+pad, boundy+pad, 90, p, dc)
        circ1 = circ.create(d/2)
        circ2 = circ.create(d/2)
        grat.transform(pya.Trans(0, False, i*grid_dx, j*grid_dy))
        gratp.transform(pya.Trans(0, False, i*grid_dx, j*grid_dy))
        circ1.transform(pya.Trans(0, False, i*grid_dx, j*grid_dy + d*s/2))
        circ2.transform(pya.Trans(0, False, i*grid_dx, j*grid_dy - d*s/2))
        ccg = ((circ1 + circ2) & grat) + (gratp - (circ1 + circ2))
        cell.shapes(li).insert(ccg)

lv.add_missing_layers()
lv.zoom_fit()
lv.commit()
