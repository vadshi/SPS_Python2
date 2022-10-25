from datetime import datetime
# нужно добавить библиотеку pytz:
# py -m pip install pytz
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # это атрибут будет изменен в экземпляре
        self._history = []        # приватный атрибут

    def __test(self):
        print('test method', self.name)

    @staticmethod
    def _get_current_time():  # приватный метод
        return pytz.utc.localize(datetime.utcnow())
    
    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])
              
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()
            
    def show_balance(self):
        print(f'Balance: {self.__balance}')
    
    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount:+} {transaction} {WHITE}on '
                  f' {date.astimezone()}')


# acc = Account('first', 0)
# acc.deposit(100)
# acc.deposit(250)
# acc.withdraw(370)
# acc.deposit(40)
# acc.withdraw(300)
# acc.show_history()
#
# # Про доступ к приватным атрибутам
# print(acc._get_current_time())
# print(acc._history)
# # print(acc.__balance)  ## Error
# # print(acc.balance)    ## Error
# # print(acc._balance)   ## Error
# print(vars(acc))
# print(acc._Account__balance)
# print(acc.__dict__)
# acc._Account__test()
# #
# acc._Account__balance = 1000
# acc.show_balance()