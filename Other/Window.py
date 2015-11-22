from tkinter import *


class FirstResult:
    def __init__(self, query):
        from pws import Google

        self.query = query
        self.result = Google.search(query, 1)

    def getname(self):
        return self.result["results"][0]["link_text"]

    def getlink(self):
        return self.result["results"][0]["link"]


class NewButton:
    def __init__(self, root, input_text, to_print):
        self.to_print = to_print
        Button(root, text=input_text, width=30, height=20, bg="white", fg="black", command=self.printer)\
            .pack(side ='bottom')

    def printer(self):
        print(self.to_print)


a = FirstResult("lolka")

root = Tk()
root.title("Текст первого запроса")
root.geometry('500x400+300+200')
root.resizable(False, False)
obj = NewButton(root, "Найти", a.getname())
root.mainloop()
