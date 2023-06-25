#Write your function here

"""misunderstood the task, this did solve what I thought they wanted.
def exponents(bases,powers):
  expo = []
  for a in range(0, len(bases)):
    expo.append(bases[a] ** powers[a])
  return expo
    """
def exponents(bases,powers):
  expo = []
  for a in range(0, len(bases)):
    for b in range(0, len(powers)):
      expo.append(bases[a] ** powers[b])
  return expo

# not mine, but cool af code -->
#exponents = lambda bases, powers: [bases[a] ** powers[b] for a in range(len(bases)) for b in range(len(powers))]

""" and this:
def exponents(bases, powers):
    return [bases[a] ** powers[b] for a in range(len(bases)) for b in range(len(powers))]
"""


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
