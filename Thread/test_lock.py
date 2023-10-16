from threading import Thread,Lock
from time import sleep


class Account(object):
    def __init__(self):
        self.__balance = 0
        self.__lock = Lock()
        
    def deposit(self, money):
        self.__lock.acquire()
        try:
            new_balance = self.__balance + money
            sleep(0.01)
            self.__balance = new_balance
        except Exception as e:
            print(e)
        finally:
            self.__lock.release()
            pass
            
    @property
    def balance(self):
        return self.__balance
        

class AddMoneyThread(Thread):
    def __init__(self, account:Account, addMoney):
        super().__init__()
        self.__account = account
        self.__addMoney = addMoney
        
    def run(self):
        self.__account.deposit(self.__addMoney)

if __name__ == '__main__':
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
    print(account.balance)