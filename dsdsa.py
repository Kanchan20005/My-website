#
#  Template_Generate_Plot_Normal_Distribution.py
#
#  This file is used to test the randn function
#  and the ability to make a histogram.
#
#  For this version we specify the histogram bins
#
#  Adapted from the example at:
#
#  http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.norm.html
#
#  By:
#  Ernest R. Behringer
#  Department of Physics and Astronomy
#  Eastern Michigan University
#  Ypsilanti, MI  48197
#  (734) 487-8799 (Office)
#  ebehringe@emich.edu
#
#  Last updated:
#
#  20160629 ERB
#

from pylab import figure,xlim,xlabel,ylim,ylabel,grid,title,show,hist
from numpy import random,linspace

# Uncomment the following line and lines below if you want to fit the distribution
#import matplotlib.mlab as mlab

#  Initialize parameter values 
q = 1.60e-19 # particle charge [C]
m = 7.0*1.67e-27 # particle mass [kg]
Ex = 0.0 # Ex = electric field in the +x direction [N/C]
Ey = -105.0 #  Ey = electric field in the +y direction [N/C]
Ez = 0.0 # Ez = electric field in the +z direction [N/C]
Bx = 0.002 # Bx = magnetic field in the +x direction [T]
By = 0.0 # By = magnetic field in the +x direction [T]
Bz = 0.0 # Bz = magnetic field in the +x direction [T]
Ntraj = 1000 # number of trajectories

# Derived quantities
qoverm = q/m # charge to mass ratio [C/kg]
vzpass = -Ey/Bx #  z-velocity for zero deflection [m/s]

# Set up the array of velocities and scaled velocities
mean = vzpass # the mean of the velocity distribution is vzpass
sigma = 0.1*vzpass # the width of the velocity distribution is 0.1*vzpass
vz = mean + sigma*random.randn(Ntraj) # the set of initial velocity magnitudes
scaled_vz = vz/vzpass # scale the z-velocities by the pass velocity
scaled_bins = linspace(0.5,1.5,11) # set the bin edges of the scaled z-velocity
bins = vzpass*scaled_bins # set the bin edges for the z-velocity [m/s]


# Start a new figure
figure()

# the histogram of the data
n, bins, patches = hist(vz, bins, normed=0, facecolor='orange', alpha=0.75)


# Uncomment this block if you want to fit the distribution
## add a 'best fit' line
#y = mlab.normpdf( bins, mean, sigma)
#l = plot(bins, y, 'm--', linewidth=1)

# Set the horizontal axis limits
xlim(0.5*vzpass,1.5*vzpass)

# Label the horizontal axis
xlabel('$v_z$ [m/s]',size=16)

# Set the vertical axis limits
ylim(0,0.5*Ntraj)

# Label the vertical axis
ylabel('$N$',size=16)

# Make a title
title('Histogram of initial $v_z$')

# Draw a grid
grid(True)

# Show the plot
show()


# Start a new figure
figure()

# the histogram of the scaled data
n, bins, patches = hist(scaled_vz, scaled_bins, normed=0, facecolor='orange', alpha=0.75)


# Uncomment this block if you want to fit the distribution
## add a 'best fit' line
#y = mlab.normpdf( bins, mean, sigma)
#l = plot(bins, y, 'm--', linewidth=1)

# Set the horizontal axis limits
xlim(0.5,1.5)

# Label the horizontal axis
xlabel('$v_z/v_{z,pass}$',size=16)

# Set the vertical axis limits
ylim(0,0.5*Ntraj)

# Label the vertical axis
ylabel('$N$',size=16)

# Make a title
title('Histogram of initial $v_z/v_{z,pass}$')

# Draw a grid
grid(True)

# Show the plot
show()