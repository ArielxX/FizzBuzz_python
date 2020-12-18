

def get_fizzbuzz(a):
    '''
    Return the FizzBuzz for the number a
            'Fizz' if a is divisible by 3 and not by 5
            'Buzz' if a is divisible by 5 and not by 3
            'FizzBuzz' if a is divisible by 3 and 5
            a in any other case
    '''
    if a % 15 == 0:
        return 'FizzBuzz'
    if a % 3 == 0:
        return 'Fizz'
    if a % 5 == 0:
        return 'Buzz'
    return str(a)


def fizzbuzz(a, b):
    # Print the Fizzbuzz for every number between a and b
    while a <= b:
        print(get_fizzbuzz(a))
        a += 1


if __name__ == '__main__':
    fizzbuzz(1, 100)
