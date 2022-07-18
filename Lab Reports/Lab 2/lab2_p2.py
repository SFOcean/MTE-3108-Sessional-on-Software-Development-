#Creating Class for base value
class InitialClass:
    def __init__(self, value):
        self.value = value
    def InitialMethod(self):
        print(f'Initial method: {self.value}')
#Class for Overridden method 
class SecondClass(InitialClass):
    def __init__(self, value):
        super().__init__(value)
    def InitialMethod(self):
        print(f'Overridden initialmethod: {self.value}')

#Initial Class
base = InitialClass("Initial Class")
base.InitialMethod()
#Overriding Second Class
override = InitialClass("Second Class")
override.InitialMethod()