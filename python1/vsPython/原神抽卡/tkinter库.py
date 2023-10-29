from tkinter import *

root = Tk()
root.title("botton组件")

def callback():
    print("我才不信")

frame1 = Frame(root)
frame2 = Frame(root)
var = StringVar()
var.set("请勿访问")
textlabel = Label(frame1,textvariable=var,justify=LEFT)
textlabel.pack(side = LEFT)


bottonlabel =Button(frame2,text = "已满18岁",command = callback)
bottonlabel.pack()
frame2.pack()
frame1.pack()
mainloop()

