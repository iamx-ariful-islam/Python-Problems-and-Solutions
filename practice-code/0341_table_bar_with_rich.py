# pip install rich

from rich.table import Table
from rich.console import Console


console = Console()
table   = Table(title="Values Table")
table.add_column("Item")
table.add_column("Value", justify="right")
table.add_row("A", "5")
table.add_row("B", "9")
table.add_row("C", "2")
console.print(table)


'''output:

  Values Table  
┏━━━━━━┳━━━━━━━┓
┃ Item ┃ Value ┃
┡━━━━━━╇━━━━━━━┩
│ A    │     5 │
│ B    │     9 │
│ C    │     2 │
└──────┴───────┘
'''