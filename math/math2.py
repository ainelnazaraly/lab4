#Write a Python program to calculate the area of a trapezoid.
import math
height=int(input())
Base1=int(input())
base2=int(input())
def area(): 
    return ((Base1+base2)/2)*height

print(area())