#codecademy code challenge question; return odd indices of a list

def odd_indices(lst):
  newlst=[]
  for i in range(len(lst)):
    if i % 2 == 1:
      newlst.append(lst[i])
  return newlst

    
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))