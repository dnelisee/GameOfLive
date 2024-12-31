from dataclasses import dataclass 
from pathlib import Path

try : 
	import tomllib 
except ImportError : 
	import tomli as tomllib # type: ignore
	

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"

"""
	This class contains coordinates of alive cell. 
"""

@dataclass 
class Pattern : 
	name : str 
	alive_cells : set[tuple[int, int]] 

	@classmethod 
	def from_toml(cls, name, toml_data) : 
		return cls(
			name, 
			alive_cells = {tuple(cell) for cell in toml_data["alive_cells"]}
		) 
	
# get a specific pattern of the file PATTERNS_FILE 
def get_pattern(name, filename=PATTERNS_FILE) : 
	"""
		get the dictionary of all data of the toml file : 
		data = {<name of the pattern> : <alive_cells array>}
	"""
	data = tomllib.loads(filename.read_text(encoding="utf-8"))

	# return the alive_cells of the datum 
	return Pattern.from_toml(name, toml_data=data[name])

# get all patterns of the file PATTERNS_FILE
def get_all_patterns(filename=PATTERNS_FILE) : 
	data = tomllib.loads(filename.read_text(encoding="utf-8"))
	return [
		Pattern.from_toml(name, toml_data)
		for name, toml_data in data.items()
	]
