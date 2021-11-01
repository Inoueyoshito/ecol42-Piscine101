import sys

def ft_capital_city():

	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	args = sys.argv

	if len(args) != 2:
		sys.exit()
	
	ans = ""
	for key in states.keys():
		if args[1] == key:
			ans = capital_cities[states[args[1]]]
			break
		else:
			ans = "Unknown state"
	print(ans)

if __name__ == '__main__':
	ft_capital_city()
