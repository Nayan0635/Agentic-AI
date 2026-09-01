# Question 5: Multilevel Inheritance (Bank System)

# Create the hierarchy

# Bank
#    ↑
# SavingsAccount
#    ↑
# PremiumSavings

### Bank

# * bank_name
# show_bank()

### SavingsAccount

# * account_number
# show_account()

### PremiumSavings

# * balance
# show_balance()
# Requirements

# * Use `super()` in every constructor.
# * Use `super()` inside methods wherever applicable.
# * Display all information.

# **Expected Output**

# Bank : SBI
# Account No : 123456789
# Balance : 250000

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        
    def show_bank(self):
        print(f"Bank : {self.bank_name}")
        
class SavingsAccount(Bank):
    def __init__(self, bank_name, account_number):
        super().__init__(bank_name)
        self.account_number = account_number
        
    def show_account(self):
        super().show_bank()
        print(f"Account : {self.account_number}")
        
        
        
class PremiumSavings(SavingsAccount):
    def __init__(self, bank_name, account_number, balance):
        super().__init__(bank_name, account_number)
        self.balance = balance
        
    def show_balance(self):
        super().show_account()
        print(f"Balance : {self.balance}")
        
        
# Main()
bnk = PremiumSavings('SBI', 123456789, 250000000)
bnk.show_balance()