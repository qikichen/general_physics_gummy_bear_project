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
        Gummy bears are fully molten, no air in between the gummy bears
        Person falling is cuboid

- Qi Nohr Chen (12.04.2023)
"""
import numpy as np
import matplotlib as plt

#STANDARD PHYSICAL CONSTANTS
GRAVITY = 9.8 #meter per second square

#ENVIRONMENT PARAMETER
HEIGHT = 100 #meters
CYLINDER_RADIUS = 2.5 #Meters

#GUMMYBEAR PARAMETERS
DENSITY_GUMMY_BEAR = 507.21 #kg/m^3
ELASTIC_MODULUS_GUMMY_BEAR = 0.07 #Mega PAscla

#MASS PARAMETERS
GUMMYBEAR_MASS = 0.0029396 #kg
BODY_MASS = 70 #kg

#HUMAN BODY PARAMETERS
FEMUR_BREAKGE = 3053 #Newton FROM A PAPER

def momentum(mass, velocity):
    """
    momentum calculations
    """
    momentum = mass * velocity
    return momentum

def rate_of_change_momentum(momentum_initial, momentum_final_, time):
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
    
    height = volume/(np.pi*CYLINDER_RADIUS**2)
    return height    

def deceleration():
    """
    Calculates deceleration [INCOMPLETE]
    """
    return 0 

def new_velocity(init_velocity, deceleration, time_span):
    """
    Calculates new velocity after each time frame
    """
    new_velocity = init_velocity + deceleration*time_span
    return new_velocity
    

def _main_():
    #Initial Parameters
    initial_gummy_bear_number = 100
    time = 0
    fall_height = HEIGHT-height_of_gummy_bear_molten(
        cylinder_volume(initial_gummy_bear_number))
    initial_momentum = energy_to_velocity(fall_height)*BODY_MASS
    
    #Momenta after contact
    momenta_after_contact = np.array([])
    velocity_after_contact = np.array([])
    
    #Algorithm
    boolean_femur_break = False
    while(boolean_femur_break == False):
        decelaration_mass = deceleration() # Remember to input something
        
    
    
    
    
    #momentum final iteratively calcualted 
    #initial momentum calculated just before impact
    #rate of change of momentum calculated
    
    
    
    

