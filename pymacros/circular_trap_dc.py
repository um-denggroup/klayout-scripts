import pya
import random
import sg
import circ

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw circular trap")

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
grid_dx = 30 / dbu
grid_dy = 30 / dbu

d_o = [d / dbu for d in [18]]
d_i = [d / dbu for d in [6, 9, 12, 16]]
dc2 = [dc + m for m in [-0.02]]

for i, do in enumerate(d_o):
    for j, di in enumerate(d_i):
        for k, d2 in enumerate(dc2):
            trap = pya.Region()
            trap.insert(circ.create(di/2) & sg.create(di, di, 0, p, dc))
            trap.insert(circ.create_ring(do/2,di/2) & sg.create(do, do, 0, p, d2))
            trap.transform(pya.Trans(0, False, (k+i*len(dc2))*grid_dx , j*grid_dy))
            cell.shapes(li).insert(trap)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()