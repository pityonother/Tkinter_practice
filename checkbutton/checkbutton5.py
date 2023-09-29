import tkinter
def create_checkbutton():
    var=tkinter.IntVar()
    checkbutton=tkinter.Checkbutton(root,text=text.get(),variable=var)
    checkbutton.pack()
root=tkinter.Tk()
text=tkinter.Entry(root)
button=tkinter.Button(root,text="创建选择",command=create_checkbutton)
text.pack()
button.pack()
root.mainloop()