from tkinter import *


root = Tk()

root.title("GUI with simple button")
root.geometry("200x100")

app = Frame(root)
app.grid()

button = Button(app, text="This is a button")
button.grid()

root.mainloop()