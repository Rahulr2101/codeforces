import math

x,y,z=list(map(float, input().split()))  
a = math.ceil(x/z)
b = math.ceil(y/z)
print(a*b)