
class Fibonacci:

    def __init__(self):
        pass

    def getFibonacciNumber(self, position):
        if position == 0:
            return 0
        a, b = 1, 1
        for i in range(position - 1):
            a, b = b, a + b
        return a
