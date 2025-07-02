class Person :
    def __init__(self, name):
        self.name = name
p1 = Person("Julio")
p2 = Person("Andrew")
p3 = Person("Jade")
p4 = Person("Fabiola")
p5 = Person("Jaime")

class Bus :

    def __init__(self, max_passenger):
        self.max_passenger = max_passenger
        self.passengers = []
    
    def add_passenger (self, Person):
        if len(self.passengers) <= self.max_passenger:
            self.passengers.append(Person)
            print(f"Se ha subido {Person.name}")
            return self.passengers
        elif len(self.passengers) > self.max_passenger:
            print("No hay mas campo en el bus")

    def remove_passenger(self, Person):
        self.passengers.remove(Person)
        print(f"{Person.name} se ha bajado")
bus = Bus(3)

bus.add_passenger(p1)
bus.add_passenger(p2)
bus.add_passenger(p3)
bus.add_passenger(p4)
bus.add_passenger(p5)
bus.remove_passenger(p1)
