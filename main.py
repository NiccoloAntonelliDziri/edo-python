from models.lotkavolterra import LotkaVolterra
from models.agkb import AGKB
from tools.axis import Axis
from tools.phase_diag import PhaseDiagram
from tools.cond_init import Initials

xaxis = Axis(0, 4, 15, "x")
yaxis = Axis(0, 4, 15, "y")
taxis = Axis(0,50,500,"t")

# model = LotkaVolterra(0.4, 0.2)
model = AGKB(1,1,1,1,1,1)

# Conditions initiales
# paramètres : x, y, couleur, style
cond_init = Initials()
cond_init.append(1,1, 'red')
cond_init.append(1.5,1.5)
cond_init.append(2.5,3)
cond_init.append(3,2.5, 'green', 'dashed')
cond_init.append(1.2,3)

PD = PhaseDiagram(field_color = 'black') # On peut changer la couleur du champ de vecteur

# On peut automatiquement exporter le graphique en png avec exportpng = True
# On peut ne pas afficher le champ de vecteur avec show_field = False
# Le nom est le titre du graphique Phase Diagram, on peut le changer avec set_title ou
# directement en modifiant le titre dans le constructeur
PD.portrait(model, xaxis, yaxis, taxis, cond_init,
            show_field = True, normalize_arrows = False, exportpng = False)
