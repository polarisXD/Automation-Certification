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


class NumberSpeller:
    def __init__(self):
        pass

    def getSinglesSpelling(self, number):
        singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return singles[number]

    def getTeensSpelling(self, number):
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]
        return teens[int(str(number)[1])]

    def getTensSpelling(self, number):
        tens = ["", "tenty", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[number]

    def getDigitsSpelling(self, digits):
        places = ["", "", "", "hundred", "thousand", "", "hundred", "million", "", "hundred", "billion"]
        return places[digits]

    def getNumberSpelling(self, number, digits):
        if number >= 10:
            return self.getTeensSpelling(number)
        elif digits % 3 == 1:
            return self.getSinglesSpelling(number)
        elif digits % 3 == 2:
            return self.getTensSpelling(number)
        elif digits % 3 == 0:
            spelling = self.getSinglesSpelling(number)
            if number != 0:
                spelling = spelling + " " + self.getDigitsSpelling(digits)
            return spelling


def spellFibonacciNumber(position):
    fibonacci_number = Fibonacci().getFibonacciNumber(position)
    if fibonacci_number == 0:
        print("0 - zero")
        return
    fibonacci_string = str(fibonacci_number)[::-1]
    digits = len(fibonacci_string)
    number_speller = NumberSpeller()
    fibonacci_spelling = ""
    skip_next = False
    for i in range(digits):
        if skip_next:
            skip_next = False
            continue
        if (i + 1) % 3 == 1 and i + 1 > 3:
            fibonacci_spelling = number_speller.getDigitsSpelling(i + 1) + " " + fibonacci_spelling
        number = int(fibonacci_string[i])
        if i % 3 == 0 and digits >= i + 2:
            if int(fibonacci_string[i+1]) == 1:
                # Is a teen number, combine with next digit
                number = int(fibonacci_string[i:i+2][::-1])
                skip_next = True
        spelling = number_speller.getNumberSpelling(number, i + 1)
        if spelling != "":
            fibonacci_spelling = spelling + " " + fibonacci_spelling
    print(str(fibonacci_number) + " - " + fibonacci_spelling[:-1])


for num in range(55):
    spellFibonacciNumber(num)
