# write a python program taht :-
# starts with a bank balance of 10000 .

# asks the user to enter the  amount they want to withdraw .

# uses a try-except block to handle errors . 

# the program should handle these cases :

# if the user enters non - numeric input, show




balance = 10000
try :
    amount = int(input("Enter Amount to withdraw :- "))

    if amount > balance :
        print("Insufficient Balance! ")
    elif amount < 0 :
        print("Withdraw amount could not be negative")
    else :
        print("Withdrawal successfull")
        print("Remaining Balance : ",balance - amount)
except ValueError :
    print("Invalid input ! please enter a number. ")

