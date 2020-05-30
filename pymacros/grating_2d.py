import pya
import random

mw = pya.Application.instance().main_window()
lv = mw.current_view()
lv.transaction("Draw gratings")

ly = lv.active_cellview().layout()
cell = lv.active_cellview().cell
li = lv.current_layer.current().layer_index()
dbu = ly.dbu

grating_period = [p / dbu for p in [0.302, 0.306, 0.310, 0.314, 0.318, 0.322, 0.326]]
grating_dc = [0.61, 0.64, 0.67, 0.70, 0.73, 0.76, 0.79]
grating_length = 40 / dbu
grating_reps = 120

grid_nx = len(grating_period)
grid_ny = len(grating_dc)
grid_dx = 50 / dbu
grid_dy = 50 / dbu

for i, gp in enumerate(grating_period):
    for j, gd in enumerate(grating_dc):
        x = grid_dx * i
        y = grid_dy * j
        grid = pya.Region()
        island = pya.Region()
        grid.insert(pya.Box(x, y, x + gp * (grating_reps + (1 - gd)), y + gp * (grating_reps + (1 - gd))))
        for k in range(grating_reps): 
            for l in range(grating_reps):
                island.insert(pya.Box(x + gp * (k + (1 - gd)), y + gp * (l + (1 - gd)),
                                      x + gp * (k + 1), y + gp * (l + 1)))
        grid.__isub__(island)
        cell.shapes(li).insert(grid)


lv.add_missing_layers()
lv.zoom_fit()
lv.commit()