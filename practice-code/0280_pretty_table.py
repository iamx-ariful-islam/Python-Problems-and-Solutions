# pip install prettytable

from prettytable import PrettyTable


# specify the column names while initializing the table
my_table = PrettyTable(['Student Name', 'Class', 'Section', 'Percentage'])

# add rows
my_table.add_row(['A', 'II', 'A', '90.00%'])
my_table.add_row(['B', 'XI', 'B', '75.00%'])
my_table.add_row(['C', 'VI', 'C', '95.00%'])
my_table.add_row(['D', 'IV', 'B', '85.00%'])
my_table.add_row(['E', 'IX', 'C', '80.00%'])

print(my_table)



'''output:

+--------------+-------+---------+------------+
| Student Name | Class | Section | Percentage |
+--------------+-------+---------+------------+
|      A       |   II  |    A    |   90.00%   |
|      B       |   XI  |    B    |   75.00%   |
|      C       |   VI  |    C    |   95.00%   |
|      D       |   IV  |    B    |   85.00%   |
|      E       |   IX  |    C    |   80.00%   |
+--------------+-------+---------+------------+
'''