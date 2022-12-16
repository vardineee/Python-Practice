from prettytable import PrettyTable

table = PrettyTable()
column = table.add_column("City name", ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
column_1 = table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.align = 'r'

print(table)