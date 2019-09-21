#GET INPUTS
currentHour = int(input('What hour is it right now? '));
alarm = int(input('In how many hours do you want the alarm to go off? '));

totalHours = alarm + currentHour;
timeRemaining = totalHours % 24;

#print('totalHours: ' + str(totalHours));
#print('hoursRemaining: ' + str(hoursRemaing));
print('The alarm will go off at ' + str(timeRemaining));