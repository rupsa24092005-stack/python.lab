class BankAccount :
    #constructer 

    def __init__(self,name,acc_number,balance) :
        self.name = name 
        self.acc_number = acc_number
        self.balance = balance 


    def deposite(self , amount ):
        self.balance = self.balance + amount
        print("Deposited : ",amount)
        return ""

    def withdraw(self , amount) :
        self.balance = self.balance - amount
        print("Withdraw : ",amount)
        return ""


    def check_balance(self) :
        print("Available Balance : ",self.balance)
        return ""

acc1 = BankAccount("Arindam" , 12345 , 1000)
acc2 = BankAccount("ritam" , 23564 , 1500)
acc3 = BankAccount("priti",45621 , 0)
print(acc1.name)  #arindam
print(acc1.acc_number) #12345
print(acc1.balance) #1000
print(acc1.deposite (1000))
print(acc1.withdraw(500))
print(acc1.balance)
print()

print(acc2.name)  
print(acc2.acc_number) 
print(acc2.balance) 
print(acc2.deposite(1000))
print(acc2.withdraw(500))
print(acc2.balance)
print()

print(acc3.name) 
print(acc3.acc_number) 
print(acc3.balance) 
print(acc3.deposite(4000))
print(acc3.withdraw(5000))
print(acc3.balance)
print()
