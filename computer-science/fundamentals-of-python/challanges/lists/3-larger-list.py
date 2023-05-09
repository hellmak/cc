"""
Write a function named larger_list that has two parameters named my_list1 and my_list2.

The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.
"""
#Write your function here

def larger_list(a,b):
  la, lb  = len(a), len(b)
  if la < lb:
   return b[-1]
  elif la => lb: #can just be written "else" but this is more readable
   return a[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
