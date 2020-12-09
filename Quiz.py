# Author: Charles Zhang
# Date: 12/08/2020
# Name: 5 Questions Bot

# Extras
started = False
# Intro
print("Hi je suis cinq questions bot\n\n")
while started == False:
  mark = 0

  start = input("to start the questions type start\n")
  if start.lower().strip("!@#$%^&*()") == "start":
   started = True
  else:
    print("...\n\n")

# 5 questions
Q1 = int(input("\n\nWhat is 1 + 1?\n"))
if Q1 == 2:
  print("Correct!!")
  mark += 1
else:
  print("nah you're wrong")

Q2 = int(input("\nWhat is 2^2?\n"))
if Q2 == 4:
  print("Correct!!")
  mark += 1
else:
  print("nah you're wrong")
Q3 = input("\nWhat is Obama's last name?\n").strip("!@#$%^&*()_+-=:").lower()
if Q3 == "obama":
  print("Correct!!")
  mark += 1
elif Q3 == "care":
  mark += 2
  print("Congrats you get an extra point")
else:
  print("nah you're wrong")
Q4 = int(input("\nWhat is 9 + 10?\n"))
if Q4 == 19:
  print("Correct!!")
  mark += 1
elif Q4 == 21:
  mark += 2
  print("Congrates you get an extra point")
else:
  print("nah you're wrong")
Q5 = input("\nis 21 the answer to life?\n").strip("!@#$%^&*()_+-=").lower()
if Q5 == "yes":
  print("Correct!!")
  mark += 1
else:
  print("nah you're wrong")

# Final Score
print(f"\n\n Your final score is {mark}/5")

# Goodbye message
print("\n...goodbye")