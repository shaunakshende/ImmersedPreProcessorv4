import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

h = 2.4/119.0;
padding_x = (1.8-1.2)/2.0
padding_z = 0.8-0.32;

# Lines for construction
C0=line(p0=(0.0, 0.0, 0), p1=(1.8, 0.0, 0))
C1=line(p0=(0.0, 1.8, 0), p1=(1.8, 1.8, 0))

# Call geometry generation functions for the background with optional argument n which indicates elevation of background elements
# n=1 for background quadratic, 2 for cubic

#background_with_uniform_refinement(C1, C2, t, num_div_vec, xyz, region_x, region_y, region_z, refinement_factor, n=1):
S = sf.background_with_uniform_refinement(C0, C1, 1.8, np.array([101, 101, 101]),O, np.array([0.7/1.8, 1.1/1.8]), np.array([0.7/1.8, 1.1/1.8]), np.array([0.5/1.8, 1.0/1.8]), 4);


#unif_linear_unif_BG_1D(S, X, ramp_factor, d, C1, C2, t,  hmin, hmax, side=-1, n=1):
S = sf.unif_linear_unif_BG_1D(S, 0.7/1.8, 0.050, 0, C0, C1, 1.8, 0.0045/1.8, 0.018/1.8, side=1);
S = sf.unif_linear_unif_BG_1D(S, 0.7/1.8, 0.050, 1, C0, C1, 1.8, 0.0045/1.8, 0.018/1.8, side=1);
S = sf.unif_linear_unif_BG_1D(S, 0.5/1.8, 0.050, 2, C0, C1, 1.8, 0.0045/1.8, 0.018/1.8, side=1);

S = sf.unif_linear_unif_BG_1D(S, 1.1/1.8, 0.050, 0, C0, C1, 1.8, 0.0045/1.8, 0.018/1.8, -1);
S = sf.unif_linear_unif_BG_1D(S, 1.1/1.8, 0.050, 1, C0, C1, 1.8, 0.0045/1.8, 0.018/1.8, -1);
S = sf.unif_linear_unif_BG_1D(S, 1.0/1.8, 0.050, 2, C0, C1, 1.8, 0.0045/1.8, 0.018/1.8, -1);


# Material 0 = Concrete
# G0 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.32]), np.array([150, 150, 40]), 0)
# G0 = sf.translate(G0, padding_x, padding_x, padding_z)
G0 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.32]), np.array([120, 120, 34]), 0)

#G0 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.32]), np.array([12, 12, 3]), 0)
G0 = sf.translate(G0, padding_x, padding_x, padding_z)

# # Charge - Material 1 - TNT charge
G1 = ms.generate_FGCone_cylindrical2(O, 0.103/2.0, 0.0085, 0.001, 0.075, [40, 200, 50], 1, 2, 1)
G1 = sf.translate(G1, 0.9, 0.9, 0.32+padding_z)

# # Material 2 : CompB (mix of RDX and TNT)
G2 = ms.generate_FGCone_cylindrical2(O, 0.113/2.0, 0.009325, 0.001, 0.08228, [44, 220, 55], 1, 2, 2)
G2 = ms.Conic_Mask2(G2, O, 0.075, 0.103/2.0, 0.0085, 2, 0)

G2 = sf.translate(G2, 0.9, 0.9, 0.32+padding_z)

#
G1 = sf.fg_superpose(G1, G2)
# #The Peridynamic solid has to be assembled last (input convention)
G1 = sf.fg_superpose(G1, G0)
# # Save geometry for visualization, and background as .dat files.

ms.save_geometry(G1, S, 880)
ms.save_PDGeometry(G1, 1, 'Block', "mmNS")
ms.vis_background()
