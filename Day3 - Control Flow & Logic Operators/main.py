"""Adventure game"""

# ASCII ART
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Program greeting
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

q1 = input("You're at a cross road. Do you want to go 'left' or 'right'? ")

if "r" in q1.lower():
    print("You follow the daisy covered road.\nYou are attacked by a giant Venus Fly Trap. Swallowed whole.")
elif "l" in q1.lower():
    print("You follow the dirt road to a pond. You see a castle across the water.")
    print("There is a boat that matches the colour of the castle and a boat that matches the colour of the trees.\n")

    q2 = input("Do you chose the grey(castle) or brown(trees) boat? ")
    if "b" or "tr" in q2.lower():
        print("You sail smoothly to the castle door.")

        q3 = input("You get to the door and see a key, a trapdoor, and an auspicious looking window...\n"
                   "Do you take the trapdoor, use the key, or sneak in through the window? ")
        if "k" in q3.lower():
            print("The key turns to ash in the lock.\nYou look at your hand as it starts to to the same.")
        elif "t" in q3.lower():
            print("You shuffle into the trapdoor.\nThere are no lights and no doors or windows.")
            print("The trap door shuts behind you and you are locked in.")
        elif "w" in q3.lower():
            print("You see the treasure. You steal it. GG")

    elif "g" or "c" in q2.lower():
        print("You get halfway to the castle before your boat sinks.")
else:
    print("Please choose 'left' or 'right'.")
