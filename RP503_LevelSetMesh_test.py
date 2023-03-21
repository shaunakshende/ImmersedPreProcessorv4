import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

# Lines for construction
L0 = 60.0*0.125/290.0;

C0=line(p0=(0.0,0.0,0), p1=(0.125,0.0,0))
C1=line(p0=(0.0,0.125,0), p1=(0.125,0.125,0))

S = sf.cent_stretch_bg(C0, C1, 0.125, np.array([291, 291, 291]), np.array([0,0,0]), np.array([1.0,1.0,1.0]), n=1)

G1 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.16]), np.array([10, 10, 10]), 0)
# Save geometry for visualization, and background as .dat files.
ms.save_geometry(G1, S, 1)
ms.vis_background()


#R0 discretization
# C0=line(p0=(0.0,0.0,0), p1=(L0,0.0,0))
# C1=line(p0=(0.0,L0,0), p1=(L0,L0,0))
#
# S = sf.cent_stretch_bg(C0, C1, L0, np.array([11, 11, 11]), np.array([0,0,0]), np.array([1.0,1.0,1.0]), n=1)
#
# G1 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.16]), np.array([10, 10, 10]), 0)
# # Save geometry for visualization, and background as .dat files.
# ms.save_geometry(G1, S, 1)
# ms.vis_background()
