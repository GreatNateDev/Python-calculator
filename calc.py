from tkinter import *
root = Tk()
root.title("calculator")
text= Entry(width=35,borderwidth=5)
text.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(num):
    cur = text.get()
    text.delete(0, END)
    text.insert(0,str(cur)+ str(num))
def cls():
    text.delete(0,END)
def add():
    firstnum = text.get()
    global fnum
    global math
    math = "add"
    fnum = int(firstnum)
    text.delete(0,END)
def equal():
    secondnum = text.get()
    text.delete(0,END)
    if math == "add":
        text.insert(0,fnum + int(secondnum))
    elif math == "sub":
        text.insert(0,fnum - int(secondnum))
    elif math == "multi":
        text.insert(0,fnum * int(secondnum))
    elif math == "div":
        text.insert(0,fnum / int(secondnum))
def subtract():
    firstnum = text.get()
    global fnum
    global math
    math = "sub"
    fnum = int(firstnum)
    text.delete(0,END)
def multiply():
    firstnum = text.get()
    global fnum
    global math
    math = "multi"
    fnum = int(firstnum)
    text.delete(0,END)
def divide():
    firstnum = text.get()
    global fnum
    global math
    math = "div"
    fnum = int(firstnum)
    text.delete(0,END)
button_9 = Button(text="9",padx=40,pady=20,command=lambda: click(9)).grid(row=1 ,column=2)
button_8 = Button(text="8",padx=40,pady=20,command=lambda: click(8)).grid(row=1 ,column=1)
button_7 = Button(text="7",padx=40,pady=20,command=lambda: click(7)).grid(row=1 ,column=0)
button_6 = Button(text="6",padx=40,pady=20,command=lambda: click(6)).grid(row=2 ,column=2)
button_5 = Button(text="5",padx=40,pady=20,command=lambda: click(5)).grid(row=2 ,column=1)
button_4 = Button(text="4",padx=40,pady=20,command=lambda: click(4)).grid(row=2 ,column=0)
button_3 = Button(text="3",padx=40,pady=20,command=lambda: click(3)).grid(row=3 ,column=2)
button_2 = Button(text="2",padx=40,pady=20,command=lambda: click(2)).grid(row=3 ,column=1)
button_1 = Button(text="1",padx=40,pady=20,command=lambda: click(1)).grid(row=3 ,column=0)
button_0 = Button(text="0",padx=40,pady=20,command=lambda: click(0)).grid(row=4 ,column=0)
button_clear = Button(text="Clear",padx=80,pady=20,command=lambda: cls()).grid(row=4 ,column=1, columnspan=2)
button_plus = Button(text="+",padx=40,pady=20,command=add).grid(row=5 ,column=0,)
button_equal = Button(text="=",padx=93,pady=20,command=equal).grid(row=5 ,column=1, columnspan=2)
button_subtract = Button(text="-",padx=42,pady=20,command=subtract).grid(row=6 ,column=0,)
button_multiply = Button(text="x",padx=41,pady=20,command=multiply).grid(row=6 ,column=1,)
button_divide = Button(text="/",padx=41,pady=20,command=divide).grid(row=6 ,column=2,)
root.mainloop()
