import numpy as np
from astropy.table import Table

def sin_table():
	arr_x = np.linspace(0, 2*np.pi, 1000)
	arr_sin_x = np.sin(arr_x)

	data_table = Table()
	data_table["x"] = arr_x
	data_table["sin(x)"] = arr_sin_x

	data_table["x"].format = "{:.3f}"
	data_table["sin(x)"].format = "{:.3f}"

	return data_table

def main():
	print(sin_table())

if __name__=="__main__":
	main()