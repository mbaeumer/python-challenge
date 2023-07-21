from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.button_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self)
        self.button["text"]="This is a button"
        self.button["command"] = self.update_click_count
        self.button.grid()

    def update_click_count(self):
        self.button_clicks += 1
        self.button["text"] = str(self.button_clicks)

root = Tk()
root.title("GUI with OOP")
root.geometry("200x100")
app = Application(root)

root.mainloop()