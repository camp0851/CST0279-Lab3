#GET VARIABLES
miles = int(input('Enter the number of miles you drove: '));
gallon = int(input('Enter the amount of gas you used (in gallons): '));

#CALCULATE MPG
milesPerGallon = miles / gallon;

#PRINT MPG
print('Your MPG is: ' + str(milesPerGallon));