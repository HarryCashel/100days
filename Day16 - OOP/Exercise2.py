from prettytable import PrettyTable

table = PrettyTable()

table.add_column("House Names", ["Lannister", "Stark", "Targaryen", "Bolton", "Martell"])
table.add_column("House Leaders", ["Tywin", "Rob", "Daenerys", "Roose", "Oberyn"])
table.add_column("Sygil", ["Lion", "Direwolf", "Dragon", "Flayed-Man", "Sunspear"])
print(table)

table.align = "l"
table.header = False

print(table)