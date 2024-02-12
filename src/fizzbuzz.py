
def fizzbuzz(number):
  if isFizzBuzz(number):
    return 'FizzBuzz'
  if isFizz(number):
    return 'Fizz'
  if isBuzz(number) :
    return 'Buzz'  
  return str(number)

def isFizzBuzz(number):
    return isFizz(number) and isBuzz(number)

def isBuzz(number):
    return number % 5 == 0

def isFizz(number):
    return number % 3 == 0
