import LJParticle
from LJParticle import LJParticle

import pygame

import newtonconfig

o=10
c=4.3
def lennardJones(part1:LJParticle, part2:LJParticle,dt):
    rvec = part1.pos-part2.pos
    r=rvec.magnitude()
    f = (24*c*o**6*(r**6 - 2*o**6))/r**13 * dt
    part2.applyforce(rvec.normalize()*f)
    part1.applyforce(rvec.normalize()*-f)
    return f
