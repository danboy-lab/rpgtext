# Atribute tree/perks made with Textual 
from textual.app import App
from textual.widgets import Header, Footer, Static, Label

class Tree(App):
	def compose(self):
		yield Header()
		yield Static("Hello World!")
		yield Footer()
		yield Label()

if __name__ == "__main__":
	app = Tree()
	app.run()