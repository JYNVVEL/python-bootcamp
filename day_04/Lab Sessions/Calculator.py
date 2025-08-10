import tkinter
import tkinter as tk


class CalculatorApp:
    """
    A simple calculator GUI using Tkinter.

    Features:
    - Supports basic arithmetic: +, -, *, /
    - Has "Clear" and "=" functions
    - Uses `eval()` to evaluate expressions (safe for this simple case)
    """

    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Simple Calculator")

        # Holds the current expression as a string
        self.expression: str = ""

        # Create the display label
        self.display = tk.Label(
            self.window,
            text="",
            anchor="e",
            bg="white",
            fg="black",
            height=8,
            width=25,
            font=("Arial", 18)
        )
        self.display.grid(row=0, column=0, columnspan=4)

        # TODO: Call a method to create all the buttons
        self.setup_buttons()

    def press(self, value: str) -> None:
        """
        Appends a digit or operator to the current expression and updates the display.

        Args:
            value: The value of the button pressed (e.g., "1", "+", etc.)
        """

        self.expression += value
        self.update_display()

    def clear(self) -> None:
        """
        Clears the current expression.
        """

        self.expression = ""
        self.update_display()

    def calculate(self) -> None:
        """
        Evaluates the current expression using eval() and updates the display with the result.

        If evaluation fails, displays "Error".
        """

        try:
            result = eval(self.expression)  # ⚠️ okay for this toy project
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self.update_display()

    def update_display(self) -> None:
        """
        Updates the label to show the current expression.
        """

        self.display.config(text=self.expression)

    def make_button(self, text: str, row: int, column: int) -> None:
        """
        Creates a single button and places it in the grid.

        Args:
            text: The label of the button.
            row: The row in the grid.
            column: The column in the grid.
        """
        if text in ('+','-','*','/','0','1','2','3','4','5','6','7','8','9'):
            button = tkinter.Button(self.window, text=text, command=lambda: self.press(text))
            button.grid(row=row,column=column)
        elif text == 'C':
            button = tkinter.Button(self.window, text=text, command=self.clear)
            button.grid(row=row, column=column)
            print("1")
        elif text == '=':
            button = tkinter.Button(self.window, text=text, command=self.calculate)
            button.grid(row=row, column=column)
            print("2")


        # TODO: Bind the correct command based on the button type
        pass

    def setup_buttons(self) -> None:
        """
        Creates and places all calculator buttons.
        You may use `make_button` to avoid repeating code.

        Recommended layout:
            7 | 8 | 9 | /
            4 | 5 | 6 | *
            1 | 2 | 3 | -
            0 | C | = | +
        """
        self.make_button("7",0,0)
        self.make_button("8",0,1)
        self.make_button("9",0,2)
        self.make_button("/", 0, 3)

        self.make_button("4", 1, 0)
        self.make_button("5", 1, 1)
        self.make_button("6", 1, 2)
        self.make_button("*", 1, 3)

        self.make_button("1", 2, 0)
        self.make_button("2", 2, 1)
        self.make_button("3", 2, 2)
        self.make_button("-", 2, 3)

        self.make_button("0", 3, 0)
        self.make_button("C", 3, 1)
        self.make_button("=", 3, 2)
        self.make_button("+", 3, 3)

        # TODO: Call make_button(...) multiple times to create the layout
        pass

    def run(self) -> None:
        """
        Starts the main event loop for the app.
        """
        self.window.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
