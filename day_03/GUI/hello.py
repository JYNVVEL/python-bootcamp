import tkinter
from tkinter import font

root = tkinter.Tk()

root.title("Python Haiku")
root.geometry("400x200")

text_1 = "Hello World"
label_1 = tkinter.Label(root, text=text_1)
label_1.pack(side="left")

text_2 = """Loops within loops spin, 
A silent function returns, 
The logic is clear."""
label_2 = tkinter.Label(root,
                        text=text_2,
                        font=("Pro Medium", 14, "bold"),
                        fg="White",
                        bg="Grey",
                        width=50,
                        height=100)
label_2.pack(side="right")





all_fonts = font.families()
print(all_fonts)

root.mainloop()

