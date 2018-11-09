"""
Palindrome
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwars)
"""

__author__ = 'kris'


if __name__ == '__main__':
  palindrome = raw_input("Insert any string")
  print(palindrome)
  pal_list = list(palindrome)
  size_pal = len(pal_list)
  for i in range(0, size_pal):
    compare_a = pal_list[i]
    compare_b = pal_list[(size_pal-1)-i]
    if i+1==size_pal:
      print("es palindrome")
    else:
      if compare_a != compare_b:
        print("no es palindrome")
        break
