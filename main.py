class Rab:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"hello I am {self.name}")

    def grow_up(self):
        self.age = self.age + 1
    
    def print_age(self):
        print(f"age - {self.age}")


rab2 = Rab(name = "rab2", age=40)
rab2.greeting()

rab1 = Rab(name = "rabb", age=20)
rab1.greeting()
