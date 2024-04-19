class CalculatorApp(object):
    def __init__(self):
        self.history = []
        self.last = 0

    def clear(self):
        self.last = 0
        self.history = []

    def last(self):
        return self.last

    def add(self, x, y):
        self.history.append(('add', x, y))
        return x + y

    def subtract(self, x, y):
        self.history.append(('subtract', x, y))
        return x - y

    def power(self, x, n):
        self.history.append(('power', x, n))
        return x**n
