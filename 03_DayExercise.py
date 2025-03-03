print(True)
print(False)

# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8, it means 2 * 2 * 2

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

age = int(18)
height = float(1.83)
Triangle_area = complex(100 + 100j)


base=int (input('ingrese la base del triangulo'))
alto=int (input('Ingrese la altura del triangulo'))
area= float (base * alto * 0.5)
print('El area del triangulo es:', area)

lado1= int (input('ingrese el primer lado'))
lado2= int (input('ingrese el segundo lado'))
lado3= int (input('ingrese el tercer lado'))
perimetro= float (lado1 + lado2 + lado3)
print('El perimetro del triangulo es:', perimetro)

largo= int(input('ingrese el largo'))
ancho= int(input('ingrese el ancho'))
area2= float(largo + ancho)
perimetro2= float(area2 * 2)
print('El area del rectangulo es:', area2)
print('El perimetro del rectangulo es:', perimetro2)


pi= float(3.14)
radio= float(input('Ingrese el radio'))
area3= float(pi * radio * radio)
cir= float(2 * pi * radio)
print('El area del circulo es:', area3)
print('La circunferencia es:', cir)

X1= float(input('ingrese las coordenadas x del primer punto'))
X2= float(input('ingrese las coordenadas x del segundo punto'))
Y1= 2*X1-2
Y2= 2*X2-2
m= (Y2-Y1)/(X2-X1)
print('La pendiente es igual a:',m)

X1_2= float(input('ingrese las coordenadas x del primer punto'))
X2_2= float(input('ingrese las coordenadas x del segundo punto'))
Y1_2= float(input('ingrese las coordenadas y del primer punto'))
Y2_2= float(input('ingrese las coordenadas y del segundo punto'))
m_2= (Y2_2-Y1_2)/(X2_2-X1_2)
d= ((X2_2-X1_2)**2)+((Y2_2-Y1_2)**2)**0.5
print('La pendiente es igual a:',m_2)
print('La distancia euclidiana entre los dos puntos es:',d)

print('La pendiente del primer vector es:',m)
print('Mientras que el segundo es:',m_2)

x= float(input('Ingresa el valor de x'))
y = x**2 + (6*x) + 9
print('El valor de y es:',y)
print('y es igual a 0 cuando x es igual a -3')

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('There is no ON in both dragon and python')

print(str(float(len('python'))))

nn=(float(input('Ingrese su numero:')))
ss=float(nn)%2
if ss == 0: 
    print('El numero es par')
else:
    print('El numero es impar')
    
print(7//3 == 2.7)

print(type('10') == type(10))

print(int(9.8) == 10)
