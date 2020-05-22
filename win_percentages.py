#write a function that determines the win perctanges givin the total nums of wins and loses

def win_percentage(wins,losses):
  percentage =(wins / (wins + losses)) * 100
  return percentage

print(win_percentage(10,2))

