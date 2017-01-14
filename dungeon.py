import random
class room():
    stuff = "none"

class dungeon:
    def rooms(x,y):
        rooms = [["room1","room2","room3","room4","room5"],
                 ["room6","room7","room8","room9","room10"],
                 ["room11","room12","room13","room14","room15"],
                 ["room16","room17","room18","room19","room20"],
                 ["room21","room22","room23","room24","room25"]]
        return rooms[x][y]

print (dungeon.rooms(1,1))
