class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"hello I am {self.name}")

    def grow_up(self):
        self.age = self.age + 1
    
    def print_age(self):
        print(f"age - {self.age}")


people1 = people(name = "oleg", age=40)
people1.greeting()

people2 = people(name = "dima", age=20)
people2.greeting()
