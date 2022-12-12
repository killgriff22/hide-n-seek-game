from pygame import *
class player:
    def __init__(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        self.speed=1
    def move(self,key,map):
        map[self.player_y][self.player_x] = 0
        if key in [K_UP,K_w]:
            if map[self.player_y-self.speed][self.player_x] == 1:
                map[self.player_y][self.player_x] = 2
                return map
            map[self.player_y-self.speed][self.player_x] = 2
            self.player_y-=self.speed
        elif key in [K_DOWN,K_s]:
            if map[self.player_y+self.speed][self.player_x] == 1:
                map[self.player_y][self.player_x] = 2
                return map
            map[self.player_y+self.speed][self.player_x] = 2
            self.player_y+=self.speed
        elif key in [K_LEFT,K_a]:
            if map[self.player_y][self.player_x-self.speed] == 1:
                map[self.player_y][self.player_x] = 2
                return map
            map[self.player_y][self.player_x-self.speed] = 2
            self.player_x -= self.speed
        elif key in [K_RIGHT,K_d]:
            if map[self.player_y][self.player_x+self.speed] == 1:
                map[self.player_y][self.player_x] = 2
                return map
            map[self.player_y][self.player_x+self.speed] = 2
            self.player_x += self.speed
        return map