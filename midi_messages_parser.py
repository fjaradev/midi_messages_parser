from rich.console import Console
from rich.table import Table
import sys

console = Console()


console.print("\n\nWelcome to the MIDI parser\n\n", justify="center", style="bold red")

while True:
	try:
		# Get the status byte
		status_byte_input = console.input("[yellow]What's the message type?(Note on, Note off): [/yellow]").lower().strip()
		while status_byte_input != "note on" and status_byte_input != "note off":
			print("Invalid message type input. Please type 'note on' or 'note off'")
			status_byte_input = console.input("[yellow]What's the message type?(Note on, Note off): [/yellow]").lower().strip()
		status_byte = 0b10010000 if status_byte_input == "note on" else 0b10000000 # Defining the status byte as 0b10010000 for Note On and 0b10000000 for Note Off
		# Get the channel number
		channel = int(console.input("[yellow]Type the channel number (1-16): [/yellow]"))
		while channel < 1 or channel > 16:
			print("Invalid channel number. Please type a number between 1 and 16")
			channel = int(console.input("[yellow]Type the channel number (1-16): [/yellow]"))
		status_byte += channel - 1
		# Get the data bytes
		data_byte1 = int(console.input("[yellow]Type the MIDI note (0-127): [/yellow]"))
		while data_byte1 < 0 or data_byte1 > 127:
			print("Invalid MIDI note. Please type a number between 0 and 127")
			data_byte1 = int(console.input("[yellow]Type the MIDI note (0-127): [/yellow]"))
		data_byte2 = int(console.input("[yellow]Type the velocity (0-127): [/yellow]"))
		while data_byte2 < 0 or data_byte2 > 127:
			print("Invalid velocity. Please type a number between 0 and 127")
			data_byte2 = int(console.input("[yellow]Type the velocity (0-127): [/yellow]"))

		# Display the MIDI message
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
		sys.exit()

