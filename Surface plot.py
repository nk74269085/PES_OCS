# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:24:34 2021

@author: Narayan Kundu
"""
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
d=np.loadtxt('ocs_anion_dft_opt_631g_a90-290.txt')
dist=set(np.array(d[:,1]))
theta=set(np.array(d[:,2]))
Energy=np.array(d[:,3])
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = sorted(list(dist))
Y = sorted(list(theta))
X, Y = np.meshgrid(X, Y)

#R = np.sqrt(X**2 + Y**2)
Z = Energy
Z = Z.reshape(X.shape)
print(X)
print(Y)
print(Z)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap='plasma')

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_xlabel('C-S distance(A$\degree$)')
ax.set_ylabel('O-C-S angle(degrees)')
ax.set_zlabel('Energy (au)')
#ax.set_title('OCS$^-$ PES plot')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
ax.set_zticklabels([])
plt.show()