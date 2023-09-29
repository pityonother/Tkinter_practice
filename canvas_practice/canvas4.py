import tkinter as tk

def move_rectangle(event):
    x, y = 0, 0
    if event.keysym == 'Up':
        x, y = 0, -10
    elif event.keysym == 'Down':
        x, y = 0, 10
    elif event.keysym == 'Left':
        x, y = -10, 0
    elif event.keysym == 'Right':
        x, y = 10, 0
    canvas.move(rectangle, x, y)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 创建一个矩形
rectangle = canvas.create_rectangle(50, 50, 100, 100, fill='blue')

# 绑定键盘事件
canvas.bind_all('<KeyPress>', move_rectangle)

root.mainloop()
