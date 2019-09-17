#GET INPUTS
currentHour = input('What hour is it right now? ')
currentHour = int(currentHour)
alarm =input('In how many hours do you want the alarm to go off? ')
alarm = int(alarm)

#
totalHours = alarm + currentHour
timeRemaining = totalHours % 24

#print('totalHours: ' + str(totalHours))
#print('hoursRemaining: ' + str(hoursRemaing))
print('The alarm will go off at ' + str(timeRemaining))