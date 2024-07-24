import LJParticle
from LJParticle import LJParticle

import pygame
import math

import config

o=0.34
eps=(0.0104*6.242*10**18)/(6.022*10**26)

def lennardJones(part1:LJParticle, part2:LJParticle,dt):
    rvec = part1.pos-part2.pos
    r=rvec.magnitude()
    e = 4*eps*((o/r)**12-(o/r)**6)
    f = (24*eps*o**6*(r**6 - 2*o**6))/r**13
    part2.applyforce(rvec.normalize()*f)
    part1.applyforce(rvec.normalize()*-f)
    return f


equilibrium_distance = 0.262     # r_e: nm
# well_depth = (0.342*6.242*10**18)/(6.022*10**26)               # D: eV
well_depth = 0.342               # D: eV
pot_width = 13.588               # a: nm

De = 0.342
a = 13.588
re = 0.262


def morsePotential(particle1:LJParticle, particle2: LJParticle, dt):
    rvec = particle1.pos - particle2.pos
    # r = rvec.magnitude()

    r = particle1.pos.distance_to(particle2.pos)

    # V'(R) = -2 a D e^(a (r - R)) * (1 - e^(a (r - R)))
    # f = -2 * pot_width * well_depth * math.e **(pot_width * (equilibrium_distance - dist)) * (1 - math.e **(pot_width * (equilibrium_distance - dist)))
    # print(f)
    f = -2 * De * a *(1-math.exp(-a * (r - re)) * math.exp(-a * (r - re)))
    particle2.applyforce(rvec.normalize() * -f)
    particle1.applyforce(rvec.normalize() * f)


def getKineticEnergy(parts):
    eKin = 0
    for part in parts:
        eKin+= part.ekin
    return eKin

def calculateTemperature(eKin, parts):
    T=(2 * eKin)/(3*len(parts)*1.380*10**-23)
    return T