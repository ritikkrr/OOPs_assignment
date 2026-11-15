from abc import ABC, abstractclassmethod
class Payment((ABC)):
    @abstractclassmethod
    def process_payment(amount):
        pass


class Creditcardpayment(Payment):
    def process_payment(amount):
        return "You can pay with credit_card"

class UPIPayment(Payment):
    def process_payment(amount):
        return "you can pay with UPI"

credit = Creditcardpayment()
upi = UPIPayment()

print(upi.process_payment())
print(credit.process_payment())
