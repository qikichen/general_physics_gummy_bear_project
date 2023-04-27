#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Physics Project:
    
    Use an iterative method to find a suitable number of gummy bears at which
    a person will survive a fall from a given height
    
    Assumptions made:
        Air resistance = 0 [Possible extensions that can be made]
        During impact, no air will replace the dent created by the fall
        Assume a cylindrical container in which the gummy bears are filled
        Gummy bears are fully molten and resolidified, no air in between the gummy bears
        Person falling is cuboid
        Specified Cylinder radius
        
        Here is my assumption:
            Gummy bear acts like an elastic object providing a resistive force
            Until maximum deformation, then it acts like a solid
            

- Qi Nohr/Mikolaj/Leonor/Hamza/Nick (12.04.2023)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

#STANDARD PHYSICAL CONSTANTS
GRAVITY = 9.8 #meter per second square

#ENVIRONMENT PARAMETER
HEIGHT = 35 #meters
CYLINDER_RADIUS = 2.5 #Meters

#GUMMYBEAR PARAMETERS
DENSITY_GUMMY_BEAR = 507.21 #kg/m^3
ELASTIC_MODULUS_GUMMY_BEAR = 70000 #Mega PAscla YM/ SURFACE AREA IS HOOKE'S LAW

#MASS PARAMETERS
GUMMYBEAR_MASS = 0.0029396 #kg
BODY_MASS = 70 #kg

#HUMAN BODY PARAMETERS
FEMUR_BREAKGE = 4649 #Newton FROM A PAPER

#EXTENSION PARAMATERS
DRAG_COEFFICIENT = 1.17 #dimensionless
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
    potential_e = BODY_MASS * GRAVITY * new_height
    air_res = DRAG_COEFFICIENT * FLUID_DENSITY * 0.657/2*new_height
    velocity = np.sqrt(potential_e/(BODY_MASS/2+air_res))
    return velocity

def velocity_no_air(new_height):
    return np.sqrt(2*GRAVITY*new_height)

def cylinder_volume(number_of_gummy):
    """
    Cylinder volume of the gummy bears after molten MASS OVER DENSITY
    """
    volume = (number_of_gummy*GUMMYBEAR_MASS)/(DENSITY_GUMMY_BEAR)
    return volume

def height_of_gummy_bear_molten(vol):
    """
    Returns the height of the molten gummy bear in the cylinder
    """
    height = vol/(np.pi*CYLINDER_RADIUS**2)
    return height    

def deceleration(distance, gummy_height):
    """
    Calculates deceleration [INCOMPLETE]
    """
    deceleration = (np.pi*CYLINDER_RADIUS**2*ELASTIC_MODULUS_GUMMY_BEAR*distance)/(gummy_height*BODY_MASS) - GRAVITY

    return  deceleration

def max_gummy_bear():
    max_num = 35*DENSITY_GUMMY_BEAR*np.pi*CYLINDER_RADIUS**2/GUMMYBEAR_MASS
    return max_num


def new_velocity(init_velocity, deceleration, time_span):
    """
    Calculates new velocity after each time frame
    """
    new_velocity = init_velocity + deceleration*time_span
    return new_velocity

def height_deformation(gummy_b_height):
    """
    Returns the maximum height of the deformation
    """
    deformation = np.sqrt((2*BODY_MASS*9.81*(HEIGHT-gummy_b_height)*gummy_b_height)/(ELASTIC_MODULUS_GUMMY_BEAR*np.pi*CYLINDER_RADIUS**2))
    return deformation

def distance_travelled(initial_velocity, acceleration, time):
    """
    """
    distance = initial_velocity * time + 0.5*acceleration*time**2
    return distance

def ode_distance_solution(time, gummy_b_height, initial_velocity):
    """
    as the gummy bear submerges, the ode solution will provide the distance it travels
    """
    omega = np.sqrt((np.pi*CYLINDER_RADIUS**2*ELASTIC_MODULUS_GUMMY_BEAR)/(gummy_b_height*BODY_MASS))
    distance_t = 1/omega*(initial_velocity-GRAVITY/omega)*np.sinh(omega*time) - GRAVITY/omega**2*(np.exp(-omega*time)-1)
    return distance_t
    
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
    

    plt.scatter(X,Y)
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
    initial_gummy_bear_number = 117500000 #Number of Gummy Bears
    print(max_gummy_bear())
    time = 0
    if (initial_gummy_bear_number >= max_gummy_bear()):
        return 0
    
    gummy_height = height_of_gummy_bear_molten(cylinder_volume(initial_gummy_bear_number))
    
    fall_height = HEIGHT - gummy_height
    print("THIS IS FALLHEIGHT")
    print(fall_height)
    initial_velocity= energy_to_velocity(fall_height)
    initial_momentum = momentum(initial_velocity)
    print("THE INITIAL MOMENTUM")
    print(initial_momentum)
    #Momenta after contact
    momenta_array = []
    velocity_array = []
    time_array = []
    force_array = []
    momenta_array.append(initial_momentum)
    velocity_array.append(initial_velocity)
    print("MAXIMUM DEFORMATION")
    print(height_deformation(gummy_height))

    
    #Algorithm : Numerical Iterative Method
    boolean_femur_break = False
    while(boolean_femur_break == False):
        time += 0.01
         # Initial Parameter for time
        distance = ode_distance_solution(time, gummy_height, initial_velocity)
        #decelaration_mass = deceleration(distance, gummy_height) # Remember to input something

        # Temporary variables added to the arrays
        #temp_velocity = new_velocity(initial_velocity,decelaration_mass, time)
        #temp_momentum = momentum(temp_velocity)
        #velocity_array.append(temp_velocity)
        #momenta_array.append(temp_momentum)

        # Calculate Force
        time_array.append(time)
        #print(temp_momentum)
        temp_momentum_rate = rate_of_change_momentum(initial_momentum, momenta_array[-1], time)
        force_array.append(temp_momentum_rate)
        
        # Distance travelled
        print("Distance Travelled")
        print(distance)

        if(height_deformation(gummy_height) <= distance): # I AM REALLY UNSURE ABOUT THIS - QIKI
            #THIS ONE SAYS IF THE MAXIMUM GUMMY DEFORMATION IS LESS THAN THE ACTUAL DEFORMED HEIGHT THEN THE FEMUR WILL BREAK
            print("THE FORCE IS")
            print(initial_momentum/time)
            boolean_femur_break = True
            

        #if(time >= 0.1):
            #boolean_femur_break = True
            
     
         
        
            
        
        

    return 0

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
 
gummy_height = height_of_gummy_bear_molten(cylinder_volume(10000000))
#print(gummy_height)
#print(height_deformation(gummy_height))

momentum_algorithm()
#plotting_2d(tim_arr, force_arr)




#momentum final iteratively calcualted DONE
#initial momentum calculated just before impact DONE
#rate of change of momentum calculated DONE

#TASKS: 
#   make an algorithm that decides whether it has reached the minimum number of gummy bears





