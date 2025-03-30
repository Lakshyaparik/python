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


class SavingAccount(BankAccount):
    def __init__(self,account_number, account_holder, balance,interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100
    

lakshya=SavingAccount("1234xab","lakshya-pareek",10000,2)

lakshya.show_details()
print(lakshya.calculate_interest())