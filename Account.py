class Account:
    def __init__(self,account_name,owner,balance):
        self.account_name = account_name
        self.owner = owner
        self.balance = balance
    def display_info(self):
        print(f"Account Number",self.account_name)
        print(f"Owner",self.owner)
    def get_balanced(self):
        print(f"Balance:",self.balance)
        return self.balance
class SavingsAccount(Account):
    def __init__(self,account_name,owner,balance,interest_rate):
        super().__init__(account_name,owner,balance)
        self.interest_rate = interest_rate
    def display_info(self):
        super().display_info()
        super().get_balanced()
        print(f"Interest Rate: {self.interest_rate * 100:.0f}%")
savings = SavingsAccount("1002", "An", 2000, 0.05)
savings.display_info()
savings.get_balanced()