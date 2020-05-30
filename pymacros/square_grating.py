import pya
import random
import sg

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw gratings")

ly = lv.active_cellview().layout()
cell = lv.active_cellview().cell
li = lv.current_layer.current().layer_index()
dbu = ly.dbu

grating_period = [p / dbu for p in [0.522, 0.525, 0.528, 0.531, 0.534, 0.537, 0.540]]
grating_dc = [0.785, 0.790, 0.795, 0.800, 0.805, 0.810, 0.815]
grating_width = 50 / dbu
grating_length = 50 / dbu
grating_reps = 120

grid_nx = len(grating_period)
grid_ny = len(grating_dc)
grid_dx = 80 / dbu
grid_dy = 80 / dbu

for i, gp in enumerate(grating_period):
    for j, gd in enumerate(grating_dc):
        x = grid_dx * j
        y = grid_dy * i
        grating = sg.create(grating_width, grating_length, 0, gp, gd)
        grating.transform(pya.Trans(0, False, x, y))
        cell.shapes(li).insert(grating)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()