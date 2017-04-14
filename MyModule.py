class Animal(object):
    def __init__(self, startname, age):
        self.name = startname #attribute1
        self.age = age #attribute2
    def description(self):
        print("this is " + self.name)
        print("he/she is " + str(self.age) +"years old")