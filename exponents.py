#codecademy code challenge that loops through two lst and returns a new lst with the base times each power in exponent lst
def exponents(bases,powers):
  lst=[]
  for base in bases:
    for power in powers:
      lst.append(base ** power)
  return lst
  


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))