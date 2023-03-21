import mesh_functions as ms
import stretching_functions as sf
from igakit.cad import *
import numpy as np

# Specify origin
O=np.array([0,0,0])

# Lines for construction
C3=line(p0=(0.0,0.0,0), p1=(0.5,0.0,0))
C4=line(p0=(0.0,0.5,0), p1=(0.5, 0.5, 0))

# Call geometry generation functions for the background with optional argument n which indicates elevation of background elements
# n=1 for background quadratic, 2 for cubic

S=sf.cent_stretch_bg(C3, C4, 0, np.array([201, 201, 1]), np.array([0,0,0]), np.array([1.0,1.0,1.0]), n=1)

# Material 0 = currently dummy material
G0 = ms.generate_unif_foreground(O, np.array([0.05, 0.05, 0.0]), np.array([125, 125, 1]), 1)
G0 = ms.extract_circular_domain(G0, np.array([0,0.025,0]), 0.025)
G0 = sf.translate(G0, 0.0, 0.25-0.025, 0.0)

#The Peridynamic solid has to be assembled last (input convention)
ms.save_geometry(G0, S, 1)
ms.vis_background()
