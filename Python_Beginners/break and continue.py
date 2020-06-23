'''i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        break
    i=i+1'''
while(True):
    inp=int(input('Enter your number:'))
    if inp>100:
        print('Congrats...you Enter greater than 100')
        break
    else:
        print('Sorry try again!')
        continue