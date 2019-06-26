# -*- coding: utf-8 -*-
"""
Purpose: Visualizing Transverse Magnetic modes in a cylindrical waveguide
Author: Kurt Burdick
created: 3/6/2019
date modified: 6/26/19
"""

import numpy as np
import matplotlib.pyplot as plt

#define constants and waveguide size
E0 = 100
a = 10
b = 10
m = 25
n = 22
pi = np.pi

# Using linspace for grid
azimuths = np.radians(np.linspace(0, 360, 100))
zeniths = np.arange(0, 70, 10)

r, theta = np.meshgrid(zeniths, azimuths)

#E-Field equations
E_x = -100*(m*pi/a)*np.cos(m*pi*r/a)*np.sin(n*pi*r/b)
    
E_y = -100*(n*pi/b)*np.sin(m*pi*r/a)*np.cos(n*pi*r/b)

E_z = 100*(np.sin(m*pi*r/a)*np.sin(n*pi*r/b))
    
E_1 = (E_x*E_x + E_y*E_y + E_z*E_z)

#make plot
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, E_1, cmap='coolwarm_r')
plt.xlabel('-r, r')
plt.title('TM modes in a Cylindrical Waveguide')
plt.show()