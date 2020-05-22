#write a function that returns the total amount that you should pay given the cost and tip percentage

def tip(total,percentage):
  tip_amount = percentage/100
  amount = total * tip_amount
  print(amount)
  return amount