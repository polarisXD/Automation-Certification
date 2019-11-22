
class NumberSpeller:
    def __init__(self):
        self.singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]
        self.tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.places = ["", "", "", "hundred", "thousand", "", "hundred", "million", "", "hundred", "billion"]

    def getSinglesSpelling(self, number):
        return self.singles[number]

    def getTeensSpelling(self, number):
        return self.teens[int(str(number)[1])]

    def getTensSpelling(self, number):
        return self.tens[number]

    def getDigitsSpelling(self, digits):
        return self.places[digits]

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

    def spellNumber(self, number):
        if number == 0:
            print("0 - zero")
            return
        number_string = str(number)[::-1]
        digits = len(number_string)
        number_spelling = ""
        skip_next = False
        for i in range(digits):
            if skip_next:
                skip_next = False
                continue
            if (i + 1) % 3 == 1 and i + 1 > 3:
                number_spelling = self.getDigitsSpelling(i + 1) + " " + number_spelling
            number = int(number_string[i])
            if i % 3 == 0 and digits >= i + 2:
                if int(number_string[i+1]) == 1:
                    # Is a teen number, combine with next digit
                    number = int(number_string[i:i+2][::-1])
                    skip_next = True
            spelling = self.getNumberSpelling(number, i + 1)
            if spelling != "":
                number_spelling = spelling + " " + number_spelling
        return number_spelling[:-1]
