


# FizzBuzz

Simple [FizzBuzz](http://wiki.c2.com/?FizzBuzzTest) project using python3

## Getting Started

Install [pipenv](https://pypi.org/project/pipenv/) to manage the virtual environment for the project

```bash
pip install pipenv
```

Then set the virtual environment on and install all the dependencies

```bash
pipenv install
```

## Running Tests

Run the unit tests using [pytest](https://docs.pytest.org/en/stable/)

```bash
pipenv run python -m pytest
```

## Run the project

Move into the **fizzbuzz** folder and run the **fizzbuzz** program

```bash
cd fizzbuzz
python fizzbuzz.py
```

### Using arguments

There are two optional arguments configured with the use of [argparse](https://docs.python.org/3/library/argparse.html) to specify the limits of the range to be displayed

**--start (-A)**: From where the fizzbuzz starts to show. For default `A = 1`

**--end (-B)**: How far the fizzbuzz is going to show. For default `B = 100`

For example:
```bash
$ cd main
$ python FizzBuzz.py --start 5 --end 10
Buzz  
Fizz  
7  
8  
Fizz  
Buzz
```

