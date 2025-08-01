class Movement():
    def __init__(self, category, title, type, amount):
        if not isinstance(amount, float):
            raise TypeError("amount must be a float")
        self.type = type
        self.category = category
        self.amount = amount 
        self.title = title



class Category():
    def __init__(self,name):
        self.name = name