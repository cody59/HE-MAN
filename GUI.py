from tkinter import *


class GUI:

    def __init__(self, master):
        frame = Frame(master, width=500, height=500, bg="grey")
        frame.grid(rowspan=5, columnspan=5)

        self.chromeBtn = Button(frame, text="Chrome")
        self.firefoxBtn = Button(frame, text="Firefox")
        self.edgeBtn = Button(frame, text="Microsoft Edge")
        self.ieBtn = Button(frame, text="Internet Explorer")
        self.operaBtn = Button(frame, text="Opera")

        self.chromeBtn.grid(row=0, column=0, sticky=W)
        self.firefoxBtn.grid(row=1, sticky=W)
        self.edgeBtn.grid(row=2, sticky=W)
        self.ieBtn.grid(row=3, sticky=W)
        self.operaBtn.grid(row=4, sticky=W)

        self.quit = Button(frame, text="Quit", command=frame.quit)
        self.quit.grid(row=0, column=3, sticky=E)


def main():
    root = Tk()
    root.geometry('{}x{}'.format(500, 500))
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    b = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
