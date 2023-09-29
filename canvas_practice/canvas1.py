#练习1：绘制基础图形
#创建一个Tkinter窗口和一个Canvas。
#在Canvas上绘制一个矩形、一个椭圆和一个多边形。
#练习2：动态移动图形
#创建一个Tkinter窗口和一个Canvas。
#在Canvas上绘制一个小矩形。
#使用键盘方向键来移动这个矩形。
#练习3：随机颜色和位置
#创建一个Tkinter窗口和一个Canvas。
#添加一个按钮，每当点击按钮时，Canvas上就随机生成一个颜色和位置都不同的矩形或圆形。
#练习4：画布上的连线
#创建一个Tkinter窗口和一个Canvas。
#当用户在Canvas上点击两次时，绘制一条连接两个点的直线。
#练习5：拖动图形
#创建一个Tkinter窗口和一个Canvas。
#在Canvas上绘制一个矩形。
#允许用户点击并拖动矩形到Canvas上的任何位置
import tkinter
import random
color=[
    'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta',
    'orange', 'brown', 'grey', 'pink', 'purple', 'violet',
    'gold', 'silver', 'darkred', 'darkgreen', 'darkblue',
    'lightblue', 'lightgreen', 'lightyellow']

def create_re():
    x1=random.randint(0, 1024)
    x2=random.randint(0, 1024)
    y1=random.randint(0,512)
    y2=random.randint(0,512)
    num=random.randint(0,21)
    canvas.create_rectangle(x1,y1,x2,y2,fill=color[num])
def create_ov():
    x1 = random.randint(0, 1024)
    x2 = random.randint(0, 1024)
    y1 = random.randint(0,512)
    y2 = random.randint(0,512)
    num = random.randint(0, 21)
    canvas.create_oval(x1, y1, x2, y2, fill=color[num])
def choice():
    para=random.randint(0,1)
    if para==0:
        create_re()
    else:
        create_ov()
root=tkinter.Tk()
canvas=tkinter.Canvas(root,bg='orange',width=1024,height=512)
button=tkinter.Button(root,text='random',command=choice)
canvas.pack()
button.pack()
root.mainloop()