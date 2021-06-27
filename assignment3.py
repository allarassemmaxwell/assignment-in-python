print("*********************************************************")
print("******************** ASSIGNMENT THREE *******************")
print("*********************************************************")
print("\n")
count = 0
# FUNCTION TO REMOVE SPACE
def remove(string):
    return string.replace(" ", "")

# GET TEXT FROM USER
user_text = input("Please enter a long text: ")

print("Original text: ",user_text)
print("Removed space: ",remove(user_text))

for i in user_text:
    if (i.isspace()):
        count += 1
print("The number of blank spaces is: ",count)


print("\n")