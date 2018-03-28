# CTI-110
# P4HW1: Distance Traveled
# Evita Reyes
# March 27, 2018
#
speed=float(input('What is the speed of the vehicle in miles per hour?'))
time=int(input('How many hours has it traveled?'))

print ('Hour','\t\t','Distance Traveled')
print ('------------------------------------')
for hour in range( 1, time + 1 ):
    distance=speed*hour
    print (hour, '\t\t',distance)
