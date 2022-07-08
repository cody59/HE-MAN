
# this is just sample code to look at and or get code from

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog


class GUI:

    def __init__(self, master):

        ########change this value to file location########
        floc = "changeme.txt"
        ##################################################

        indicator_type = Label(text="input bad actors ips")
        indicator_type.grid(row=0, column=1, sticky=W, padx=20)

        exlabel = Label(text="ex: xxxxxx, xxxxxx, xxxxxx")
        exlabel.grid(row=1, column=1, sticky=W, padx=20)

        scroll = Scrollbar(master, orient='vertical')
        scroll.grid(row=2, column=2, sticky=NS)

        atxt = Text(master, width=90, height=30, yscrollcommand=scroll.set)
        scroll.config(command=atxt.yview)
        atxt.grid(row=2, column=1, pady=5, padx=20)

        appbtn = Button(master, text="Append", command=lambda: self.append(atxt, floc))
        appbtn.grid(row=3, column=1, sticky=SW, padx=20)

        readbtn = Button(master, text="Read", command=lambda: self.popup(master, floc))
        readbtn.grid(row=3, column=1, sticky=SW, padx=80)

        imfile = Button(master, text="Import File", command=lambda: self.importfile())
        imfile.grid(row=3, column=1, sticky=SW, padx=125)

    def append(self, atxt, floc):

        final = self.checkDuplicate(atxt, floc)

        #location of the file to update

        fa = open(floc, 'a')
        for lines in final:
            fa.write(lines + "\n")
        fa.close()

    def write(self, floc):

        #TODO make text editor pop up

        fw = open(floc, 'w')

    def readlines(self, floc):

        fin = open(floc, 'r')
        text = fin.readlines()
        fin.close()

        return text

    def read(self, floc):

        fin = open(floc, 'r')
        text = fin.read()
        fin.close()

        return text

    def popup(self, master, floc):

        text = self.readlines(floc)

        top = Toplevel(master)
        scroll = Scrollbar(top)
        scroll.grid(row=0, column=1, sticky=NS)
        top.geometry("640x550")
        top.title(floc)

        fread = Listbox(top, yscrollcommand=scroll.set, width=100, height=30)
        for line in text:
            fread.insert(END, str(line))
        fread.grid(row=0, column=0, padx=10, pady=10)
        scroll.config(command=fread.yview)

    def checkDuplicate(self, atxt, floc):

        text = atxt.get(1.0, END)
        x = text.split("\n")

        fread = self.readlines(floc)

        for line in range(len(x)):
            for i in fread:
                if i.strip("\n") == x[line].strip("\n"):

                    x[line] = "0"

        final = list(filter(lambda x: x != "0", x))

        #TODO check for duplicates in same list

        return final

    def importfile(self):
        # returns array

        fin = filedialog.askopenfile()
        finlist = fin.readlines()

        return finlist

    def format(self):

        #TODO formats text

        print("hi")


if __name__ == '__main__':

    master = Tk()
    master.title("Update Bad Actors")
    master.geometry('800x600')
    a = GUI(master)
    master.mainloop()