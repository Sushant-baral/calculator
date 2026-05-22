class Calculator:
    def __init__(self):
        self.result = 0
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
        entry = f"{a} {op} {b} = {result}"
        self.history.append(entry)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []


# Quick test — remove later
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(10, 5))        # 15
    print(calc.subtract(10, 3))   # 7
    print(calc.multiply(4, 6))    # 24
    print(calc.divide(20, 4))     # 5.0
    print(calc.percentage(50))    # 0.5
    print(calc.get_history())