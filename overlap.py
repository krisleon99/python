"""
List Overlap
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

__author__ = 'kris'

import random

if __name__ == '__main__':
  a = random.sample([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5)
  b = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 8)
  print("list a: {}".format(a))
  print("list of b: {}".format(b))
  my_set_a = set(a)
  my_set_b = set(b)
  print(my_set_a.intersection(my_set_b))
  print(my_set_a & my_set_b)
 
