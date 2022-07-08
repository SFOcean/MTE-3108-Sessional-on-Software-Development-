class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print ("Hello, my name is " + self.name)
        print ("Hello, my age is " + self.age)


p1 = person ("Shahriar", "24")
p1.myfunc()