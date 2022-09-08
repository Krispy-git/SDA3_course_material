from tkinter import *

root = Tk()
canvas = Canvas()


root.geometry("350x500")

root.title("Tkinter Demo")

var = StringVar()
label = Message(root, textvariable=var, width=200)
var.set("This is some text")
label.pack(pady=20)

canvas.create_oval(10, 10, 80, 80, outline = "black", fill = "red",width = 2)
canvas.create_oval(150, 10, 220, 80, outline = "black", fill = "red",width = 2)
canvas.create_oval(80, 10, 150, 80, outline = "black", fill = "white",width = 2)

canvas.create_rectangle(10, 90, 80, 160, outline = "black", fill = "red",width = 2)
canvas.create_rectangle(150, 90, 220, 160, outline = "black", fill = "red",width = 2)
canvas.create_rectangle(80, 90, 150, 160, outline = "black", fill = "white",width = 2)
canvas.pack()

Button(root, text= "Exit", command=root.quit).pack(pady=20)

root.mainloop()