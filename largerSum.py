#codecademy challenge to sum the nums in a list and return the list with the larger sum
def larger_sum(lst1,lst2):
  lst1sum = 0
  lst2sum = 0
  for num in lst1:
    lst1sum += num
  for num in lst2:
    lst2sum += num
  if lst1sum > lst2sum:
    return lst1
  elif lst1sum < lst2sum:
    return lst2
  else: 
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))