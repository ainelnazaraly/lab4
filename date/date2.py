#Write a Python program to print yesterday, today, tomorrow.
import datetime
x=datetime.datetime.now()
x1=x.day-1
x2=x.day+1
print(x1,x.day, x2 )