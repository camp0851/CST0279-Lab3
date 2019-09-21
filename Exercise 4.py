#GET INPUTS
startingDayNumber = int(input('What is the day you\'re leaving? '));
duration = int(input('How long will you be gone for? '));
startingDayPlusDuration = startingDayNumber + duration;

endingDayNumber = startingDayPlusDuration % 7

print('You will be returning on day ' + str(endingDayNumber));