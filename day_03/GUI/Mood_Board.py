import tkinter
from tkinter import mainloop

root = tkinter.Tk()

root.title("Mood Board")
root.geometry("400x100")

text_1 = ":) Happy"
text_2 = ":( Sad"

label_1 = tkinter.Label(root,
                        text=text_1,
                        fg="white",
                        bg="Green",
                        width=30,
                        height=100)
label_1.pack(side="left")

label_2 = tkinter.Label(root,
                        text=text_2,
                        fg="white",
                        bg="Blue",
                        width=70,
                        height=100)
label_2.pack(side="right")



root.mainloop()