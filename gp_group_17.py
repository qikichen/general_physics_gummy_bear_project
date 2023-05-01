#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Physics Project:
    
    Use an iterative method to find a suitable number of gummy bears at which
    a person will survive a fall from a given height
    
    Assumptions made:
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
CYLINDER_RADIUS = 1.5 #Meters

#GUMMYBEAR PARAMETERS
DENSITY_GUMMY_BEAR = 507.21 #kg/m^3
ELASTIC_MODULUS_GUMMY_BEAR = 70000 #PAscla YM/ SURFACE AREA IS HOOKE'S LAW

#MASS PARAMETERS
GUMMYBEAR_MASS = 0.0029396 #kg
BODY_MASS = 70 #kg

#HUMAN BODY PARAMETERS
FEMUR_BREAKGE = 20000 #Newton FROM A PAPER

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
    distance_t = (1/omega)*(initial_velocity-GRAVITY/omega)*np.sinh(omega*time) - (GRAVITY/omega**2)*(np.exp(-omega*time)-1)
    return distance_t

def plotting_2d(X,Y): 
    plt.title("Number of Gummy Bears vs Log(Force)")
    plt.ylabel("Log(Force)")
    plt.xlabel("Number of Gummy Bears")
    plt.axhline(y = np.log(FEMUR_BREAKGE), c="red")
    plt.scatter(X,Y, c="black")
    plt.savefig("group_project_plot", DPI = 3000)
    plt.show()

#PHYSICS EXTENSIONS TO THIS PROBLEM


#ALGORITHMS

def momentum_algorithm(initial_gummy_bear_number):
    time = 0
    gummy_height = height_of_gummy_bear_molten(cylinder_volume(initial_gummy_bear_number))
    fall_height = HEIGHT - gummy_height
    initial_velocity= energy_to_velocity(fall_height)
    initial_momentum = momentum(initial_velocity)
    #Algorithm : Numerical Iterative Method
    boolean_femur_break = False
    while(boolean_femur_break == False):
        time += 0.001
         # Initial Parameter for time
        distance = ode_distance_solution(time, gummy_height, initial_velocity)
        if(height_deformation(gummy_height) <= distance): 
            force = initial_momentum/time
            return force
     
    return 0

def minimising_algorithm():
    """
    Minimising algorithm
    """

    g_number = 1000
    gummy_height = height_of_gummy_bear_molten(cylinder_volume(g_number))
    h_deform = height_deformation(gummy_height)
    gummy_height = height_of_gummy_bear_molten(cylinder_volume(g_number))

    if (g_number >= max_gummy_bear()):
        return 0 
    while (h_deform < gummy_height):
        g_number += 1000

    force_array = []
    raw_force_array = []
    number_array = []

    while (g_number < max_gummy_bear()-100000):
        raw_force = momentum_algorithm(g_number)
        force = np.log(raw_force)
        raw_force_array.append(raw_force)
        force_array.append(force)
        number_array.append(g_number)
        print(force)
        print(g_number)
        g_number += 100

    for i in range(len(raw_force_array)):
        if(raw_force_array[i] >= FEMUR_BREAKGE-0.2 and raw_force_array[i] <= FEMUR_BREAKGE+0.2):
            fall = HEIGHT - height_of_gummy_bear_molten(cylinder_volume(number_array[i]))
            print("THE NUMBER OF GUMMY BEARS TO SURVIVE A FALL:")
            print(number_array[i])
            print("THE FALL HEIGHT:")
            print(fall)
            print("NUMBER OF GUMMY BEAR PACKETS")
            number_packs = (0.0029396*number_array[i])/0.175
            print(number_packs)
            print("COST IN POUNDS")
            print(number_packs* 1.25)
    
    plotting_2d(number_array, force_array)
   
    return 0
 
minimising_algorithm()



