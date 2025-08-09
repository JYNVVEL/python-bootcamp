import tkinter
from tkinter import messagebox
root = tkinter.Tk()

root.title("Entry Bind")
root.geometry("400x200")

label_1 = tkinter.Label(root, text="Enter your password: ")
label_1.pack()

entry = tkinter.Entry(root, show="*")
entry.pack()

label_2 = tkinter.StringVar()
label = tkinter.Label(root, textvariable=label_2)
label.pack()

password = "HelloWorld"

def show_input(event=None):
    user_input = entry.get()
    if user_input != password:
        label_2.set(value="Access Denied")
        messagebox.showerror("Error","This is an error message.")
    else:
        label_2.set(value="Access Granted")
        messagebox.showinfo("Access Granted","Access Granted")

button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()






root.bind("<Return>", show_input)

root.mainloop()