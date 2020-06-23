put1=int(input('Enter your first number:'))
operator=input('Enter your operatior + - / *:')
put2=int(input('Enter your second number:'))
#for addition
if operator=='+':
    if put1==56 and put2==9:
        put3=77
        print('your total add is:',put3)
    else:
        print('Your total add is:',put1+put2)
else:
    pass
#for subtraction
if operator=='*':
    if put1==45 and put2==3:
        put3=555
        print('Your total multipluction is:',put3)
    else:
        print('your total multipluction is:',put1*put2)
else:
    pass
#for division
if operator=='/':
    if put1==56 and put2==6:
        put3=4
        print('Your division is:',put3)
    else:
        print('your total division is:',put1/put2)
else:
    pass



