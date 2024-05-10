import models.lotkavolterra as lv
import tools.axis as ax
from tools.phase_diag import PhaseDiagram

import matplotlib.pyplot as plt

xaxis = ax.Axis(0, 4, 15, "x")
yaxis = ax.Axis(-1, 4, 15, "y")

model = lv.LotkaVolterra(0.4, 0.2)


