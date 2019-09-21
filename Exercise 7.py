#VARIABLES
P = 10000;
r = 0.08;
n = 12;

#USER INPUT
t = int(input('Enter the amount of years the money will be compounded for: '));

#FORMULA
A = P * (1 + (r / n)) ** (n * t);

#PRINT
print('The compounded amound is $' + str(A));