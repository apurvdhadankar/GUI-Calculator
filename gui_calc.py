from tkinter import * 


win = Tk()
win.geometry('354x465')
win.title('CALCULATOR')
win.config(bg='black')
winlabel = Label(win,text="CALCULATOR",fg='white',bg='black',font=("Courier New",30,'bold'))
winlabel.pack(side=TOP)

textin = StringVar()
operator = ""

def clickbut(numbers):  #lambda:clickbut(1)
    global operator
    operator=operator+str(numbers)
    textin.set(operator)
 
def equlbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''
def equlbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''
def equlbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''
def equlbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''

def clrbut():
    textin.set('')

wintext=Entry(win,font=("Courier New",17,'bold'),textvar=textin,fg='white',width=25,bd=5,bg='black')
wintext.pack()

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold',))
but1.place(x=10,y=100)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold',))
but1.place(x=10,y=170)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold',))
but1.place(x=10,y=240)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold',))
but1.place(x=75,y=100)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold',))
but1.place(x=75,y=170)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold',))
but1.place(x=75,y=240)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold',))
but1.place(x=140,y=100)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold',))
but1.place(x=140,y=170)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold',))
but1.place(x=140,y=240)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold',))
but1.place(x=10,y=310)

but1 = Button(win,padx=47,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut('.'),text=".",font=("Courier New",16,'bold',))
but1.place(x=75,y=310)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut("+"),text="+",font=("Courier New",16,'bold',))
but1.place(x=205,y=100)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut("-"),text="-",font=("Courier New",16,'bold',))
but1.place(x=205,y=170)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut("*"),text="*",font=("Courier New",16,'bold',))
but1.place(x=205,y=240)

but1 = Button(win,padx=14,pady=14,bd=4,fg='white',bg='black',command=lambda:clickbut("/"),text="/",font=("Courier New",16,'bold',))
but1.place(x=205,y=310)

but1 = Button(win,padx=14,pady=119,bd=4,fg='white',bg='black',command=clrbut,text="CE",font=("Courier New",16,'bold',))
but1.place(x=270,y=100)

but1 = Button(win,padx=151,pady=14,bd=4,fg='white',bg='black',command=equlbut,text="=",font=("Courier New",16,'bold',))
but1.place(x=10,y=380)

statusbar = Label(win, text="Python GUI Calculator", relief=SUNKEN, anchor=W,font=("Courier New",9,))
statusbar.pack(side=BOTTOM, fill=X)

win.mainloop()
