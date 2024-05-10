import models.lotkavolterra as lv
from models.agkb import AGKB
import tools.axis as ax
from tools.phase_diag import PhaseDiagram

xaxis = ax.Axis(0, 4, 15, "x")
yaxis = ax.Axis(-1, 4, 15, "y")
taxis = ax.Axis(0,4,100,"t")

# model = lv.LotkaVolterra(0.4, 0.2)
model = AGKB(1,1,1,1,1,1)

y0 = [1,1]
liste_cond_init = [y0]

PD = PhaseDiagram() 
PD.portrait(model, xaxis, yaxis, taxis, liste_cond_init)
