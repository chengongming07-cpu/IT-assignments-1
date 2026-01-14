 #exercise 1:
name = input('what your name?')
print('hello ', name)

    #exercise 2:
radius = float(input('Enter the radius of the circle: '))
perimeter = 2 * 3.14 * radius
print('The perimeter of the circle is:', perimeter)
    
    #exercise 3:
length = float(input('Enter the length of the rectangle:'))
width = float(input('Enter the width of the rectangle:'))
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is:', area)
print('The perimeter of the rectangle is:', perimeter)
    
    #exercise 4:
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
sum = a + b + c
average = sum / 3
product = a * b * c
print('The sum is:', sum)
print('The average is:', average)
print('The product is:', product)
    
    #exercise 5:
talents = float(input('Enter your talents:'))
pounds = float(input('Enter pounds:'))
lots = float(input('Enter lots:'))
total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

    #exercise 6:
import random
code_3 = ""
for i in range(3):
    code_3 += str(random.randint(0, 9))
code_4 = ""
for i in range(4):
    code_4 += str(random.randint(1, 6))

print("3-digit code:", code_3)
print("4-digit code:", code_4)
