import tkinter
root=tkinter.Tk()
canvas=tkinter.Canvas(root,bg='white',width=1024,height=512)
canvas.create_rectangle(10,10,110,110,fill='orange')
canvas.create_oval(70,60,120,150,fill='green')
canvas.pack()
tkinter.mainloop()