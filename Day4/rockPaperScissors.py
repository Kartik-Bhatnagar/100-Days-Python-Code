rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

def findWinner(c1,c2):
  # 'Rock' > 'Scissors'
  #'Paper' > 'Rock'
  #'Scissors' > 'Paper'
  winnerDict = {
    'Rock' : {
      'Paper':'win', 'Scissors' :'loose' 
    },
    'Paper' :{
      'Scissors' :'win', 'Rock' :'loose'
    },
    'Scissors' :{
      'Rock' :'win', 'Paper' :'loose'
    } 
  }
  if c1 in winnerDict or c2 in winnerDict:
    if winnerDict[c1][c2] == 'win':
      return (c2,'user2')
    else:
      return (c1,'user1')
  else:
    print("Wrong choices")
    return 0,0
choiceException = "Please type valid option"
validChoice, playOn = False, False
choices = {0: ['Rock', rock], 1: ['Paper', paper], 2: ['Scissors', scissors]}
while (not validChoice) or (not playOn):
    try:
        userChoice = (int(
            input(
                "What do you choose? Type 0 for Rock, 1 for Paper )or 2 for Scissors."
            )))

    except:
        print(choiceException)
        continue  
    if userChoice in [0, 1, 2]:
        validChoice = True
        print("Very Good !! You have chosen {} \n {}".format(
          choices[userChoice][0], choices[userChoice][1]))
     
    else:
        print(choiceException)
        continue
    compChoice = random.randint(0,2)
    print(f"Computer has choosen {choices[compChoice][0]} \n {choices[compChoice][1]}")
    if compChoice == userChoice:
      print("It's a Tie \n")
      continue
    else: #either one is the winner
      winChoice, winUser = findWinner(choices[userChoice][0],choices[compChoice][0])
    if winUser == 'user1':
      print("Congratulations! 🎉 You have won")
    elif winUser == 'user2' : 
      print("Computer won . Better Luck Next Time !")
  
    try:
      endGame = int(input("type 0 to end this game or any other number to continue"))
      
      if endGame == 0:
        playOn = True
  
    except:
      continue
#furure work : add a score board 
    