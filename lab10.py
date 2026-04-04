class Payment :
    def pay(self,amount):
        print("Payment is processing......")

class Creditcard(Payment):
    def pay(self,amountt) :
        print(f"Processing credit card payment.{amount}")
        print("Verifing otp.....")
        print("Payment succesfull")

class Debitcard(Payment) :
    def paf(self,amount):
        print(f"Processing debit card payment.{amount}")
        print("Verifing otp.....")
        print("Payment succesfull")

class UPI(Payment):
    def pay(self,amount):
        print(f"Processing UPI payment.{amount}")
        print("verifing upi.......")
        print("payment suceesfull")

amount = float(input("Enter Your Amount to Pay :-  "))
method = input("Enter Payment Method :- ")
if method == 'cerdit' :
    payment = Creditcard()
elif method == 'debit':
    payment = Debitcard()
elif method == 'UPI' :
    payment = UPI()
else:
    print("Invalid payment method")
    exit()


payment.pay(amount)