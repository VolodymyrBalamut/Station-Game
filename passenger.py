import Person

class Passenger(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

p1 = Passenger("John", 36)

p1.myfunc()
print(p1.name)
print(p1.age)
