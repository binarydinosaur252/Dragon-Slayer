import random
import characters
from time import sleep

print "DRAGON SLAYER"
print "designed and developed by Cyrus Burt and Eric Matt" + "\n"
sleep(5)

#game intro
print "Welcome to the magical world of Kraagnord!"
sleep(5)
print "A strange and mystical world crawling with evil wizards, brave warriors and dragons!" + "\n"

#rules
print "and now for the rules."
sleep(3)
print "use the command Fight to slay evil creatures (but don't kill the good guys!)"
sleep(3)
print "use the command Pickup to take treasure and pick up things." + "\n\n\n\n\n"

#game start
name = raw_input("What is your name?: ")
name = str(name)
print "greetings, " + name + " I have a quest for you" + "\n"

print "here are your weapons" + "\n\n"

print "YOU GOT A SWORD!"
sleep(2)

todo1 = raw_input("what do you do now? : ")
if todo1 == "Explore":
   print "you look around and the wizard who gave you the sword" + "\n" "seems to have dissapeared"
elif todo1 == "Fight":
    print "You swing your sword and don't hit anything"
elif todo1 == "Pick up":
    print "You get 50 peices of gold that were hidden under a rock!"   


