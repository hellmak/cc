#Write your function here

def same_values(a,b):
  output  = []
  for i in range(len(a)):
    if a[i] == b[i]:
      output.append(i)
  return output

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#oneliner:
print((lambda a, b: [i for i, x in enumerate(a) if x == b[i]])([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
