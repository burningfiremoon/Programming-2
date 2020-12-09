# Author: Charles Zhang
# Date: 12/08/2020
# Name: 5 Questions Bot

# Extras
started = False
mark = 0
Q1w = False
Q2w = False
Q3w = False
Q4w = False
Q5w = False
# Intro
print("Hi je suis cinq questions bot\n\n")
while not started:
    mark = 0
    start = input("to start the questions type start\n")
    if start.lower().strip("!@#$%^&*()") == "start":
        started = True
    else:
        print("...\n\n")

# -----5 questions-----
Q1 = int(input("\n\nWhat is 1 + 1?\n"))
if Q1 == 2:
    print("Correct!!")
    mark += 1
else:
    print("nah you're wrong")
    Q1w = True

Q2 = int(input("\nWhat is 2^2?\n"))
if Q2 == 4:
    print("Correct!!")
    mark += 1
else:
    print("nah you're wrong")
    Q2w = True
Q3 = input("\nWhat is Obama's last name?\n").strip("!@#$%^&*()_+-=:").lower()
if Q3 == "obama":
    print("Correct!!")
    mark += 1
elif Q3 == "care":
    mark += 2
    print("Congrats you get an extra point")
else:
    print("nah you're wrong")
    Q3w = True
Q4 = int(input("\nWhat is 9 + 10?\n"))
if Q4 == 19:
    print("Correct!!")
    mark += 1
elif Q4 == 21:
    mark += 2
    print("Congrats you get an extra point")
else:
    print("nah you're wrong")
    Q4w = True
Q5 = input("\nis 21 the answer to life?\n").strip("!@#$%^&*()_+-=").lower()
if Q5 == "yes":
    print("Correct!!")
    mark += 1
else:
    print("nah you're wrong")
    Q5w = True

# Final Score
print(f"\n\n Your final score is {mark}/5")
redo = input("\nIf you want to retry the answers you got wrong type redo").lower().strip("!@#$%^&*()_+-=<>?,./")

# get them to redo wrong answers
if redo == "redo":
  print("now you get 3 extra tries for each question before we give you the answer")
  Q3_counter = 3
  Q4_counter = 3
  Q5_counter = 3
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
                Q1w = False
            else:
                print("nah you're wrong")
                Q1_counter -= 1
        elif Q2_counter <= 0:
            print("hello world")





# Goodbye message
print("\n...goodbye")
