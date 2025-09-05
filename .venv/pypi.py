from prettytable import PrettyTable

table = PrettyTable()



table.field_names = ["pokemon","type"]
table.add_rows(
   [["Pikachu", "Lighting"],
    ["Squirtle", "Water"],
    ["Bulbasaur", "Leaf"],
    ["Charmander", "Fire"]]
)

table.align = "l"
print(table)