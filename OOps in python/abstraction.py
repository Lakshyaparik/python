#abstraction without decrators and abstract class isme error nhi aygi bus none output hoga
#pyhon force bhi nhi krega method override ke liya
class Bank:
    def loan_interest(self):
        pass 
    
class Sbi(Bank):
    pass

class Icici(Bank):
    def loan_interest(self):
            print("icici loan interest 8%")

class hdfc(Bank):
    def loan_interest(self):
        pass
        

loan=[Bank(),Sbi(),Icici(),hdfc()]

# for info in loan:
#     info.loan_interest()


#abstraction with decrators and abstract class isme error aygi agar koi class wo method def nhi kregi jo 
#pyhon force bhi nhi krega method override ke liya

from abc import ABC,abstractmethod
class Payment_Gateway(ABC):
     @abstractmethod
     def payment_process(self):
          """payment process define krna hi hoga"""
          pass
     

class Paypal(Payment_Gateway):
     pass


class Paytm(Payment_Gateway):
     def payment_process(self):
          pass
     
class Google_pay(Payment_Gateway):
     def payment_process(self):
          print("google pay pyment process!")

#payment_system=[Payment_Gateway(),Paypal(),Paytm(),Google_pay()]
payment_system=[Payment_Gateway(),Paypal(),Paytm(),Google_pay()]

for payment in payment_system:
     print(payment.payment_process())


