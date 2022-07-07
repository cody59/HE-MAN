import os


class Initialize:

    def check(self):
        tki = os.popen("pip show tk").read()

        if not os.path.isdir(".\\log"):
            os.mkdir(".\\log")

        fwrite = open(".\\log\\tmp", "w")
        fwrite.write(tki)
        fwrite.write("\n")
        fwrite.close()

        fread = open(".\\log\\tmp", "r")
        if "tk" in fread.read():
            # dosnt mean anything placeholder
            flag = 1
        else:
            self.installtk()
        fread.close()
        os.remove(".\\log\\tmp")
        os.removedirs(".\\log")

    def installtk(self):
        os.system("pip install tk")

