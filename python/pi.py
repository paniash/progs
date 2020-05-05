# Code to calculate the value of pi using Wallis' method
ssum = 1
for i in range(1,10000):
    ssum = ssum*((4*i**2)/(4*i**2-1))
    

print("Pi:", 2*ssum) 
