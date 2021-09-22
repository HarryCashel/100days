"""Program to mark a map with an 'X'"""

# Greeting
print("This is our Map. Let's place a coordinate!")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("\nExample: 'Column 1, Row 1 would be entered as:\t"
      "11")
position = (input("Where do you want to put the treasure? "))

column = int(position[0])
row = int(position[1])
treasure_map[row - 1][column - 1] = "X    "

print(f"{row1}\n{row2}\n{row3}")