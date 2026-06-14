def writeToFile(x, y):
    f = open(x, "w+")
    f.write(y + "\n")
    f.close()
    
def appendToFile(x, y):
	f = open(x, "a")
	f.write(y + "\n")
	f.close()
	
def readFromFile(x):
	f = open(x, "r")
	content = f.read()
	print(content)
	return content

writeToFile('greet.txt', 'Hello!')
appendToFile('greet.txt', 'Goodbye!')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
