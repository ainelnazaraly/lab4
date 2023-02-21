#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def isEven(nums): 
    for i in range(nums+1): 
        if i%2==0: 
            yield i

n=int(input())
for i in isEven(n): 
    print(i)