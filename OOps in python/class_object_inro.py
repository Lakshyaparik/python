# class banyi and instance(object) banya hai

class BankAccount:
    def __init__(self,account_number, account_holder, balance):
         self.account_number = account_number  # अकाउंट नंबर सेट किया
         self.account_holder = account_holder  # अकाउंट होल्डर का नाम सेट किया
         self.balance = balance 

    def show_details(self):
                 print(f"Account Number: {self.account_number}")
                 print(f"Account Holder: {self.account_holder}")
                 print(f"Balance: ₹{self.balance}")

lakshya=BankAccount(2345448,"lakshya Pareek",20000)

lakshya.balance-=1000
lakshya.show_details()

