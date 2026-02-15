# Q.1 Convert the time entered in hh,min and sec into seconds.
# Take input
time=int(input('Enter time :'))

#Convert time into HOURS
hours=int(time)
#print time in hours
print(f'Time in hours is {hours}.')

#Convert time into MINUTES
minutes=int((hours)*60)
#print time in minutes
print(f'Time in minutes is {minutes}.')

#Convert time into SECONDS
seconds=int((minutes)*60)
#Print time in seconds
print(f'Time in seconds is {seconds}.')