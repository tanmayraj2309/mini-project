# Design a project where as an input student will give a static number (between 1 to 6) and then roll the dice which randomly generate some value between 1 to 6. The winning situation arrives when the given static/fixed number exactly same to the number came after rolling the dice.
#
# User can play the game as many numbers of times he wants until user wants to exit, and whenever winning situation occur some scores must be given to the user, and these scores goes on adding if user play this game multiple number of times. Note: Dice contains face value’s (1 to 6)
#
# Hint: Make use of random.randint() function
#
# (Student is free to decide the input and output layout for this mini project)



import math
import random
loses=0
score=0
looprun=0
print("_______________________\n")
print("Welcome To Dice Game🎲")
print("_______________________\n")
while True:
  a=input(">>>Enter Your Guess 🤫:  ")
  if a.lower()=='quit':
    if score==0:
      a1="times! 😂"
    elif score==1:
      a1="time! 🥱"
    elif score==2:
      a1="times! 😃"
    else:
      a1="times! 🤩"
    print("\nThanks for playing the game. You won",score, a1 )
    exit()
  def dice_game(user_guess,loses,score):
    if user_guess>6:
      print("\n🚫🚫🚫\nEnter a valid guess within the range 1-6\n")
    else:
      print("\nRolling 🎲...")
      dice_value=random.randint(1,6)
      print("🎲"+ "="+str(dice_value))
      if user_guess==dice_value:
        print("Congratulations You won!!! 🥳\n")
        score+=1
      else:
        if loses>0:
          print("You lost again 🤕 but don't give up keep trying!😤\n")
        else:
          print("You lost 😕\n")
          loses+=1
    b=[loses,score]
    return b
  b=dice_game(int(a),loses,score)
  loses=b[0]
  score=b[1]
