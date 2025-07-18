from Clases import Movement, Category
class FinanceManager:
    def __init__(self):
        self.category = []    
        self.movement = []   

    def new_category(self,name):
        new_category = Category(name)
        self.category.append(new_category)
        return self.category

    def new_movement(self, category, title, movement_type, amount):
        new_movement = Movement(category, title, movement_type, amount,)
        self.movement.append(new_movement)
        return self.movement