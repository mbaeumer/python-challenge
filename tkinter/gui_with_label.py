from tkinter import *

root = Tk()

root.title("GUI with simple label")
root.geometry("200x100")

app = Frame(root)
app.grid()

label = Label(app, text="This is a label")
label.grid()

root.mainloop()