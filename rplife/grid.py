# for defaultdict : collections.defaultdict
import collections

# elements that represent cells in the terminal 
ALIVE = "♥"
DEAD  = "."

"""
	The roles of this class are : 
	- evolve the network to the next generation 
	- give a representation as chaine of grid 
"""
class LifeGrid : 
	def __init__(self, pattern) : 
		self.pattern = pattern 

	def evolve(self) : 
		"""
			Verify alive and death cell around each cell 
			in other to give the next generation 
		"""
		# relative coordinates of neighbors
		neighbors = (
			(-1, -1),# above left 
			(-1, 0), # above 
			(-1, 1), # above right 
			(0, -1), # left 
			(0, 1),  # right
			(1, -1), # below left 
			(1, 0),  # below 
			(1, 1)   # below right 
		)

		# number of neighbors 
		num_neighbors = collections.defaultdict(int)

		# count the number of neighbors 
		for row, col in self.pattern.alive_cells : 
			for drow, dcol in neighbors : 
				num_neighbors[(row + drow, col + dcol)] += 1 

		# set of cells which will remain alive at the next generation 
		stay_alive = {
			cell for cell, num in num_neighbors.items() if num in {2, 3}
		} & self.pattern.alive_cells

		# set of cells which will come to life at the next generation 
		come_alive = {
			cell for cell, num in num_neighbors.items() if num == 3
		} - self.pattern.alive_cells 

		# update alive_cells by set the new generation 
		self.pattern.alive_cells = stay_alive | come_alive

	def as_string(self, bbox) : 
		"""
			Permit to represent the grid as a string which 
			can be display on the terminal. 

			The box bbox define the part of the grid which 
			will be displayed on the terminal.  
		"""
		# variables of the grid to display 
		start_col, start_row, end_col, end_row = bbox

		# display array 
		display = [self.pattern.name.center(2 * (end_col - start_col))]

		# fill the display array 
		for row in range(start_row, end_row) : 
			# fill a row 
			display_row = [
				ALIVE if (row, col) in self.pattern.alive_cells else DEAD 
				for col in range(start_col, end_col)
			]

			# add it in the final array 
			display.append(" ".join(display_row))

		# convert the array into string that will be displayed 
		return "\n ".join(display)
		

	def __str__(self) : 
		""" 
			redefine the representation of the object LifeGrid 
		""" 
		return (
			f"{self.pattern.name}: \n"
			f"Alive cells -> {sorted(self.pattern.alive_cells)}"
		)