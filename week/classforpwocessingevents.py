from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK= Button(winsow, text = "OK", fg = "red",
                     command = self.processOK)
        btCancel = Button(window, text = "cncel", bg = "yellow",
                          command = self.processCancel)
        btOK.pack()
        btCancel.pack()

        window.mainloop()
    def processOK(self):
        print("OK button is clicked")

    def processCancel(self):
        print("cancel button")