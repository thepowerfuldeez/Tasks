import tkinter
from random import randint

def rand():
    print(randint(1,501))

window = tkinter.Tk()
window.title("GENERATING")
window.minsize(400,60)
button = tkinter.Button(window, text="GENERATE RANDINT", command=rand)
button.pack()
window.mainloop()