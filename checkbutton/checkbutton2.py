import tkinter
def apple():
    if var1.get():
        label=tkinter.Label(root,text='苹果')
        label.pack()
def banana():
    if var2.get():
        label=tkinter.Label(root,text='香蕉')
        label.pack()
def orange():
    if var3.get():
        label=tkinter.Label(root,text='橙子')
        label.pack()
def choice():
    if var1.get():
        apple()
    if var2.get():
        banana()
    if var3.get():
        orange()

root=tkinter.Tk()
var1=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()
checkbutton1=tkinter.Checkbutton(root,text="苹果",variable=var1)
checkbutton2=tkinter.Checkbutton(root,text="香蕉",variable=var2)
checkbutton3=tkinter.Checkbutton(root,text="橙子",variable=var3)
button=tkinter.Button(root,text="Chose your favourite fruit!",command=choice)
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
button.pack()
root.mainloop()

