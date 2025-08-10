import tkinter
import json

class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("User")
        self.geometry("400x400")
        self.entry1_var = tkinter.StringVar()
        self.entry2_var = tkinter.StringVar()
        self.radio_var = tkinter.StringVar(value="Light")
        self.check_value = tkinter.BooleanVar()
        self.slider_value = tkinter.IntVar(value=0)
        self.create_widget()

    def create_widget(self):
        name = tkinter.Label(self, text="Name", width=20, height=5)
        name.grid(row=0, column=0)

        age = tkinter.Label(self, text="Age", width=20, height=2)
        age.grid(row=1, column=0)

        entry_1 = tkinter.Entry(self, textvariable=self.entry1_var)
        entry_1.grid(row=0, column=1)

        entry_2 = tkinter.Entry(self, textvariable=self.entry2_var)
        entry_2.grid(row=1, column=1)

        theme = tkinter.Label(self, text="Preferred Theme", width=20, height=5)
        theme.grid(row=2, column=0)


        radio_1 = tkinter.Radiobutton(self, text="Light", variable=self.radio_var, value="Light")
        radio_1.grid(row=2, column=1)

        radio_2 = tkinter.Radiobutton(self, text="Dark", variable=self.radio_var, value="Dark")
        radio_2.grid(row=2, column=2)


        checkbox = tkinter.Checkbutton(self, text="Subscribe to Newsletter", variable=self.check_value)
        checkbox.grid(row=3, column=1)

        rate = tkinter.Label(self, text="Rate Us")
        rate.grid(row=4, column=0)


        slider = tkinter.Scale(self, from_=0, to=10, orient="horizontal", variable=self.slider_value)
        slider.grid(row=4, column=1)

        submit_button = tkinter.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=6, column=1)

    def submit(self, event=None):
        data = {
           "Name" : self.entry1_var.get(),
           "Age" : self.entry2_var.get(),
            "Theme" : self.radio_var.get(),
            "Subscribe ": self.check_value.get(),
           "Rating" : self.slider_value.get(),
        }

        with open("user.json", "w") as file:
            json.dump(data, file, indent=4)


app = Application()
app.mainloop()