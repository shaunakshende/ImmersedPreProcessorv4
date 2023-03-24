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
S = sf.background_with_uniform_refinement(C3, C4, 0.305+1.0*padding, np.array([81, 81, 81]),O, np.array([0.4, 0.6]), np.array([0.4, 0.6]), np.array([0.0, 0.2]), 8);

#unif_linear_unif_BG_1D(S, X, ramp_factor, d, C1, C2, t,  hmin, hmax, side=-1, n=1):
S = sf.unif_linear_unif_BG_1D(S, 0.4/1.0, 0.05, 0, C3, C4, 1.0, 1.0/(80.0*8.0), 0.0125/1.0, 1);
S = sf.unif_linear_unif_BG_1D(S, 0.6/1.0, 0.05, 0, C3, C4, 1.0, 1.0/(80.0*8.0), 0.0125/1.0, -1);

S = sf.unif_linear_unif_BG_1D(S, 0.4/1.0, 0.05, 1, C3, C4, 1.0, 1.0/(80.0*8.0), 0.0125/1.0,  1);
S = sf.unif_linear_unif_BG_1D(S, 0.6/1.0, 0.05, 1, C3, C4, 1.0, 1.0/(80.0*8.0), 0.0125/1.0, -1);


S = sf.unif_linear_unif_BG_1D(S, 0.2/1.0, 0.05, 2, C3, C4, 1.0, 1.0/(80.0*8.0), 0.0125/1.0, -1);

# Plate (Homogenized Composite plate) - Material 0
G0 = ms.generate_unif_PDforeground(O, np.array([0.305, 0.305, 0.00126]), np.array([120, 120, 1]), 0)
G0 = sf.translate(G0, padding/2.0, padding/2.0, 0)

#The Peridynamic solid has to be assembled last (input convention)

# Save geometry for visualization, and background as .dat files.
ms.save_geometry(G0, S, 800)

# save PD geometry : Foreground object, # processors, name, units (NMS = newton meter second)
ms.save_PDGeometry(G0, 1, 'Plate', "NMS")
ms.vis_background()
