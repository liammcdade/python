import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

radians = float(input("enter the value in radians: ")) 
degrees = radians_to_degrees(radians)
print("Degrees: " , degrees)

