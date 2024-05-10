import models.lotkavolterra as lv
import tools.axis as ax
from tools.phase_diag import PhaseDiagram
from tools.field import Field

import matplotlib.pyplot as plt

xaxis = ax.Axis(0, 4, 15, "x")
yaxis = ax.Axis(-1, 4, 15, "y")
taxis = ax.Axis(0,0,0,"t")

model = lv.LotkaVolterra(0.4, 0.2)

Field().plot(model, xaxis, yaxis)

