from tkinter import *
def click(event):
    global dkvalue
    text=event.widget.cget("text")
    print(text)
    if text== "=":
        if dkvalue.get().isdigit():
            value=int(dkvalue.get())
        else:
            try:
                value=eval(screen.get())
        
            except Exception as e:
                dkvalue.set("Syntax error")
                screen.update()
        dkvalue.set(value)
        screen.update()
        
    elif text=="C":
        dkvalue.set("")
        screen.update()
    else:
        dkvalue.set(dkvalue.get()+text)
        screen.update()
        


dk=Tk()
dk.geometry("700x600")
dk.title("cal by Dk")

dkvalue=StringVar()
dkvalue.set("")
screen=Entry(dk,textvar=dkvalue,font="bold 40 italic")
screen.pack(fill=X,ipadx=10,pady=10,padx=10)


f = Frame(dk,bg="black")
b = Button(f,text="9",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="8",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="7",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(dk,bg="black")
b = Button(f,text="6",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="5",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="4",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
f = Frame(dk,bg="black")
b = Button(f,text="3",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="2",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="1",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
f = Frame(dk,bg="black")
b = Button(f,text="0",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="+",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=12,pady=12)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="-",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=12,pady=12)
b.bind("<Button-1>",click)
f.pack()
f = Frame(dk,bg="black")
b = Button(f,text="/",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="%",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="*",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()
f = Frame(dk,bg="black")
b = Button(f,text="=",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=8,pady=8)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="C",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=6,pady=18)
b.bind("<Button-1>",click)
f.pack()
b = Button(f,text="on",font="lucida",bg="blue")
b.pack(side=RIGHT,padx=6,pady=8)
b.bind("<Button-1>",click)
f.pack()





dk.mainloop()