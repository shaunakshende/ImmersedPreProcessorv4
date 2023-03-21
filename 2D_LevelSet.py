import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

# Lines for construction
<<<<<<< HEAD
C0=line(p0=(0.0,0.0,0), p1=(0.5,0.0,0))
C1=line(p0=(0.0,0.5,0), p1=(0.5, 0.5, 0))

# Call geometry generation functions for the background with optional argument n which indicates elevation of background elements
# n=1 for background quadratic, 2 for cubic
#S = sf.background_with_uniform_refinement(C0, C1, 0.0, np.array([76, 76, 1]),O, np.array([0.0,0.1/0.5]), np.array([(0.25-0.1)/0.5,(0.25+0.1)/0.5]), np.array([0, 0]), 4);
S=sf.cent_stretch_bg(C0, C1, 0, np.array([201, 201, 1]), np.array([0,0.25,0]), np.array([1.0,1.0,1.0]), n=1)

# S = sf.linear_stretch_bg_one_sided(S, 0.1, 1.15, 0, C0, C1, 0.0, 1);
# S = sf.linear_stretch_bg_one_sided(S, 0.15, 1.15, 1, C0, C1, 0.0, 1);
# S = sf.linear_stretch_bg_one_sided(S, 0.35, 1.15, 1, C0, C1, 0.0, -1);
#
=======
C3=line(p0=(0.0,0.0,0), p1=(0.5,0.0,0))
C4=line(p0=(0.0,0.5,0), p1=(0.5, 0.5, 0))

# Call geometry generation functions for the background with optional argument n which indicates elevation of background elements
# n=1 for background quadratic, 2 for cubic

S=sf.cent_stretch_bg(C3, C4, 0, np.array([150, 150, 1]), np.array([0,0,0]), np.array([1.0,1.0,1.0]), n=1)
>>>>>>> b939304c0a120585301d5074d26994e02fab1929

# Material 0 = currently dummy material
# G0 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.32]), np.array([150, 150, 40]), 0)
# G0 = sf.translate(G0, padding_x, padding_x, padding_z)
G0 = ms.generate_unif_PDforeground(O, np.array([1.2, 1.2, 0.32]), np.array([10, 10, 1]), 0)

#The Peridynamic solid has to be assembled last (input convention)
ms.save_geometry(G0, S, 1)
ms.vis_background()
