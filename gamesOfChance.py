import random

money = 100

#Write your game of chance functions here
def heads_or_tails(bet,call):
  global money
  if bet > money:
    print("Sorry you can't bet that much! You don't have enough money")
  else:
    num = random.randint(1,2)
    coin = ''
    if num % 2 == 0:
      coin = 'heads'
    else:
      coin = 'tails'
    if call == coin:
      money += bet
      print('Congrats the coin was ', coin, ' and you called it correct! You win ', bet, 'You have ', money, '!')
    else:
      money -= bet
      print('Sorry the coin was ', coin, ' and you called it incorrectly. You lost ', bet, ' amount. You have ', money, 'left')

def Cho_Han(guess,bet):
  num1 = random.randint(1,6)
  num2 = random.randint(1,6)
  sum = num1 + num2
  global money
  if bet > money:
    print("Sorry you can't bet that much! You don't have enough money")
  else:
    if sum % 2 == 0:
      if guess == 'even':
        money += bet
        print('You won! The dice total was', sum, 'You won', bet,'.You now have ', money)
      else:
        money -= bet
        print ('Sorry you lost. The dice total was', sum, 'You lost',bet, 'You now have', money)
    if sum % 2 != 0:
      if guess == 'odd':
        money += sum
        print('You won! The dice total was', sum, 'You won', bet, '. You now have ', money)
      else:
        money -= sum
        print ('Sorry you lost. The dice total was', sum, 'You lost', bet, 'You now have', money)

def random_card(bet):
  user = random.randint(1,12)
  computer = random.randint(1,12)
  global money
  if user > computer:
    money += bet
    print('Yay your card was higher! You won your bet:', bet, 'and now you have ', money)
  elif user < computer:
    money -= bet
    print('Sorry you card was lower! You lost your', bet, 'and now you have ', money)
  else:
    money += (bet / 2)
    print('Its a tie, You win half your bet: ', bet, 'You now have', money)

def roulette(bet,choice):
  num = random.randint(0,37)
  global money
  if bet > money:
    print("Sorry you can't bet that much! You don't have enough money")
  else:
    if num == 37:
      num = '00'
    if choice == num:
      money += (bet * 35)
      print('Congrats you won! The number you choose', choice, 'was choosen! You now have', money)
    elif choice == 'even':
      if num % 2 == 0:
        money += bet
        print('Yay you won! The number was even and you won your bet:', bet, 'You now have', money)
      else:
        money -= bet
        print('Sorr you lost. The number was odd. You now have', money, 'money.')
    elif choice == 'odd':
      if not num % 2 == 0:
        money += bet
        print('Yay you won. The number was odd and you won your bet:', bet, 'You now have', money)
      else:
        money -= bet
        print('Sorry you lost. The number was even. You now have ', money, 'money left.')
  
#Call your game of chance functions here
heads_or_tails(20000,'heads')
Cho_Han('even',20000)
random_card(20)
roulette(5000,'odd')