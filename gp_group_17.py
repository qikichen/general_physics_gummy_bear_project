#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Physics Project:
    
    Use an iterative method to find a suitable number of gummy bears at which
    a person will survive a fall from a given height
    
    Assumptions made:
        Air resistance = 0 [INITIALLY]
        During impact, no air will replace the dent created by the fall
        Assume a cylindrical container in which the gummy bears are filled
        Gummy bears are fully molten and resolidified, no air in between the gummy bears
        Person falling is cuboid
        Specified Cylinder radius

- Qi Nohr/Mikolaj/Leonor/Hamza/Nick (12.04.2023)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

#STANDARD PHYSICAL CONSTANTS
GRAVITY = 9.8 #meter per second square

#ENVIRONMENT PARAMETER
HEIGHT = 100 #meters
CYLINDER_RADIUS = 2.5 #Meters

#GUMMYBEAR PARAMETERS
DENSITY_GUMMY_BEAR = 507.21 #kg/m^3
ELASTIC_MODULUS_GUMMY_BEAR = 0.07 #Mega PAscla YM/ SURFACE AREA IS HOOKE'S LAW

#MASS PARAMETERS
GUMMYBEAR_MASS = 0.0029396 #kg
BODY_MASS = 70 #kg

#HUMAN BODY PARAMETERS
FEMUR_BREAKGE = 3053 #Newton FROM A PAPER

#EXTENSION PARAMATERS
DRAG_COEFFICIENT = 0 #dimensionless
FLUID_DENSITY = 1.2 #kg.m^-3 for air


def momentum(velocity):
    """
    momentum calculations
    """
    momentum = BODY_MASS * velocity
    return momentum

def rate_of_change_momentum(momentum_initial, momentum_final, time):
    """
    Rate of change of momentum used to calculate the fall 

    """
    rom = (momentum_final-momentum_initial)/time # Time of contact
    return rom

def energy_to_velocity(new_height):
    """
    uses conservation of energy to calculate the veloctiy (THIS IGNORES AIR 
    RESISTANCE)
    """
    velocity = np.sqrt(2*GRAVITY*new_height)
    return velocity

def cylinder_volume(number_of_gummy):
    """
    Cylinder volume of the gummy bears after molten MASS OVER DENSITY
    """
    volume = GUMMYBEAR_MASS/(number_of_gummy*DENSITY_GUMMY_BEAR)
    return volume

def height_of_gummy_bear_molten(vol):
    """
    Returns the height of the molten gummy bear in the cylinder
    """
    height = vol/(np.pi*CYLINDER_RADIUS**2)
    return height    

def deceleration():
    """
    Calculates deceleration [INCOMPLETE]
    """

    return 2 

def new_velocity(init_velocity, deceleration, time_span):
    """
    Calculates new velocity after each time frame
    """
    new_velocity = init_velocity + deceleration*time_span
    return new_velocity

def height_deformation(force, length, area, ym):
    """
    Returns the maximum height of the deformation
    """
    deformation = (force*length)/(area * ym)
    return 0

def plotting_3d(X,Y,Z): #MIKOLAJ DO THIS [Fix this for me please]

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
    # Customize the z axis.
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def plotting_2d(X,Y): # MIKOLAJ DO THIS

    plt.figure()
    plt.subplots(211)
    plt.plot(X,Y)
    plt.grid(True)
    plt.show()

#PHYSICS EXTENSIONS TO THIS PROBLEM

def drag_force(frontal_area, flow_velocity):
    """
    Calculates the drag force of a body falling through any medium (constant parameters are given above)
    """
    f_d = 1/2 * DRAG_COEFFICIENT * frontal_area* flow_velocity**2 *FLUID_DENSITY

    return f_d

#ALGORITHMS

def momentum_algorithm():
    initial_gummy_bear_number = 100 #Number of Gummy Bears
    time = 0
    
    gummy_height = height_of_gummy_bear_molten(cylinder_volume(initial_gummy_bear_number))
    fall_height = HEIGHT - gummy_height
    initial_velocity= energy_to_velocity(fall_height)
    initial_momentum = momentum(initial_velocity)
    
    #Momenta after contact
    momenta_array = np.array([])
    velocity_array = np.array([])
    time_array = np.array([])
    force_array = np.array([])
    np.insert(momenta_array, initial_momentum)
    np.insert(velocity_array, initial_velocity)

    
    #Algorithm : Numerical Iterative Method
    boolean_femur_break = False
    while(boolean_femur_break == False):
        time += 0.1
         # Initial Parameter for time
        decelaration_mass = deceleration() # Remember to input something

        # Temporary variables added to the arrays
        temp_velocity = new_velocity(decelaration_mass)
        temp_momentum = momentum(temp_velocity)
        np.insert(velocity_array, temp_velocity)
        np.insert(momenta_array, temp_momentum)

        # Calculate Force
        np.insert(time_array, time)
        temp_momentum_rate = rate_of_change_momentum(momenta_array[0], momenta_array[-1], time)
        np.insert(force_array, temp_momentum_rate)

        if(height_deformation >= gummy_height or temp_momentum*-1 >= FEMUR_BREAKGE ): # I AM REALLY UNSURE ABOUT THIS - QIKI
            #THIS ONE SAYS IF THE MAXIMUM GUMMY DEFORMATION IS LESS THAN THE ACTUAL DEFORMED HEIGHT THEN THE FEMUR WILL BREAK
            boolean_femur_break = True

        if(momenta_array[-1] < momenta_array[-2]):
            boolean_femur_break = True

    return momenta_array, velocity_array, time_array, force_array

def minimising_algorithm():
    """
    MIKOLAJ and Qiki: Work on deciding how to minimise the number of gummy bears such that we can automate the process!
    Current ideas:
        Hill climbing algorithm
        Derivatives? 

        Current algorithm idea (Hill Climbing inspired):
            Take the max/min of each force array and hill climb, if it is above the femur breakage, eg: then we need to lessen gummy bears
    """
    return 0
    



#momentum final iteratively calcualted DONE
#initial momentum calculated just before impact DONE
#rate of change of momentum calculated DONE

#TASKS: 
#   make an algorithm that decides whether it has reached the minimum number of gummy bears





