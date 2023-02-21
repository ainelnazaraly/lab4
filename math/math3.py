#Write a Python program to calculate the area of regular polygon.
import math
ns=int(input())
ls=int(input())
per=ns*ls
angle=360/(2*ns)
rad=angle/180*math.pi
ap=ls/(2*(1/math.tan(rad)))
area=(per*ap)/2
print(math.ceil(area))
