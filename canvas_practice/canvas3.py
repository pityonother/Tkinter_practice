import tkinter
def on_press(event):
    item=canvas.find_closest(event.x,event.y)
    if item:
        global selected_item
        selected_item=item[0]
def on_drag(event):
    if selected_item:
        dx=event.x-canvas.coords(selected_item)[0]
        dy= event.y-canvas.coords(selected_item)[1]
        canvas.move(selected_item,dx,dy)
def on_release(event):
    global selected_item
    selected_item=None

root=tkinter.Tk()
canvas=tkinter.Canvas(root,bg='orange',width=1024,height=512)
rectangle=canvas.create_rectangle(10,10,110,110,fill='green')
canvas.bind_all('<ButtonPress-1>',on_press)
canvas.bind_all('<B1-Motion>',on_drag)
canvas.bind_all('<ButtonRelease-1>',on_release)
canvas.pack()
root.mainloop()
