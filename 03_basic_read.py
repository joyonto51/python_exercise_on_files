# file = open("03_basic_read.txt", "r")
# file_handler = file.readlines()
with open("03_basic_read.txt") as file_handler:
	for line in file_handler:
		text = line.split(',')
		print("{}-{}".format(text[0],text[2]), end='')

print('')

# file.close()