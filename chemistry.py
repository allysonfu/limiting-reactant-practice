#Import necessary modules/libraries
import random
import numpy as np 
import math

#Store a randomly-generated float between 0.5 and 5 as x
x = np.random.uniform(0.5, 5)

#Truncate x to be more reasonable
def truncate(number, digits) -> float:
  stepper = 10.0 ** digits
  return math.trunc(stepper * x) / stepper
x = truncate(x, 2)

#Initialize userTries variable to 0
userTries = 0

#Choose prompt output based on randomly-generated number (1/5 chance for each)
prompt = random.random()

#Prompt #1
if prompt <= 0.25:
  print("""Consider a gas-phase reaction that proceeds according to the following balanced chemical equation: N₂ + 3H₂ -> 2NH₃.\n"""
  """Equal moles of each reactant are combined in a vessel, and """+ str(x) + 
  """ moles of the excess reactant remain at the end of the reaction.""")
  reactant1Name = str("N₂")
  reactant2Name = limitingReactant = str("H₂")
  productName = str("NH₃")
  #Compute answers & round them to 2 decimal places
  answer1 = round(x*1.5, 2)
  answer2 = round(x*1.5, 2)
  answerP = round(x, 2)

#Prompt #2
elif prompt > 0.25 and prompt <= 0.5:
  print("""Consider a gas-phase reaction that proceeds according to the following balanced chemical equation: 2SO₂ + O₂ -> 2SO₃\n"""
  """Equal moles of each reactant are combined in a vessel, and """+ str(x) + 
  """ moles of the excess reactant remain at the end of the reaction.""")
  reactant1Name = limitingReactant = str("SO₂")
  reactant2Name = str("O₂")
  productName = str("SO₃")
  #Compute answers & round them to 2 decimal places
  answer1 = round(x*2, 2)
  answer2 = round(x*2, 2)
  answerP = round(x*2, 2)

#Prompt #3
elif prompt > 0.5 and prompt <= 0.75:
  print("""Consider a gas-phase reaction that proceeds according to the following balanced chemical equation: Cl₂ + 3F₂ -> 2ClF₃\n"""
  """Equal moles of each reactant are combined in a vessel, and """+ str(x) + 
  """ moles of the excess reactant remain at the end of the reaction.""")
  reactant1Name = str("Cl₂")
  reactant2Name = limitingReactant = str("F₂")
  productName = str("ClF₃")
  #Compute answers & round them to 2 decimal places
  answer1 = round(x*1.5, 2)
  answer2 = round(x*1.5, 2)
  answerP = round(x, 2)

#Prompt #4
else:
  print("""Consider a gas-phase reaction that proceeds according to the following balanced chemical equation: 2H₂ + O₂ -> 2H₂O\n"""
  """Equal moles of each reactant are combined in a vessel, and """+ str(x) + 
  """ moles of the excess reactant remain at the end of the reaction.""")
  reactant1Name = limitingReactant = str("H₂")
  reactant2Name = str("O₂")
  productName = str("H₂O")
  #Compute answers & round them to 2 decimal places
  answer1 = round(x*2, 2)
  answer2 = round(x*2, 2)
  answerP = round(x*2, 2)

#Store a randomly-generated float between 0.0 and (less than) 1.0 as question
question = random.random()

#Choose question output based on randomly-generated number (50/50 chance for either)
if question < 0.5: 
  print("To two decimal places, how many moles of each reactant are present at the beginning of the reaction?")
  user1 = float(input(reactant1Name + ": "))                              #Asks for user to input answer for first reactant
  user2 = float(input(reactant2Name + ": "))                              #Asks for user to input answer for second reactant

  while user1 != answer1 or user2 != answer2:                             #Runs loop while either user answers are incorrect
    userTries += 1                                                        #Counts number of times user imputs incorrect answer
    if userTries == 3:                                                    #Displays hint after third user try
      print("Hint: " + limitingReactant + " is the limiting reactant")
    if user1 != answer1 and user2 == answer2:                             #Asks for user to input answer for first reactant if previously incorrect
      print("Please check " + reactant1Name)
      user1 = float(input(reactant1Name + ": "))
    elif user1 == answer1 and user2 != answer2:                           #Asks for user to input answer for second reactant if previously incorrect
      print("Please check " + reactant2Name)
      user2 = float(input(reactant2Name + ": "))
    elif user1 != answer1 and user2 != answer2:                           #Asks for user to input answer for both reactants if previously incorrect
      print("Please check both answers")
      user1 = float(input(reactant1Name + ": "))
      user2 = float(input(reactant2Name + ": "))
  
  if user1 == answer1 and user2 == answer2:                               #Check whether user answer is correct
    print("Correct!")

elif question >= 0.5:
  print("To two decimal places, how many moles of the product is produced?")
  userP = float(input(productName + ": "))                                #Asks for user to input answer for product

  while userP != answerP:                                                 #Runs loop while user answer is incorrect
    userTries += 1                                                        #Counts number of times user imputs incorrect answer
    if userTries == 3:                                                    #Displays hint after third user try
      print("Hint: " + limitingReactant + " is the limiting reactant")
    else:
      print("Please check your answer")
      userP = float(input(productName + ": "))                            #Asks for user to input answer for product if previously incorrect
  
  if userP == answerP:                                                    #Checks whether user answer is correct
    print("Correct!")
