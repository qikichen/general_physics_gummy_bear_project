#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
General Physics Project:
    
    Use an iterative method to find a suitable number of gummy bears at which
    a person will survive a fall from a given height

- Qi Nohr Chen (12.04.2023)
"""
import numpy as np
import matplotlib as plt

HEIGHT = 100 #meters
DENSITY_GUMMY_BEAR = 507.21 #kg/m^3
GRAVITY = 9.8 #meter per second square
FEMUR_BREAKGE = 3053 #Newton FROM A PAPER
CYLINDER_RADIUS = 2.5 #Meters
ELASTIC_MODULUS_GUMMY_BEAR = 0.07 #Mega PAscla
GUMMYBEAR_MASS = 0.0029396 #kg

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

def energy_to_velocity():
    """
    uses conservation of energy to calculate the veloctiy (THIS IGNORES AIR 
    RESISTANCE)
    """
    velocity = np.sqrt(2*GRAVITY*HEIGHT)
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


    

def _main_():
    #momentum final iteratively calcualted 
    #initial momentum calculated just before impact
    #rate of change of momentum calculated
    
    #SEE IF GITHUB WORKS
    
    

