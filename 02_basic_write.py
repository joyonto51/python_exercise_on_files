authors = [
	[1,'almasud','Abdullah Al Masud'],
	[2,'rimon','Rimon Ali'],
	[3,'niloy','Niloy Roy'],
	[4,'sourav','Sourav Deb Sharma'],
	[5,'sathi','Sathi Rani Roy']
]

file = open("02_basic_write.txt", "a+")

for item in authors:
	text = ','.join(map(str,item))
	file.write(text +'\n')

file.close()