#Write a Python program to calculate two date difference in seconds.
import datetime 
x1=datetime.datetime(2022,3,21)
x2=datetime.datetime(2022,3,22)
d=x2-x1
print(d.total_seconds())
