'''Napiš si třídy pro cokoliv chceš tak, aby splňovaly zadání:

    Jedna rodičovská třída, kde bude alespoň jeden atribut a jedna metoda.
    Dvě (nebo více) odvozených tříd.
    Jedna odvozená třída bude kompletně přepisovat metodu nadřazené třídy.
    Druhá odvozená třída bude rozšiřovat metodu nadřazené třídy pomocí super().
    Obě odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc jiným způsobem (koťátko mňouká, štěňátko štěká).'''

class BankingProducts:
    def __init__(self, name):
        self.name = name

    def interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
        print(f'Interest rate of {self.name} is {interest_rate}%')

    def minimum_balance(self, minimum_balance):
        self.minimum_balance = minimum_balance
        if self.minimum_balance < 0:
            print(f'You have to deposit money into your {self.name}! Minimum balance is 0.')
    
class CurrentAccount(BankingProducts):
    
    def usage(self):
        '''odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc jiným způsobem'''
        print(f'{self.name} it is mainly used for cash and non cash transaction. You dispose of your invested funds')

    def interest_rate(self, interest_rate):
        '''odvozená třída bude rozšiřovat metodu nadřazené třídy pomocí super().'''
        self.interest_rate = interest_rate
        print(f'{self.name} does not have interestesting interest rate.')
        super().interest_rate(interest_rate)

class SavingAccount(BankingProducts):  
    '''odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc jiným způsobem'''
    def usage(self):
        print(f'{self.name} you keep your money aside, they are quickly available and sometimes there is a good interest rate')

class Loan(BankingProducts):
    def usage(self):
        '''odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc jiným způsobem'''
        print(f'when you do not want to save money and you absolutely need to buy something, use {self.name}')

    def monthly_payment(self, monthly_payment):
        print(f'You will pay {monthly_payment} CZK from your account')
    
    def minimum_balance(self, monthly_payment):
        '''odvozená třída bude kompletně přepisovat metodu nadřazené třídy.'''
        print(f'There is no minimum balance, all you have to do is pay the monthly payment {monthly_payment} CZK on time.')

account = CurrentAccount('Current account')
account.usage()
account.interest_rate(0)
account.minimum_balance(-1)

save = SavingAccount('Saving account')
save.usage()
save.interest_rate(5)
save.minimum_balance(0)

loan = Loan('Loan')
loan.usage()
loan.interest_rate(15)
loan.monthly_payment(5000)
loan.minimum_balance(5000)


