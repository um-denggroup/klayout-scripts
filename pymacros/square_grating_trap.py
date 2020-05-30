import pya
import random

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw gratings")

ly = lv.active_cellview().layout()
cell = lv.active_cellview().cell
li = lv.current_layer.current().layer_index()
dbu = ly.dbu

grating_period = [p / dbu for p in [0.336]]
grating_dc = [0.7]
grating_dc2 = [-0.03, -0.025, -0.02, -0.015, -0.01, -0.005, 0]
grating_rt = [r / dbu for r in [5, 7, 9, 11, 13, 15, 17]]
grating_length = 40 / dbu
grating_reps = 120

grid_nx = len(grating_period)
grid_ny = len(grating_dc)
grid_dx = 50 / dbu
grid_dy = 50 / dbu

gp = grating_period[0]
gd = grating_dc[0]
for i, gr in enumerate(grating_rt):
    for j, gd2 in enumerate(grating_dc2):
        x = grid_dx * i
        y = grid_dy * j
        boundary = pya.Region()
        outer_grating = pya.Region()
        inner_grating = pya.Region()
        boundary.insert(pya.Path([pya.Point(x, y + grating_length / 2)], gr * 2, gr, gr, True))
        for k in range(grating_reps):
            outer_grating.insert(pya.Box(x + gp * (k - grating_reps / 2), y,
                                         x + gp * (k - grating_reps / 2 + (1 - gd)), y + grating_length))
            inner_grating.insert(pya.Box(x + gp * (k - grating_reps / 2), y,
                                         x + gp * (k - grating_reps / 2 + (1 - gd - gd2)), y + grating_length))
        inner_grating.__iand__(boundary)
        outer_grating.__isub__( boundary)
        cell.shapes(li).insert(inner_grating)
        cell.shapes(li).insert(outer_grating)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()