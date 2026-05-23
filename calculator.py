import tkinter as tk
from tkinter import scrolledtext


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
        self.history_visible = False

        self._build_display()
        self._build_buttons()
        self._bind_keyboard()

    def _build_display(self):
        self.expr_label = tk.Label(
            self.root, text="", anchor="e",
            bg="#1e1e2e", fg="#6e6e8e",
            font=("Arial", 14), padx=10
        )
        self.expr_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(20, 0))

        self.display = tk.Label(
            self.root, text="0", anchor="e",
            bg="#1e1e2e", fg="#ffffff",
            font=("Arial", 36, "bold"), padx=10
        )
        self.display.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 10))

    def _build_buttons(self):
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

            ("History", 7, 0, 4, "#313149", "#89b4fa"),
        ]

        for (text, row, col, colspan, bg, fg) in buttons:
            btn = tk.Button(
                self.root, text=text, bg=bg, fg=fg,
                font=("Arial", 18, "bold"), relief="flat",
                cursor="hand2", activebackground=bg, activeforeground=fg,
                command=lambda t=text: self._on_click(t)
            )
            btn.grid(
                row=row, column=col, columnspan=colspan,
                padx=5, pady=5, sticky="nsew", ipadx=10, ipady=18
            )

        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(2, 8):
            self.root.rowconfigure(i, weight=1)

        # History panel (hidden by default)
        self.history_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.history_box = scrolledtext.ScrolledText(
            self.history_frame,
            bg="#313149", fg="#cdd6f4",
            font=("Arial", 12), relief="flat",
            state="disabled", width=28, height=8
        )
        self.history_box.pack(padx=10, pady=10, fill="both", expand=True)

    def _bind_keyboard(self):
        self.root.bind("<Key>", self._on_key)
        self.root.focus_set()

    def _on_key(self, event):
        key = event.char
        keysym = event.keysym

        if key in "0123456789.":
            self._on_click(key)
        elif key == "+":
            self._on_click("+")
        elif key == "-":
            self._on_click("-")
        elif key == "*":
            self._on_click("×")
        elif key == "/":
            self._on_click("÷")
        elif key == "%":
            self._on_click("%")
        elif keysym in ("Return", "KP_Enter"):
            self._on_click("=")
        elif keysym == "BackSpace":
            self._backspace()
        elif keysym == "Escape":
            self._on_click("AC")

    def _backspace(self):
        self.expression = self.expression[:-1]
        self.display.config(text=self.expression if self.expression else "0")

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
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display.config(text=str(result))
                # Save to history
                self.calc.history.append(f"{self.expression} = {result}")
                self._update_history_box()
                self.expression = str(result)
            except ZeroDivisionError:
                self.display.config(text="Can't ÷ 0")
                self.expression = ""
            except:
                self.display.config(text="Error")
                self.expression = ""

        elif text == "History":
            self._toggle_history()

        else:
            self.expression += text
            self.display.config(text=self.expression)
            self.expr_label.config(text="")

    def _toggle_history(self):
        if self.history_visible:
            self.history_frame.grid_forget()
            self.history_visible = False
        else:
            self.history_frame.grid(row=8, column=0, columnspan=4, sticky="ew")
            self.history_visible = True
            self._update_history_box()

    def _update_history_box(self):
        self.history_box.config(state="normal")
        self.history_box.delete("1.0", tk.END)
        history = self.calc.get_history()
        if history:
            for entry in reversed(history):
                self.history_box.insert(tk.END, entry + "\n")
        else:
            self.history_box.insert(tk.END, "No history yet.")
        self.history_box.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()