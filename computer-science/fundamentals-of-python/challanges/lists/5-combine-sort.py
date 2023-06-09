"""
Write a function named combine_sort that has two parameters named my_list1 and my_list2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""
#Write your function here
def combine_sort(my_list1, my_list2):
  return sorted( my_list1 + my_list2 )

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#alternative solution, seems to be atleast as clear and not include the extra work of writing a function?:
print(sorted([4, 10, 2, 5] + [-10, 2, 5, 10]))
