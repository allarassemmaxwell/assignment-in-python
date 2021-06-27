print("*********************************************************")
print("********************* ASSIGNMENT TWO ********************")
print("*********************************************************")
print("\n")
numbers = [1, 4, 9, 3,13, 17]
maximum = max(numbers)
minimum = min(numbers)
user_make = input("Enter the mark: ")
# CHECK IF THE INPUT IT'S NOT AN INTEGER, DISPLAY A MESSAGE(MAX AND MIN NUMBER) AND WAIT FOR ANOTHER INPUT
while user_make.isdigit() == False:
    print("Maximum number is: ", maximum, " and the mininum number is: ", minimum)
    user_make = input("Please enter an integer number: ")

# CHECK IF THE INPUT IS IN THE LIST OR NOT
if int(user_make) in numbers:
    print("Your number: ", user_make, " is in the list")
else:
    print("Your number: ", user_make, " is not in the list")

print("\n")