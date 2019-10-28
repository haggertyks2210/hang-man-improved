#Kaiden Haggerty
#Period 1
import random
print("Welcome to Hangman")
Words= "arizona", "government", "crazy", "man", "spider", "jones", "freedom"
Mwords= list(Words)
guessList=[]
Right=[]
Wrong=[]
Mwords=random.choice(Words)
for letter in Mwords:
	Right.append("_")
print(Right)

letter=input("Enter a letter: ")


misses=0

while True:
 if letter in Words:
  index= Mwords.index(letter)
  Right.pop(int(index))
  Right.insert(int(index),letter)
  print("The letter is in the secret word")
  print(Right)
 
 
 else:
  misses=misses+1
  print(Wrong)
  
  