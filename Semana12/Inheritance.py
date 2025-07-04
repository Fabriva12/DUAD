class Animal:
    def move(self):
        print("Puede moverse")

class Fly(Animal):
    def fly(self):
        print("Puede volar")

class Walk(Animal):
    def walk(self):
        print("Puede caminar")

class Swim(Animal):
    def swim(self):
        print("Puede nadar")

class Duck(Swim, Walk, Fly):
    def __init__(self):
        print("Nació un pato")

class Turtle(Swim, Walk):
    def __init__(self):
        print("Nació una tortuga")

class Parrot(Walk, Fly):
    def __init__(self):
        print("Nacio un loro")



parrot=Parrot()
parrot.fly()
duck=Duck()
duck.swim()
duck.walk()
turtle=Turtle()
turtle.move()
