'''How does polymorphism in the Payment class allow different payment methods 
   (e.g., CreditCardPayment and PhonePayPayment) to be processed using a common 
   interface, and what are the benefits of this approach?'''

class Payment:
    def process_payment(self, amount):
        self.amount= amount
        #raise NotImplementedError("Error Method")
      

        
#-----------------------------Process Payment--------------------------------#
def process_payments(payment_method, amount):
    payment_method.process_payment(amount)
    
#-----------------------------Class Credit Card------------------------------#    
class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Credit card payment of ${amount} using card number {self.card_number}.")

#----------------------------Class Phone Pay--------------------------------#
class PhonePayPayment(Payment):
    def __init__ (self, upi_id):
        self.upi_id = upi_id

    def process_payment(self,amount):
        print(f"Processing PayPal payment of ${amount} using email {self.upi_id}.")

#-----------------------------Main Method------------------------------------#
def main():
    credit_card = CreditCardPayment(card_number = "123456789")
    phone_pay = PhonePayPayment(upi_id = "123456789@ybl")

    print("Process Payment")
    process_payments(credit_card,100)
    process_payments(phone_pay,200)

if __name__ =="__main__":
    main()    