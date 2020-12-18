

def get_FizzBuzz( a ):
	if a % 15 == 0:
		return 'FizzBuzz'
	if a % 3 == 0:
		return 'Fizz'
	if a % 5 == 0:
		return 'Buzz'
	return str(a)

def FizzBuzz( a, b ):
	while a <= b:
		print( get_FizzBuzz( a ) )
		a += 1

if __name__ == '__main__':
	
	FizzBuzz(1, 100)