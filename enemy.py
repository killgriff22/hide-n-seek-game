import random,pygame
class enemyAI:
    def __init__(self,enemy_x,enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.x_threshold = 30
        self.y_threshold = 60
        self.attempts_before_random = 3
        self.attempts=0
    def update(self,map):
        map[self.enemy_y][self.enemy_x] = 0
        movedirection = int(random.random()*4//1)
        if movedirection == 0:
            try:map[self.enemy_y-1][self.enemy_x]
            except:return map
            if map[self.enemy_y-1][self.enemy_x] == 1:
                map[self.enemy_y][self.enemy_x] = 3
                return map
            map[self.enemy_y-1][self.enemy_x] = 3
            self.enemy_y-=1
        elif movedirection == 1:
            try:map[self.enemy_y+1][self.enemy_x]
            except:return map
            if map[self.enemy_y+1][self.enemy_x] == 1:
                map[self.enemy_y][self.enemy_x] = 3
                return map
            map[self.enemy_y+1][self.enemy_x] = 3
            self.enemy_y+=1
        elif movedirection == 2:
            try:map[self.enemy_y][self.enemy_x-1]
            except:return map
            if map[self.enemy_y][self.enemy_x-1] == 1:
                map[self.enemy_y][self.enemy_x] = 3
                return map
            map[self.enemy_y][self.enemy_x-1] = 3
            self.enemy_x -= 1
        elif movedirection == 3:
            try:map[self.enemy_y][self.enemy_x+1]
            except:return map
            if map[self.enemy_y][self.enemy_x+1] == 1:
                map[self.enemy_y][self.enemy_x] = 3
                return map
            map[self.enemy_y][self.enemy_x+1] = 3
            self.enemy_x += 1
        return map
    def pathfind_to(self,location:pygame.rect,map,frame,override=False):
        if self.attempts >= self.attempts_before_random:
            self.attempts = 0
            return self.update(map)
        old=(self.enemy_x,self.enemy_y)
        map[self.enemy_y][self.enemy_x] = 0
        x1,y1 = self.enemy_x,self.enemy_y
        x2,y2 = location
        if frame%self.x_threshold:
            if x1<x2:
                self.enemy_x+=1
            elif x2<x1:
                self.enemy_x-=1
        if frame%self.y_threshold:
            if y1<y2:
                self.enemy_y+=1
            elif y2<y1:
                self.enemy_y-=1
        if map[self.enemy_y][self.enemy_x] == 1:
            new = (self.enemy_x,self.enemy_y)
            self.enemy_x,self.enemy_y=old
            if (new[0] > old[0] and old[1]==new[1]) or (new[0] < old[0] and old[1]==new[1]):
                for y in range(50):
                    if not map[y][self.enemy_x]:
                       if y>self.enemy_y:
                           self.enemy_y+=1
                           break 
                       elif y<self.enemy_y:
                           self.enemy_y-=1
                           break
            elif (new[1]>old[1] and new[0]==old[0]) or (new[1]<old[1] and new[0]==old[0]):
                for x in range(50):
                    if not map[self.enemy_y][x]:
                       if x>self.enemy_x:
                           self.enemy_x+=1
                           break 
                       elif x<self.enemy_x:
                           self.enemy_x-=1
                           break
        map[self.enemy_y][self.enemy_x] = 3
        new = (self.enemy_x,self.enemy_y)
        if new == old and not new == location:
            self.attempts += 1
        return map