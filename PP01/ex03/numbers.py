def numbers():
	for i in open("./numbers.txt").read().split(','):
		print(i.rstrip('\n'))

if __name__ == '__main__':
	numbers()
