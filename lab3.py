#TASK1 - SUM OF NATURAL NUMBERS USING WHILE LOOP
#n = int(input("Enter the number :- "))
#sum_of_all = 0

#i=1
#while (i < n):
 #   sum_of_all += i # 0 1 3 6 10
  #  i += 1 # 1 2 3 4 5
#print(f"The sum of all values upto {n} is : ",sum_of_all)
#TASK2 - IDENTIFY THE SMALLEST NUMBER USING WHILE LOOP
#smallest_num = 99999
#count = int(input("Hoe many inputs : "))

#i = 0

#while (i < count) :
 #   n = int(input("Enter your number : "))

  #  if smallest_num > n :
   #     smallest_num = n

    #i +=1

#print("The smallest value is : ",smallest_num)
    
#TASK 3- PASSWORD CHECKER USING WHILE LOOP 

#corrcet_password = 12345
#count = 1

#while True:
 #   n = int(input("Enter your password : "))

  #  if count == 5 :
   #     print("you have reached maxmium number of trails!..")
    #    print("please try again later!")
     #   break

    #if corrcet_password !=n :
     #   count += 1
      #  print("try again !")
    #else:
     #   print("Access granted !")
      #  break 
#TASK4 - NUMBER GUSSING GAMING USING BREAK AND WHILE

#import random

#secret_number = random.randint(1,50)
#print("Welcome to the number gussing game !")
#print("guess the number between 1 and 50 !")

#while True:
 #   n =int(input("Enter your guess...."))

  #  if n < secret_number :
   #     print("Too low ! Try again.. !")
    #elif n > secret_number :
     #   print("Too big ! Try again.. !")
    #else :
     #   print("Yay! you have got the number...")
      #  break


#TASK5 - VIP ENTRY GAME

while True :
    code = int(input("Please Enter your code : "))

    if code % 5 !=0 :
        print("you are not a VIP !")
        print("Get Away..")
    else :
        print("Granted Access !")
        break
#TASK6 - MARIO BROTHER WODEN FOREST LOST GAME FUNCTION 
