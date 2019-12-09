
class Counter:
    def __init__(self):
        pass

    def countEntries(self, entry, dictionary):
        if entry not in dictionary.keys():
            dictionary[entry] = 1
        elif entry in dictionary.keys():
            count = dictionary[entry]
            dictionary[entry] = count + 1
        else:
            print(entry + " not handled")
