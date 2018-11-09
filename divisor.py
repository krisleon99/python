__author__ = 'krisleon99'
"""
Divisors Solutions
Exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

def div(number):
  divisors = []
  for i in range(1, number+1):
      divisor = number/i
      if number % i == 0:
        print i
        divisors.append(i)
  return divisors

if __name__ == '__main__':
  num = int(raw_input("Enter your number"))
  print(div(num))

