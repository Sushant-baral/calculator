import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._save_history(a, '+', b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history(a, '-', b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history(a, '*', b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._save_history(a, '/', b, result)
        return result

    def percentage(self, a):
        return a / 100

    def _save_history(self, a, op, b, result):
        self.history.append(f"{a} {op} {b} = {result}")

    def get_history(self):
        return self.history


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.calc = Calculator()
        self.expression = ""

        self._build_display()
        self._build_buttons()

    def _build_display(self):
        # Expression label (small, shows what you typed)
        self.expr_label = tk.Label(
            self.root,
            text="",
            anchor="e",
            bg="#1e1e2e",
            fg="#6e6e8e",
            font=("Arial", 14),
            padx=10
        )
        self.expr_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(20, 0))

        # Main display
        self.display = tk.Label(
            self.root,
            text="0",
            anchor="e",
            bg="#1e1e2e",
            fg="#ffffff",
            font=("Arial", 36, "bold"),
            padx=10
        )
        self.display.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 10))

    def _build_buttons(self):
        # (text, row, col, colspan, bg, fg)
        buttons = [
            ("AC", 2, 0, 1, "#313149", "#ff6b6b"),
            ("+/-", 2, 1, 1, "#313149", "#cdd6f4"),
            ("%", 2, 2, 1, "#313149", "#cdd6f4"),
            ("÷", 2, 3, 1, "#f38ba8", "#1e1e2e"),

            ("7", 3, 0, 1, "#45475a", "#cdd6f4"),
            ("8", 3, 1, 1, "#45475a", "#cdd6f4"),
            ("9", 3, 2, 1, "#45475a", "#cdd6f4"),
            ("×", 3, 3, 1, "#f38ba8", "#1e1e2e"),

            ("4", 4, 0, 1, "#45475a", "#cdd6f4"),
            ("5", 4, 1, 1, "#45475a", "#cdd6f4"),
            ("6", 4, 2, 1, "#45475a", "#cdd6f4"),
            ("-", 4, 3, 1, "#f38ba8", "#1e1e2e"),

            ("1", 5, 0, 1, "#45475a", "#cdd6f4"),
            ("2", 5, 1, 1, "#45475a", "#cdd6f4"),
            ("3", 5, 2, 1, "#45475a", "#cdd6f4"),
            ("+", 5, 3, 1, "#f38ba8", "#1e1e2e"),

            ("0", 6, 0, 2, "#45475a", "#cdd6f4"),
            (".", 6, 2, 1, "#45475a", "#cdd6f4"),
            ("=", 6, 3, 1, "#a6e3a1", "#1e1e2e"),
        ]

        for (text, row, col, colspan, bg, fg) in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                bg=bg,
                fg=fg,
                font=("Arial", 18, "bold"),
                relief="flat",
                cursor="hand2",
                activebackground=bg,
                activeforeground=fg,
                command=lambda t=text: self._on_click(t)
            )
            btn.grid(
                row=row, column=col, columnspan=colspan,
                padx=5, pady=5, sticky="nsew", ipadx=10, ipady=18
            )

        # Make columns and rows expandable
        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(2, 7):
            self.root.rowconfigure(i, weight=1)

    def _on_click(self, text):
        if text == "AC":
            self.expression = ""
            self.display.config(text="0")
            self.expr_label.config(text="")

        elif text == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display.config(text=self.expression)

        elif text == "%":
            try:
                value = float(self.expression)
                self.expression = str(value / 100)
                self.display.config(text=self.expression)
            except:
                self.display.config(text="Error")

        elif text == "=":
            try:
                self.expr_label.config(text=self.expression + " =")
                expr = self.expression.replace("×", "*").replace("÷", "/")
                result = eval(expr)
                # Clean up float display
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display.config(text=str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                self.display.config(text="Can't ÷ 0")
                self.expression = ""
            except:
                self.display.config(text="Error")
                self.expression = ""

        else:
            self.expression += text
            self.display.config(text=self.expression)
            self.expr_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()