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

grating_period = [p / dbu for p in [0.336]]
grating_dc = [0.6]
grating_length = 20 / dbu
grating_reps = 120

grid_nx = len(grating_period)
grid_ny = len(grating_dc)
grid_dx = 30 / dbu
grid_dy = 30 / dbu

for i, gp in enumerate(grating_period):
    for j, gd in enumerate(grating_dc):
        x = grid_dx * i
        y = grid_dy * j
        grating = sg.create(grating_length / 2, grating_length / 2, 0, gp, gd)
        grating.transform(pya.Trans(0, False, x + grating_length / 4, y + grating_length / 4))
        cell.shapes(li).insert(grating)
        grating = sg.create(grating_length / 2, grating_length / 2, 45, gp, gd)
        grating.transform(pya.Trans(0, False, x + grating_length / 4, y - grating_length / 4))
        cell.shapes(li).insert(grating)
        grating = sg.create(grating_length / 2, grating_length / 2, 90, gp, gd)
        grating.transform(pya.Trans(0, False, x - grating_length / 4, y - grating_length / 4))
        cell.shapes(li).insert(grating)
        grating = sg.create(grating_length / 2, grating_length / 2, 135, gp, gd)
        grating.transform(pya.Trans(0, False, x - grating_length / 4, y + grating_length / 4))
        cell.shapes(li).insert(grating)

for i, gp in enumerate(grating_period):
    for j, gd in enumerate(grating_dc):
        x = grid_dx * i + grid_dx
        y = grid_dy * j
        grating = sg.create(grating_length / 2, grating_length / 2, 0, gp, gd)
        grating.transform(pya.Trans(0, False, x + grating_length / 4, y + grating_length / 4))
        cell.shapes(li).insert(grating)
        grating = sg.create(grating_length / 2, grating_length / 2, 45, gp, gd)
        grating.transform(pya.Trans(0, False, x - grating_length / 4, y + grating_length / 4))
        cell.shapes(li).insert(grating)
        grating = sg.create(grating_length / 2, grating_length / 2, 90, gp, gd)
        grating.transform(pya.Trans(0, False, x - grating_length / 4, y - grating_length / 4))
        cell.shapes(li).insert(grating)
        grating = sg.create(grating_length / 2, grating_length / 2, 135, gp, gd)
        grating.transform(pya.Trans(0, False, x + grating_length / 4, y - grating_length / 4))
        cell.shapes(li).insert(grating)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()