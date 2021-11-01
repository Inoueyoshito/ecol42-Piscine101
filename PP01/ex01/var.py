def my_var():
	num = 42
	num1 = "42"
	num2 = "forty-two"
	num3 = 42.0
	num4 = True
	num5 = [42]
	num6 = {'42': '42'}
	num7 = (42,)
	num8 = set()

	print(num, 'has a type', type(num))
	print(num1, 'has a type', type(num1))
	print(num2, 'has a type', type(num2))
	print(num3, 'has a type', type(num3))
	print(num4, 'has a type', type(num4))
	print(num5, 'has a type', type(num5))
	print(num6, 'has a type', type(num6))
	print(num7, 'has a type', type(num7))
	print(num8, 'has a type', type(num8))


if __name__ == '__main__':
	 my_var()
