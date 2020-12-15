# Author: Charles Zhang
# Date: 12/08/2020
# Name: 5 Questions Quiz Bot

# Extras
import time
redo = 0
#for clearification Q1w = Question 1 wrong
started = False
Q1w = False
Q2w = False
Q3w = False
Q4w = False
Q5w = False
right_questions = 0
wrong_questions = 0
# Extra Functions made last minute
def congrats(right_questions):
  if right_questions == 1:
    print("Hey you got your first question right")
  elif right_questions == 2:
    print("Good job you got 2 questions correct")
  elif right_questions == 3:
    print("That your 3rd questions right :D")
  elif right_questions == 4:
    print("Let's gooo you got 4 correct")
  elif right_questions == 5:
    print("you're on fire person of non specific gender")

def wrong(wrong_questions):
  if wrong_questions == 1:
    print("It's alright it's just 1 question")
  elif wrong_questions == 2:
    print("Your score is still greater than 50%")
  elif wrong_questions == 3:
    print("You just officially dropped below 50%")
  elif wrong_questions == 4:
    print("how did you get 4 questions wrong on this quiz")
  elif wrong_questions == 5:
    print("person of non specific gender, stop messing around the next time you take the test")




# Intro
print("Hi je suis cinq questions bot\n\n")
while started == False:
  mark = 0

  start = input("to start the questions type start\n")
  if start.lower().strip("!@#$%^&*()") == "start":
   started = True
  else:
    print("...\n\n")

print("1 Rule before we start\nplease only type numbers for the math questions")
time.sleep(2)

# 5 questions
Q1 = int(input("\n\nWhat is 1 + 1?\n"))
if Q1 == 2:
  right_questions += 1
  mark += 1
  congrats(right_questions)
else:
  wrong_questions += 1
  wrong(wrong_questions)
  Q1w = True

Q2 = int(input("\nWhat is 2^2?\n"))
if Q2 == 4:
  right_questions += 1
  mark += 1
  congrats(right_questions)
else:
  wrong_questions += 1
  wrong(wrong_questions)
  Q2w = True

Q3 = input("\nWhat is Obama's last name?\n").strip("!@#$%^&*()_+-=<>?,./").lower()
if Q3 == "obama":
  right_questions += 1
  mark += 1
  congrats(right_questions)
elif Q3 == "care":
  right_questions += 1
  mark += 2
  print("Congrats you get an extra point")
else:
  wrong_questions += 1
  wrong(wrong_questions)
  Q3w = True
Q4 = int(input("\nWhat is 9 + 10?\n"))
if Q4 == 19:
  right_questions += 1
  mark += 1
  congrats(right_questions)
elif Q4 == 21:
  right_questions += 1
  mark += 2
  print("Congrats you get an extra point")
else:
  wrong_questions += 1
  wrong(wrong_questions)
  Q4w = True
Q5 = input("\nIs 21 the answer to life?\n").strip("!@#$%^&*()_+-=").lower()
if Q5 == "yes" or Q5 == "true":
  right_questions += 1
  mark += 1
  congrats(right_questions)
else:
  wrong_questions += 1
  wrong(wrong_questions)
  Q5w = True

# Final Score
print(f"\n\n Your final score is...")
time.sleep(2)
print(f"{mark}/5")
time.sleep(1)
if Q1w == False and Q2w == False and Q3w == False and Q4w == False and Q5w == False:
  redo = "nothing is wrong"
else:
  redo = False
while redo == False:
  redo = input("\nIf you want to retry the answers you got wrong type redo if not type no\n").lower().strip("!@#$%^&*()_+-=<>?,./")
  if redo == "redo":
    redo = True
  elif redo == "no" or redo == "nope" or redo == "nah":
    break
  else:
    print("sorry I don't understand you")
    redo = False

old_mark = mark

# get them to redo wrong answers
if redo == True:
  print("\nnow you get 3 extra tries for each question you've gotten, before we give you the answer")
  # -----For Question 1-----
  Q1_counter = 3
  while Q1w:
    if Q1_counter <= 3 and Q1_counter > 0:
      Q1 = int(input("\n\nWhat is 1 + 1?\n"))
      if Q1 == 2:
        print("Correct!!")
        mark += 1
        Q1w = False
      else:
        print("nah you're still wrong\n  try again")
        Q1_counter -= 1
    elif Q1_counter <= 0:
      print("Sorry you have gotten this question more than three times")
      print("\nThe answer was 2")
      Q1w = False
  # -----For Question 2-----
  Q2_counter = 3
  while Q2w:
    if Q2_counter <= 3 and Q2_counter > 0:
      Q2 = int(input("\nWhat is 2^2?\n"))
      if Q2 == 4:
        print("Correct!!")
        mark += 1
        Q2w = False
      else:
        print("nah you're still wrong\n  try again")
        Q2_counter -= 1
    elif Q2_counter <= 0:
      print("Sorry you have gotten this question more than three times")
      print("\nThe answer was 4")
      Q2w = False
  # -----For Question 3-----
  Q3_counter = 3
  while Q3w:
    if Q3_counter <= 3 and Q3_counter > 0:
      Q3 = input("\nWhat is Obama's last name?\n").strip("!@#$%^&*()_+-=:").lower()
      if Q3 == "obama":
        print("Correct!!")
        mark += 1
        Q3w = False
      else:
        print("Sorry you're still wrong try again")
        Q3_counter -= 1
    elif Q3_counter <= 0:
      print("Sorry you have gotten this question more than three times")
      print("\nThe answer was Obama")
      Q3w = False
  # -----For Question 4-----
  Q4_counter = 3
  while Q4w:
    if Q4_counter <= 3 and Q4_counter > 0:
      Q4 = int(input("\nWhat is 9 + 10?\n"))
      if Q4 == 19:
        print("Correct!!")
        mark += 1
        Q4w = False
      else:
        print("you got this question wrong again????")
        Q2_counter -= 1
    elif Q4_counter <= 0:
      print("how did you get this question wrong more than 3 times???")
      print("you know the answer was 19")
      Q4w == False
  # -----For Question 5-----
  Q5_counter = 3
  while Q5w:
    if Q5_counter <= 3 and Q5_counter > 0:
      Q5 = input("\nis 21 the answer to life?\n").strip("!@#$%^&*()_+-=").lower()
      if Q5 == "yes" or Q5 == "true":
        print("Correct!!")
        mark += 1
        Q5w = False
      else:
        print("did you make a typo?? how did you get this question wrong")
        Q5_counter -= 1
    elif Q5_counter <= 0:
      print("did you serously get this question wrong more than 3 times???\nThis was a yes or no question")
      print("The answer was clearly \"yes\"")
      Q5w = False
  time.sleep(1)
  print(f"\n\nyour new mark is {mark}/5")
  time.sleep(1)
  print(f"Your old mark was {old_mark}/5")


if mark == 7:
  print("Congrats on getting all the extra points, but the cake is a lie")
elif mark >= 5:
  print("\ndid you know that there are 2 extra points available?, you can try to get 7/5 for a cake, on your next attempt on this 5 question quiz")

# Goodbye message
time.sleep(2)
print("\n...goodbye")