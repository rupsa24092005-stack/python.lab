# problem 1

# write a python program that :- 
# take a sentence as input from the uesr . 
# Remove extra spaces from the biginning and end
# Converts how many times the letter "a" appears (case -insensitive)
# finds the first position of the word "is"
# Replace the word "bad" with "good"
# prints the final cleaned sentence 


sentence = input("Enter a text :- ")

sentence = sentence.strip().lower()

count_a  = sentence.count('a')

pos_is = sentence.find("is")

sentence = sentence.replace("bad","good")

print("Final sentence",sentence.title())
print("Number of times a appesred: ",count_a)
print("The index of is = ",pos_is)


#Problem 2 
# Takes a uesrname as input
# Removes extra spaces
# Converts it to lower case
# counts how many times the character "_" appears
# Finds the position of "@" usinf both find() and index()
# Replaces "admin" with "user" .
# display the username in UPERCASE and title case


username = input("Enter your username :- ")
uesrname = username.strip().lower().upper()
count_username = uesrname.count('_')
pos_find = username.find("@")
pos_index = username.index("@")
new_username = username.replace("admin","user")

print("Number of times underscore appesrs: ",count_username)
print("Username in titlecase : ",new_username.title())
print("Username in titlecase : ",new_username.upper())
print("position of @ using find : ",pos_find)
print("position of @ using index : ",pos_index)
