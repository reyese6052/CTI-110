#CTI-110
#P3HW2-Software Sales
#Evita Reyes
#March 11, 2018
#
pkg = int(input('Enter the number of packages purchased: '))
subtotal = pkg * 99
if pkg < 10:
    discount = 0
elif pkg >= 10 and pkg < 19:
    discount = 0.1
elif pkg >= 20 and pkg < 50:
    discount = 0.2
elif pkg >= 50 and pkg < 100:
    discount = 0.3
else:
    discount = 0.4

discountTotal = subtotal * discount
total = subtotal - discountTotal

print ('Your total discount comes to $', format(discountTotal,',.2f'))
print ('Your total purchase cost with discount applied comes to $', format(total,',.2f'))
