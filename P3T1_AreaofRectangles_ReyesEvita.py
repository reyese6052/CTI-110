#CTI-110
#P3T1 - Area of Rectangles
#Evita Reyes
#March 11, 2018
#
length1 = int(input('Enter the length of Rectangle 1: '))
width1 = int(input('Enter the width of Rectangle 1: '))

length2 = int(input('Enter the length of Rectangle 2: '))
width2 = int(input('Enter the width of Rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print ('Rectangle 1 has the greatest area.')
elif area2 > area1:
    print ('Rectangle 2 has the greatest area.')
else:
    print ('Both rectangles have the same area.')
    
