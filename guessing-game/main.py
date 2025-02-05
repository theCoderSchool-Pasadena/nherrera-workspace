import random
print ("Welcome to the guessing game!")
print("Guess a number from 1-100.")
print("You will have five tries to guess the number.")
print("It will tell you if your guess was to high or to low.\n")
print("your difficulty levels are hard and normal")
print("type what difficulty you want")
dif=input("select your difficulty: ")
if dif == "hard":
  lives=3
else:
  lives=5
numberToGuess=random.randint(1,100)
while lives>0:
  guess=int(input("guess your number now: "))
  if guess<numberToGuess:
    print("your guess was to low")
    lives-=1
  if guess>numberToGuess:
    print("your guess was to high")
    lives-=1
  if guess==numberToGuess:
    print("congratulations you guessed correctly")
    break
if lives==0:
  print("sorry you have run out of lives:(the answer was\n")
  print(numberToGuess)
  
