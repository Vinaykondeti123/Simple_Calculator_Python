# simple calculator using conditional statements
a=float(input('Enter first Number: '))
b=float(input('Enter second Number: '))
operator=input('Enter operator: ')
if operator=='+':
   print(f'Addition: {a+b}')
elif operator=='-':
   print(f'Subtraction: {a-b}')
elif operator=='*':
   print(f'Multiplication: {a*b}')
elif operator=='/':
   print(f'Division: {a/b}')
elif operator=='%':
   print(f'Remainder: {a%b}')
else:
   print('Invalid operator')