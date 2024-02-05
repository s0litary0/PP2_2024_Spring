class StringClass:

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

p = StringClass()

p.getString()
p.printString()