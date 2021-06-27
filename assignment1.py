print("*********************************************************")
print("********************* ASSIGNMENT ONE ********************")
print("*********************************************************")
print("\n")

# GET MINUTES INPUT
minutes = input("Enter minutes to be used every month: ")
# CHECK IF THE INPUT IT'S NOT AN INTEGER, REASK USER TO ENTER
while minutes.isdigit() == False:
   minutes = input("Please enter an integer number: ")

# GET COST PER MINUTE INPUT
cost_per_minutes = input("Enter the cost of each minute: ")
# CHECK IF THE INPUT IT'S NOT AN INTEGER, REASK USER TO ENTER
while cost_per_minutes.isdigit() == False:
   cost_per_minutes = input("Please enter an integer number: ")

# CONVERT NUMBERS TO INTEGER
minutes = int(minutes)
cost_per_minutes = int(cost_per_minutes)
total_price = 0
# IF COST PER MINUTES IS GREATER THAN 30
if cost_per_minutes > 30:
   discount    = ((minutes*cost_per_minutes)*10)/100
   total_price = minutes * cost_per_minutes
   print("You got a discount of 10% which is: $",discount, " \nTotal price is: $",total_price-discount)
   print("\n")
else:
   total_price = minutes * cost_per_minutes
   print("Total price is: $",total_price)
   print("\n")

