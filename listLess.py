__author__ = 'krisleon99'
"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

def less_number(number):
  a = [100, 4, 6, 1,  5, 4, 2, 3, 4, 60, 78, 90, 6, 8, 200, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  a.sort()
  print("of the list: {}".format(a))

  mid = int(len(a)) / 2
  print(mid)
  
  if mid >= number:
    search_less(a, mid, number)
  else:
    mid2 = mid + (mid)/2
    print(mid2)
    if mid2 >= number:
      search_less(a, mid2, number)
    else:
      search_less(a, mid2, number)


def search_less(a, mid, number):
  b = []
  for i in a:
    if i < number:
     b.append(i)
  print("less than five {}".format(b))


if __name__ == '__main__':
  number = int(raw_input("enter a number"))
  less_number(number)



