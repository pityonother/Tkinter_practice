import tkinter
def combine():
    if var1.get():
        var2.set(1)
    else:
        var2.set(0)

root=tkinter.Tk()
var1=tkinter.IntVar()
var2=tkinter.IntVar()
A=tkinter.Checkbutton(root,text='A',variable=var1,command=combine)
B=tkinter.Checkbutton(root,text='B',variable=var2)
A.pack()
B.pack()
root.mainloop()