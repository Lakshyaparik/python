# class banyi and instance(object) banya hai

class BankAccount:
    def __init__(self,account_number, account_holder, balance):
         self.account_number = account_number  # अकाउंट नंबर सेट किया
         self.account_holder = account_holder  # अकाउंट होल्डर का नाम सेट किया
         self.__balance = balance 

    def show_details(self):
                 print(f"Account Number: {self.account_number}")
                 print(f"Account Holder: {self.account_holder}")
                 print(f"Balance: ₹{self.__balance}")

    def deposit(self,amount):
            if amount>0:
                  self.__balance+=amount
                  print(f"Deposit Amount: {amount} Current Balance: {self.__balance}")
            else:
                  print("Deposit Error")

    def withdraw(self,amount):
           if 0 < amount <= self.__balance:
                  self.__balance-=amount
                  print(f"Withdraw Amount: {amount} Current Balance: {self.__balance}")
           

lakshya=BankAccount(2345448,"lakshya Pareek",20000)

lakshya.deposit(1000)
print('\n')
lakshya.withdraw(8000)

