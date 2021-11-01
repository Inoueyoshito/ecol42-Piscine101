import sys

def ft_state():

	args = sys.argv

	if len(args) != 2:
		sys.exit()

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
	
	ans = ""
	for value in capital_cities.values():
		if args[1] == value:
			k = get_keys_from_value(capital_cities, args[1])[0]
			ans = get_keys_from_value(states, k)[0]

			break
		else:
			ans = "Unknown state"
	print(ans)

if __name__ == '__main__':
	ft_state()
