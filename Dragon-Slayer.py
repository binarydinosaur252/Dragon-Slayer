import random
import characters
from time import sleep

with open ('asciiart/dragon2') as dragon2:
    for line in dragon2:
        print (line, end ='')
print ("Designed and developed by Cyrus Burt and Eric Matt" + "\n")
sleep(5)

#game intro
print ("Welcome to the magical world of Kraagnord!")
sleep(5)
print ("A strange and mystical world crawling with evil wizards, brave warriors and dragons!" + "\n")

#rules
print ("and now for the rules.")
sleep(3)
print ("use the command Fight to slay evil creatures (but don't kill the good guys!)")
sleep(3)
print ("use the command Get to take treasure and pick up things.")
sleep(3)
print ("use the command Look to see what is in the room or look at specific items in the room" + "\n\n\n\n\n")

#game start
name = input("What is your name?: ")
name = str(name)
print ("greetings, " + name + " I have a quest for you" + "\n")

sleep(2)

print ("here are your weapons" + "\n\n")

sleep(1)

print ("YOU GOT A SWORD!")
with open ('asciiart/sword1') as sword1:
    for line in sword1:
        print (line, end ='')

sleep(2)

leave = "n"
while leave != "y":
   todo1 = input("what do you do now? : ")
   if todo1 == ("Explore"):
      print ("you look around and the wizard who gave you the sword" + "\n" "seems to have dissapeared")
      leave = input("do you want to leave y/n: ")
   elif todo1 == ("Fight"):
      print ("You swing your sword and don't hit anything")
   elif todo1 == ("Get"):
      print ("You get 50 peices of gold that were hidden under a rock!")
   elif todo1 == ("Look"):
      print ("You see stuff in the room!")
   else :
      print ("I don't know how to " +todo1+ " because my programers didn't want to spend the time to make that work")
      print ("You can Get, Look, Explore, and Fight")
             
print ("You walk outside and see the a little town busy with people")

leave = "n"
while leave != "y":
    todo2 = input("You walk into the town and see an old woman selling magic items. What do you do now warrior? : ")
    if todo2 == ("Explore"):
        print ("You walk through the town and don't see much.")
    elif todo2 == ("Fight"):
        print ("You start to swing your sword and stab the old woman selling potions")
    elif todo2 == ("Talk"):
        print ("The old woman sees you and runs off leaving behind" + "\n" "A POTION OF HEALING")
    elif todo2 == ("Leave"):
        leave = input("do you want to leave y/n: ") 
    
