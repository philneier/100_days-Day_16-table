from prettytable import PrettyTable

#create object
table = PrettyTable()
print(table)

#table methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

#table attributes
print(table.align)
#will return "c" (for central) for both columns
table.align = "l"
print(table.align)
print(table)

