from tkinter import*
import time
root=Tk()
root.title('Digital Clock')
root.geometry('1380x1080')
root.config(bg='orange')
#Function for Clock
def clock():
    h=str(time.strftime('%H'))
    m=str(time.strftime('%M'))
    s=str(time.strftime('%S'))
    #this if statement for when AM and When PM
    if int(h)>12 and int(m)>0:
        Lable_for_Noon.config(text='PM')
    #this if statement for convert 24 to 12
    if int(h)>12:
        h=str(int(h)-12)

    Lable_for_Hour.config(text=h)
    Lable_for_Min.config(text=m)
    Lable_for_Sec.config(text=s)

    Lable_for_Hour.after(200,clock)
#Lable for clock heading
Lable_for_heading=Label(root,text='Digital Clock',font=('times new roman',50,'bold'),bg='white',fg='red')
Lable_for_heading.place(x=330,y=100,width=700,height=70)
#Lable for Hour
Lable_for_Hour=Label(root,text='15',font=('times new roman',50,'bold'),bg='blue',fg='white')
Lable_for_Hour.place(x=350,y=200,width=150,height=150)

Lable_for_Hour1=Label(root,text='Hour',font=('times new roman',20,'bold'),bg='blue',fg='white')
Lable_for_Hour1.place(x=350,y=360,width=150,height=50)
#Lable for Minute
Lable_for_Min=Label(root,text='15',font=('times new roman',50,'bold'),bg='blue',fg='white')
Lable_for_Min.place(x=520,y=200,width=150,height=150)

Lable_for_Min1=Label(root,text='Minute',font=('times new roman',20,'bold'),bg='blue',fg='white')
Lable_for_Min1.place(x=520,y=360,width=150,height=50)
#Lable for Second
Lable_for_Sec=Label(root,text='15',font=('times new roman',50,'bold'),bg='red',fg='white')
Lable_for_Sec.place(x=690,y=200,width=150,height=150)

Lable_for_Sec1=Label(root,text='Second',font=('times new roman',20,'bold'),bg='red',fg='white')
Lable_for_Sec1.place(x=690,y=360,width=150,height=50)
#Lable for Noon
Lable_for_Noon=Label(root,text='AM',font=('times new roman',50,'bold'),bg='green',fg='white')
Lable_for_Noon.place(x=860,y=200,width=150,height=150)

Lable_for_Noon1=Label(root,text='Noon',font=('times new roman',20,'bold'),bg='green',fg='white')
Lable_for_Noon1.place(x=860,y=360,width=150,height=50)
clock()
root.mainloop()

#wow

