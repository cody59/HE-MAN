from tkinter import *
from initialize import *
from tkinter.messagebox import showinfo
from tkinter import filedialog


class GUI:

    def __init__(self, master):
        frame = Frame(master, width=500, height=500, bg="grey")
        frame.grid(rowspan=5, columnspan=5)

        self.ping = Button(frame, text="Net Sweep", command=lambda: self.netSweep())
        self.ping.grid(row=0, column=0, sticky=N)

        self.enum = Button(frame, text="Host Enumeration", command=lambda: self.hostenum())
        self.enum.grid(row=0, column=1, sticky=N)
        #executes everything vvv
        self.ult = Button(frame, text="Ultimate", command=lambda: self.popup(master, "hello"))
        self.ult.grid(row=0, column=2, sticky=N)

        self.quit = Button(frame, text="Quit", command=frame.quit)
        self.quit.grid(row=1, column=3, sticky=E)

    def popup(self, master, name):

        top = Toplevel(master)
        scroll = Scrollbar(top)
        scroll.grid(row=0, column=1, sticky=NS)
        top.geometry("640x550")
        top.title(name)

    def netSweep(self):
        print("netSweep")

    def ultimate(self):
        print("ultimate")

    def hostenum(self):
        print("hostenum")


def main():
    init = Initialize()
    init.check()

    root = Tk()
    root.geometry('{}x{}'.format(500, 500))
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    b = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
