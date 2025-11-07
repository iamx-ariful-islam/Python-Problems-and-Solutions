# pip install rich

from rich.console import Console
from rich.progress import track


console = Console()
console.print("[bold cyan]Rich Progress Example[/bold cyan]")

for step in track(range(5), description="Processing..."):
    pass

console.print(":sparkles: Done!", style="green")