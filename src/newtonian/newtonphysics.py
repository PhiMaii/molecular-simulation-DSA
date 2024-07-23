import LJParticle
from LJParticle import LJParticle

import pygame

import newtonconfig

o=0.34
c=0.01

os = 0.34*10**-9
es = 0.01
def lennardJones(part1:LJParticle, part2:LJParticle,dt):
    rvec = part1.pos-part2.pos
    r=rvec.magnitude()
    e = 4*c*((o/r)**12-(o/r)**6)
    f = (24*c*o**6*(r**6 - 2*o**6))/r**13 * dt
    part2.applyforce(rvec.normalize()*f)
    part1.applyforce(rvec.normalize()*-f)
    return f


def getKineticEnergy(parts):
    eKin = 0
    for part in parts:
        eKin+= 0.5*part.vel.magnitude()**2*part.mass
    return eKin

def calculateTemperature(eKin, parts):
    T=(2*eKin)/(3*len(parts)*1.380*10**-23)
    return T