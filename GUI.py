from tkinter import *
from initialize import *


class GUI:

    def __init__(self, master):
        frame = Frame(master, width=500, height=500, bg="grey")
        frame.grid(rowspan=5, columnspan=5)

        self.quit = Button(frame, text="Quit", command=frame.quit)
        self.quit.grid(row=0, column=3, sticky=E)


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
