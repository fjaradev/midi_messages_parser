from rich.console import Console
from rich.table import Table

console = Console()


console.print("\n\nWelcome to the MIDI parser\n\n", justify="center", style="bold red")

while True:
	try:
		status_byte = 0x90 if console.input("[yellow]What's the message type?(Note on, Note off): [/yellow]").lower().strip()[0] == "note on" else 0x80
		data_byte1 = int(console.input("[yellow]Type the MIDI note: [/yellow]"))
		data_byte2 = int(console.input("[yellow]Type the velocity: [/yellow]"))

		table = Table(show_header=True, header_style="bold magenta")
		table.add_column("Binary", style="dim", width=30, justify="center")
		table.add_column("Hexadecimal", style="dim", width=12, justify="center")
		table.add_column("Decimal", style="dim", width=12, justify="center")
		table.add_row(f"[bold cyan]{status_byte:08b}  {data_byte1:08b}  {data_byte2:08b}[/bold cyan]",
					f"[bold cyan]{status_byte:02x}  {data_byte1:02x}  {data_byte2:02x}[/bold cyan]",
					f"[bold cyan]{status_byte:0d}  {data_byte1:0d}  {data_byte2:0d}[/bold cyan]")
		console.print(table)
		del table

	except KeyboardInterrupt:
		print("\n\nProgram finished")
