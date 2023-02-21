#Implement a generator that returns all numbers from (n) down to 0.
def  ret(n): 
    for i in range(n, -1, -1): 
        yield i

n=int(input())
for i in ret(n): 
    print(i, end=", ")
    

