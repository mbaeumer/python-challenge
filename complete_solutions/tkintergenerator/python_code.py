from tkinter import *
class Application(Frame):
  def __init__(self, master):
    super(Application, self).__init__(master)
    self.grid()

root = Tk()
root.title("GUI with OOP")
root.geometry("200x100")
root.mainloop()