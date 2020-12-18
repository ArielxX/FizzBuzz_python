

def get_FizzBuzz( a ):
	return str(a)

def FizzBuzz( a, b ):
	while a <= b:
		print( get_FizzBuzz( a ) )
		a += 1

if __name__ == '__main__':
	
	FizzBuzz(1, 100)