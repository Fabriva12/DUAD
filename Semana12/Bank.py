class BankAccount:
    def __init__(self):
        self.balance = 0
    def add_money(self, amount):
        self.balance += amount
        
    def get_money(self, amount):
        self.balance -= amount
        
    def show_money(self):
        print(f"En su cuenta tiene {self.balance} de colones")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance
    
    def get_money(self, amount):
        if self.balance - amount < self.min_balance:
            print("No hay suficiente dinero")
        else:
            self.balance -= amount        
        
account1= SavingsAccount(2000)
account1.add_money(5000)
account1.add_money(5000)
account1.show_money()
account1.get_money(9000)
account1.show_money()