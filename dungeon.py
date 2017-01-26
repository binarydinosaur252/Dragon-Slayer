import random

room1 = "room1"
room2 = "room2"
room3 = "room3"
room4 = "room4"
room5 = "room5"
room6 = "room6"
room7 = "room7"
room8 = "room8"
room9 = "room"
room10 = "room10"
room11 = "room11"
room12 = "room12"
room13 = "room13"
room14 = "room14"
room15 = "room15"
room16 = "room16"
room17 = "room17"
room18 = "room18"
room19 = "room19"
room20 = "room20"
room21 = "room21"
room22 = "room22"
room23 = "room23"
room24 = "room24"
room25 = "room25"
class room:
    def room(n,e,s,w,items):
        stuff = "Really cool stuff",items
        doors = [["north",n],["east",e],["south",s],["west",w]]
        return [doors,stuff]

class levels:
    def rooms(x,y):
        rooms = [[room1,room2,room3,room4,room5],
                 [room6,room7,room8,room9,room10],
                 [room11,room12,room13,room14,room15],
                 [room16,room17,room18,room19,room20],
                 [room21,room22,room23,room24,room25]]
        return rooms[x][y]

print (levels.rooms(4,4))
room1 = room.room(0,1,1,1,"Sword")

print (room1[1])
print (levels.rooms(0,0))
