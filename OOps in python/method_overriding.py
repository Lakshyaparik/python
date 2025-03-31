
#method overiding happen when we overide the parent method 
#means the class must be a parent 

class Account:
    def __init__(self,account_number, account_holder, balance):
         self.account_number = account_number  # अकाउंट नंबर सेट किया
         self.account_holder = account_holder  # अकाउंट होल्डर का नाम सेट किया
         self.balance = balance 

    def show_details(self):
                 print(f"Account Number: {self.account_number}")
                 print(f"Account Holder: {self.account_holder}")
                 print(f"Balance: ₹{self.balance}")



class SavingAccount(Account):
    def __init__(self,account_number, account_holder, balance,interest_rate):
              super().__init__(account_number, account_holder, balance)
              self.interest_rate=interest_rate

    
    def show_details(self):
          # parent_show_details=super().show_details()
           total_balance=self.balance*self.interest_rate / 100
           print(f"From Parent Method: {super().show_details()} || Current Method: {total_balance}")


lakshya=SavingAccount(1234,"lakshya-pareek",20000,3.00)

lakshya.show_details()