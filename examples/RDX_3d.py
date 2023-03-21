import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

# Lines for construction
C0=line(p0=(0.0,0.0,0), p1=(2.0,0.0,0))
C1=line(p0=(0.0,2.0,0), p1=(2.0,2.0,0))

#background_with_uniform_refinement(C1, C2, t, num_div_vec, xyz, region_x, region_y, region_z, refinement_factor, n=1):
S = sf.background_with_uniform_refinement(C0, C1, 2.0, np.array([51, 51, 51]),O, np.array([0.0, 1.3])/2.0, np.array([0.0, 1.3])/2.0, np.array([0.0, 1.30])/2.0, 6);
#S = sf.cent_stretch_bg(C0, C1, 0.150, np.array([194, 194, 194]), np.array([0,0,0]), np.array([1.0,1.0,1.0]), n=1)

# #unif_linear_unif_BG_1D(S, X, ramp_factor, d, C1, C2, t,  hmin, hmax, side=-1, n=1):
S = sf.unif_linear_unif_BG_1D(S, 1.3/2.0, 0.05, 0, C0, C1, 2.0, (2.0/300.0)/2.0, 0.04/2.0, -1);
S = sf.unif_linear_unif_BG_1D(S, 1.3/2.0, 0.05, 1, C0, C1, 2.0, (2.0/300.0)/2.0, 0.04/2.0, -1);
S = sf.unif_linear_unif_BG_1D(S, 1.3/2.0, 0.05, 2, C0, C1, 2.0, (2.0/300.0)/2.0, 0.04/2.0, -1);

G1 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.16]), np.array([10, 10, 10]), 0)
# Save geometry for visualization, and background as .dat files.
ms.save_geometry(G1, S, 1)
ms.vis_background()
