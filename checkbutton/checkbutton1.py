import tkinter
def checked():
    if var1.get():
        label = tkinter.Label(root, text='The checkbutton is selected!')
        label.pack()
root=tkinter.Tk()
var1=tkinter.IntVar()
checkbutton=tkinter.Checkbutton(root,text="A CheckButton",bg='orange',command=checked,variable=var1)
checkbutton.pack()
root.mainloop()

#练习 1：基础复选框
#创建一个 Tkinter 程序，其中包含一个复选框和一个按钮。当点击按钮时，输出复选框是否被选中。
#
#练习 2：多个复选框
#创建一个 Tkinter 程序，其中包含三个复选框，分别标记为“苹果”，“香蕉”和“橙子”。还应有一个按钮，当点击该按钮时，输出用户选择的水果。
#
#练习 3：联动复选框
#创建一个 Tkinter 程序，其中包含两个复选框 A 和 B 以及一个标签。当 A 被选中时，复选框 B 也应自动被选中，并在标签上显示“联动激活”。如果取消选中 A，B 也应被取消选中。
#
#练习 4：全选 / 取消全选
#创建一个 Tkinter 程序，其中包含四个复选框和一个“全选/取消全选”按钮。点击这个按钮应选中或取消选中所有复选框。
#
#练习 5：动态添加复选框
#创建一个 Tkinter 程序，其中包含一个文本输入框和一个按钮。用户在文本框中输入文本（如“苹果”、“香蕉”等）并点击按钮，程序应动态地创建一个与该文本标签相对应的复选框。