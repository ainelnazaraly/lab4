#Write a Python program to subtract five days from current date.
import datetime 
x=datetime.datetime.now()
x2=x.day-5
print(datetime.date(x.year, x.month, x2))