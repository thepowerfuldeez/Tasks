from tkinter import *
from pws import Google


class FirstResult:
    def __init__(self, query):
        self.query = query
        self.result = Google.search(query, 1)

    def getname(self):
        print(self.result["results"][0]["link_text"])

    def getlink(self):
        return self.result["results"][0]["link"]


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("First token text")
        self.geometry("500x400+300+200")
        self.resizable(False, False)
        self.entry = Entry(self, width=50)
        searchengine = FirstResult("x")
        svar1 = StringVar()
        svar2 = StringVar()
        global temp
        temp = ["", ""]
        self.button = Button(self, text="Get", width=42, height=15, bg="white", fg="black", command=self.updatestatus)
        svar1.set(temp[0])
        svar2.set(temp[1])
        self.textlabel = Label(self, textvariable=svar1)
        self.linklabel = Label(self, textvariable=svar2)
        self.entry.pack()
        self.button.pack()
        self.linklabel.pack(side="bottom")
        self.textlabel.pack(side="bottom")

    def updatestatus(self):
        searchengine = FirstResult(self.entry.get())
        temp = searchengine.getname(), searchengine.getlink()

app = SampleApp()
app.mainloop()
