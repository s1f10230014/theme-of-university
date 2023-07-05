class Bank:
    def __init__(self, amounts):
        self._amounts = amounts.copy()

    def transfer(self, sender, receiver, yen):
        self._amounts[sender] -= yen
        self._amounts[receiver] += yen

    def money_check(self, name):
        return self._amounts[name]
    
    def withdraw(self,name,yen):
        return self._amounts[name] - yen if  self._amounts[name]>yen else None


bank = Bank({
    'bob': 1234
})

balance = bank.withdraw('bob',234)
print(balance)
balance = bank.withdraw('bob',9999)
print(balance)
