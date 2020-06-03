#codecademy challenge question to sum the nums in a lst while they total less than 9000

def over_nine_thousand(lst):
  if len(lst) == 0:
    return 0
  sum = 0
  for num in lst:
    sum += num
    if sum > 9000:
      break
  return sum