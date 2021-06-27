print("*********************************************************")
print("******************** ASSIGNMENT FOUR ************s********")
print("*********************************************************")
print("\n")
list = [
    '19591210-0848',
    '19850504-7053',
    '19930724-2652',
    '19751227-5202',
    '19761111-2835',
]

for number in list:
    clean_data = int(number.replace("-", ""))
    if clean_data % 2 == 0:
        print("{0} is a Female".format(number))
    else:
        print("{0} is a Male".format(number))
print("\n")