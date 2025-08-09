import tkinter

root = tkinter.Tk()

root.title("Entry Bind")
root.geometry("400x100")

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(value="Please enter any input...")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event):
    given_text = entry.get()
    user_input.set(given_text)


root.bind("<Return>", show_input)

root.mainloop()