print('Enter your first number:')
num=input()
print('Enter your second number:')
num2=input()
try:
    print('num and num1 total value is:',int(num)+int(num2))
except Exception as string:
    print('This line is very important')