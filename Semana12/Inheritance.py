class Animal:
    def move(self):
        print("Can move")

class Fly(Animal):
    def fly(self):
        print("Can fly")

class Walk(Animal):
    def walk(self):
        print("Can walk")

class Swim(Animal):
    def swim(self):
        print("Can swim")

class Duck(Swim, Walk, Fly):
    def __init__(self):
        print("Born a duck")

class Turtle(Swim, Walk):
    def __init__(self):
        print("Born a turtle")

class Parrot(Walk, Fly):
    def __init__(self):
        print("Born a parrot")



parrot=Parrot()
parrot.fly()
duck=Duck()
duck.swim()
duck.walk()
turtle=Turtle()
turtle.move()
