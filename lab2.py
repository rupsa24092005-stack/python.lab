user_input = int(input("Enter your input for row and columns:- "))
for i in range(user_input):#creating rows 0,1,2,3,4
    for j in range(i+1): # i+1 -> 1, j->0 star printed
        print("*", end=" ") #print * and space 
    print() #new line creat
     
for i in range(user_input):
    for j in range(user_input-i):
        print(" ", end="")

    for k in range(2*i-1):
        print("*", end="")
    print()
print() 
        
for i in range(user_input,0, -1): # -1 for reverse
   for j in range(i): 
      print("*", end=" ") 
   print() #new line creat