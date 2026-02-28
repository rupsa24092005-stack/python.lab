# lab 5 : online shopping cart analysis
# you are building a simple system to analysis customer purchase in an online store
# each customer buys multiple items 
# problem statement 
# take input of purchased items separeted by space .
# store them in a list 
# convert items into a set to find unique product purchased
# store information in a tuple
# store name 
# location
# GST number
# perform the following :
# print total items purchased 
# print unique items purchased
# print how many items each was bought
# try modifing the tuple and observe what happems .


items_input = input("Enter purchase items separeted by space : ").lower() #input
items_list = items_input.split(" ") # list
unique_items = set(items_list) # converted into set
store_info = ('superMart' , 'domjur','GST563152')
 
#calculating total items using loops 
 
total_items = len(items_list)
# total_items = 0
#for item in items_list:
   # total_items += 1

unique_total_items = 0

for item in unique_items:
    unique_total_items += 1



print("\n------Shopping Summary--------")
print("Total Items purchased : ",total_items)
print("Total Unique Items purchased : ",unique_total_items)
print("Item purchase count : \n",)
for item in unique_items :
    print(item,":", items_list.count(item))

try :
    store_info[0] = 'SmartBazar'
except TypeError :
    print("\nTuple Modification Error ")

print('store Info:',store_info)

