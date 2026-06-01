# 📌 Problem Statement

# In real life, we use different payment methods like:

# Credit Card
# Debit Card
# UPI

# Even though the action is the same (making a payment), the process is different for each method.

# Your task is to design a system that demonstrates polymorphism using this scenario.

# 🎯 Requirements

# Create a base class:

# Payment

# with a method:

# pay(amount)
# Create derived classes:
    # CreditCard
    # DebitCard
    # UPI
# Each class should override the pay() method:
    # CreditCard → simulate OTP verification
    # DebitCard → simulate PIN verification
    # UPI → simulate UPI ID confirmation
# Use polymorphism:
    # Store all payment objects in a list
    # Call pay() using a loop



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