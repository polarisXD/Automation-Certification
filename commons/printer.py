
class Printer:
    def __init__(self):
        pass

    def printEntries(self, dictionary):
        for key in dictionary.keys():
            print(key + ": " + str(dictionary[key]))