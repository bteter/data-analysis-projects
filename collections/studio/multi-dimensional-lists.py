food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food = food.split(',') #turns original string into list
food_cabinet = sorted(food) #sorts list alphabetically 

equipment = equipment.split(',')
equipment_cabinet = sorted(equipment)

pets = pets.split(',')
pets_cabinet = sorted(pets)

sleep_aids = sleep_aids.split(',')
sleep_aids_cabinet = sorted(sleep_aids)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
user_selection = input("Choose a cabinet 0-3: ")


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

#if the user selects 0 print food, if user selects 1 print equipment etc
# if input is > 3 print error, if input is not int print error,

if user_selection == str(0):
    print(cargo_hold[0])
if user_selection == str(1):
    print(cargo_hold[1])
if user_selection == str(2):
    print(cargo_hold[2])
if user_selection == str(3):
    print(cargo_hold[3])
else:
    print("Error, please select cabinet 0-3")

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
