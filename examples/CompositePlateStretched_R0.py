import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

padding = 1.0-0.305
standoff = 0.075

# Lines for construction
C3=line(p0=(0.0,0.0,0), p1=(0.305+padding,0.0,0))
C4=line(p0=(0.0,0.305+padding,0), p1=(0.305+padding, 0.305+padding,0))

#background_with_uniform_refinement(C1, C2, t, num_div_vec, xyz, region_x, region_y, region_z, refinement_factor, n=1):
S = sf.background_with_uniform_refinement(C3, C4, 0.305+1.0*padding, np.array([51, 51, 51]),O, np.array([0.4, 0.6]), np.array([0.4, 0.6]), np.array([0.0, 0.2]), 1);

# Plate (Homogenized Composite plate) - Material 0
G0 = ms.generate_unif_PDforeground(O, np.array([0.305, 0.305, 0.00126]), np.array([120, 120, 1]), 0)
G0 = sf.translate(G0, padding/2.0, padding/2.0, 0)

# Save geometry for visualization, and background as .dat files.
ms.save_geometry(G0, S, 192)

# save PD geometry : Foreground object, # processors, name, units (NMS = newton meter second)
ms.save_PDGeometry(G0, 1, 'Plate', "NMS")
ms.vis_background()
