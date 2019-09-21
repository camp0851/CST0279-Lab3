#IMPORT
from math import pi;

#GET RADIUS
radius = int(input('Enter the radius of the circle: '));

#GET AREA
area = pi * radius ** 2;

#PRINT AREA TO SCREEN
area = str(area);
print('The area of the circle is ' + str(area));