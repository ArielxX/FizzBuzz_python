import argparse
from colored import stylize, fg


def get_fizzbuzz(a):
	'''
	Return the FizzBuzz for the number a
			'Fizz': if a is divisible by 3 and not by 5
			'Buzz': if a is divisible by 5 and not by 3
			'FizzBuzz': if a is divisible by 3 and 5
			a: in any other case
	'''
	if a % 15 == 0:
		return 'FizzBuzz', fg('green')
	if a % 3 == 0:
		return 'Fizz', fg('blue')
	if a % 5 == 0:
		return 'Buzz', fg('red')
	return str(a), fg('black')


def fizzbuzz(a, b):
	# Print the Fizzbuzz for every number between a and b
	while a <= b:
		[ans, color] = get_fizzbuzz(a)
		print(stylize(ans, color))
		a += 1


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="Show the fizzbuzz function from A to B")
	parser.add_argument(
		"-A", "--start", help="From where the fizzbuzz starts to show. For default A = 1", type=int, default=1)
	parser.add_argument(
		"-B", "--end", help="How far the fizzbuzz is going to show. For default B = 100", type=int, default=100)
	args = parser.parse_args()

	fizzbuzz(args.start, args.end)
