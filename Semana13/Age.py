from datetime import date
class User:
    def __init__(self,name,date_of_birth):
        self.date_of_birth= date_of_birth
        self.name = name
    
    @property
    def age(self):
        today = date.today()
        age= today.year - self.date_of_birth.year
        if (today.month, today.day)<(self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
def adult(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError (f"{user.name} is not an adult")
        return func(user, *args)
    return wrapper
@adult
def enter_club(user):
    return f"{user.name} can enter the club."

user= User("Fabiola",date(2010,12,10))
try:
    print(enter_club(user))
except ValueError as e:
    print(e)