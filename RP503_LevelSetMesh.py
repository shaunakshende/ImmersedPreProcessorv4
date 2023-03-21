import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

# Lines for construction
C0=line(p0=(0.0,0.0,0), p1=(0.31,0.0,0))
C1=line(p0=(0.0,0.31,0), p1=(0.31,0.31,0))

#background_with_uniform_refinement(C1, C2, t, num_div_vec, xyz, region_x, region_y, region_z, refinement_factor, n=1):
#S = sf.background_with_uniform_refinement(C0, C1, 1.0, np.array([267, 267, 267]),O, np.array([0.0, 0.3]), np.array([0.0, 0.30]), np.array([0.0, 0.30]), 20);
S = sf.cent_stretch_bg(C0, C1, 0.31, np.array([266, 266, 266]), np.array([0,0,0]), np.array([1.0,1.0,1.0]), n=1)

# #unif_linear_unif_BG_1D(S, X, ramp_factor, d, C1, C2, t,  hmin, hmax, side=-1, n=1):
#S = sf.unif_linear_unif_BG_1D(S, 0.3, 0.05, 0, C0, C1, 1.0, 0.001, 0.02, -1);
#S = sf.unif_linear_unif_BG_1D(S, 0.3, 0.05, 1, C0, C1, 1.0, 0.001, 0.02, -1);
#S = sf.unif_linear_unif_BG_1D(S, 0.3, 0.05, 2, C0, C1, 1.0, 0.001, 0.02, -1);

G1 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.16]), np.array([10, 10, 10]), 0)
# Save geometry for visualization, and background as .dat files.
ms.save_geometry(G1, S, 1)
ms.vis_background()
