from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.is_checked = BooleanVar()
        self.check_button = Checkbutton(self,
                                  text="this is a checkbox",
                                  variable=self.is_checked,
                                  command=self.handle_check)
        self.check_button.grid()
        self.label = Label(self)
        self.label["text"] = "This is a label"
        self.label.grid()

    def handle_check(self):
        self.label["text"]="Not checked"
        if self.is_checked.get():
            self.label["text"] = "Checked"


root = Tk()
root.title("GUI with checkbutton")
root.geometry("200x100")
app = Application(root)

root.mainloop()