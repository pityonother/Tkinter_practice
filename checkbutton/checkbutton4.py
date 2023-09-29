import tkinter
count=0
def on_click():
    global count
    if count==0:
        var1.set(1)
        var2.set(1)
        var3.set(1)
        var4.set(1)
        count=1
    else:
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)

root=tkinter.Tk()
var1=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()
var4=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(root,text="A",variable=var1)
checkbutton2=tkinter.Checkbutton(root,text="B",variable=var2)
checkbutton3=tkinter.Checkbutton(root,text="C",variable=var3)
checkbutton4=tkinter.Checkbutton(root,text="D",variable=var4)
button=tkinter.Button(root,text="全选/取消全选",command=on_click)
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
checkbutton4.pack()
button.pack()
root.mainloop()