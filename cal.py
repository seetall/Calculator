from _ast import Lambda
from ast import operator
from tkinter import *
root = Tk() 
root.config(bg="black")
text_Input=StringVar()
root.title ("Calculator")
e= Entry(root, width=50, borderwidth=8,bg="black",fg="white",textvariable=text_Input)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
operator=""

def button_click(number):
    global operator
    operator=operator+str(number) 
    text_Input.set(operator)

def button_clear():
    global operator
    operator=" "
    text_Input.set(" ")

def button_equal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=" "

button_1 = Button(root, text="1",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(1))
button_2 = Button(root, text="2",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(2))#command lambda 
button_3 = Button(root, text="3",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(3))
button_4 = Button(root, text="4",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(4))
button_5 = Button(root, text="5",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(5))
button_6 = Button(root, text="6",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(6))
button_7 = Button(root, text="7",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,bg="black",fg="white", command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=40, pady=20,bg="black",fg="white", command=lambda : button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,bg="black",fg="white", command=lambda: button_click(0))
but_add= Button(root, text="+", padx=38, pady=20,fg='black', bg='orange', command=lambda:button_click("+"))
but_sub = Button(root, text=' - ', padx=38, pady=20, fg='black', bg='orange',command=lambda: button_click(" - "))
but_mul = Button(root, text=' * ',padx=38, pady=20, fg='white', bg='orange',command=lambda:button_click("*") ) 
but_div = Button(root, text=' / ',padx=37, pady=20, fg='white', bg='orange', command=lambda: button_click("/") )
button_equal= Button(root, text="=", padx=150, pady=20,bg="black",fg="white", command=button_equal)
button_clear= Button(root, text="C",padx=40, pady=20,bg="black",fg="white", command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3. grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4,column=0)

but_add.grid(row=5,column=2)
but_mul.grid(row=4, column=1)
but_div.grid(row=4, column=2)
but_sub.grid(row=5, column=1)
button_equal.grid(row=6,column=0,columnspan=3)
button_clear.grid(row=5,column=0)
root.mainloop()

