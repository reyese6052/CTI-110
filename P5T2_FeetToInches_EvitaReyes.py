# Convert feet to inches
# April 21, 2018
# CTI-110 P5T2_FeetToInches 
# Evita Reyes
#
CONVERSION_FACTOR = 12

def main():
    feet = float(input('Enter a number in feet.'))
    show_inches(feet)

def show_inches(ft):
    inches = ft * CONVERSION_FACTOR
    print (ft, 'feet equals', inches, 'inches.')

main()
