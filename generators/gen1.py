#Create a generator that generates the squares of numbers up to some number N.
def square(n): 
    for i in range(1, n+1): 
        yield i*i

n=int(input())

for i in  square(n): 
    print(i)