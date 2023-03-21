import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

padding = 1.0-0.305
h = (0.305+padding)/75.0
hf = (0.305+padding)/151.0
L = 0.305+padding
standoff = 0.075

# Lines for construction
C3=line(p0=(0.0,0.0,0), p1=(0.305+padding,0.0,0))
C4=line(p0=(0.0,0.305+padding,0), p1=(0.305+padding, 0.305+padding,0))

#background_with_uniform_refinement(C1, C2, t, num_div_vec, xyz, region_x, region_y, region_z, refinement_factor, n=1):
S = sf.background_with_uniform_refinement(C3, C4, 0.305+1.0*padding, np.array([25, 25, 25]),O, np.array([0.4, 0.6]), np.array([0.4, 0.6]), np.array([0.0, 0.2]), 1);

# #unif_linear_unif_BG_1D(S, X, ramp_factor, d, C1, C2, t,  hmin, hmax, side=-1, n=1):
# S = sf.unif_linear_unif_BG_1D(S, 0.4/1.0, 0.1, 0, C3, C4, 1.0, 0.00125/1.0, 0.0125/1.0, 1);
# S = sf.unif_linear_unif_BG_1D(S, 0.6/1.0, 0.1, 0, C3, C4, 1.0, 0.00125/1.0, 0.0125/1.0, -1);
#
# S = sf.unif_linear_unif_BG_1D(S, 0.4/1.0, 0.1, 1, C3, C4, 1.0, 0.00125/1.0, 0.0125/1.0,  1);
# S = sf.unif_linear_unif_BG_1D(S, 0.6/1.0, 0.1, 1, C3, C4, 1.0, 0.00125/1.0, 0.0125/1.0, -1);
#
#
# S = sf.unif_linear_unif_BG_1D(S, 0.2/1.0, 0.025, 2, C3, C4, 1.0, 0.00125/1.0, 0.0125/1.0, -1);

# #S = sf.linear_stretch_bg_one_sided(S, 0.4, 1.57, 0, C3, C4, 0.305+1.0*padding, -1);
#
# S = sf.linear_stretch_bg_one_sided(S, 0.2, 1.45, 2, C3, C4, 0.305+1.0*padding, 1);

# Plate (Homogenized Composite plate) - Material 0
G0 = ms.generate_unif_PDforeground(O, np.array([0.305, 0.305, 0.00126]), np.array([120, 120, 1]), 0)
G0 = sf.translate(G0, padding/2.0, padding/2.0, 0)
print(np.sum(G0.vols)-0.305*0.305*0.00126)

# Charge - Material 1 - RP-503 charge
# G1 = ms.generate_unif_foreground(O, np.array([0.0051*2.0, 0.0051*2.0, 0.004651320879015]), np.array([71, 71, 33]), 1)
# G1 = sf.translate(G1, 0.305/2.0-0.0051+padding/2.0, 0.305/2.0-0.0051+padding/2.0, 0.15-(0.004651320879015)/2.0) # 152 mm standoff distance
# G1 = ms.Cylinder_Mask(G1, np.array([L/2.0, L/2.0, 0]), 0.0049)
# vol = G1.vols;

#The Peridynamic solid has to be assembled last (input convention)

#G1 = sf.fg_superpose(G1, G0)

# Save geometry for visualization, and background as .dat files.
ms.save_geometry(G0, S, 94)

# save PD geometry : Foreground object, # processors, name, units (NMS = newton meter second)
ms.save_PDGeometry(G0, 1, 'Plate', "NMS")
ms.vis_background()
