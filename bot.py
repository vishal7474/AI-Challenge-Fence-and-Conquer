import random


EMPTY = 0

class player:
    def __init__(self):
        self.step=0
        self.count = 0
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.count5 = 0
        self.count6 = 0
        self.count7 = 0
        self.count8 = 0
        self.count9 = 0
        self.count10 = 0
        self.count11 = 0
        self.count12 = 0
        self.count13 = 0

    def move(self,B,N,cur_x,cur_y):

        lis = [(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]
        if (self.count != 20):
            self.count += 1
            return lis[self.count-1]
        else:
            return self.move2(B,N,cur_x,cur_y)

    def move2(self,B,N,cur_x,cur_y):

        lis = [(0,-1),(0,-1),(0,-1),(0,-1),(0,-1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1)]
        if (self.count1 != 15):
            self.count1 += 1
            return lis[self.count1-1]
        else:
            return self.move3(B,N,cur_x,cur_y)

    def move3(self,B,N,cur_x,cur_y):

        lis = [(1,0),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]
        if (self.count2 != 15):
            self.count2 += 1
            return lis[self.count2-1]
        else:
            return self.move4(B,N,cur_x,cur_y)

    def move4(self,B,N,cur_x,cur_y):

        lis = [(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
        if (self.count3 != 15):
            self.count3 += 1
            return lis[self.count3-1]
        else:
            return self.move5(B,N,cur_x,cur_y)


    def move5(self,B,N,cur_x,cur_y):

        lis = [(1,0),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]
        if (self.count4 != 15):
            self.count4 += 1
            return lis[self.count4-1]
        else:
            return self.move6(B,N,cur_x,cur_y)

    def move6(self,B,N,cur_x,cur_y):

        lis = [(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
        if (self.count5 != 15):
            self.count5 += 1
            return lis[self.count5-1]
        else:
            return self.move7(B,N,cur_x,cur_y)

    def move7(self,B,N,cur_x,cur_y):

        lis = [(1,0),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]
        if (self.count6 != 15):
            self.count6 += 1
            return lis[self.count6-1]
        else:
            return self.move8(B,N,cur_x,cur_y)

    def move8(self,B,N,cur_x,cur_y):

        lis = [(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
        if (self.count7 != 15):
            self.count7 += 1
            return lis[self.count7-1]
        else:
            return self.move9(B,N,cur_x,cur_y)

    def move9(self,B,N,cur_x,cur_y):

        lis = [(1,0),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]
        if (self.count8 != 15):
            self.count8 += 1
            return lis[self.count8-1]
        else:
            return self.move10(B,N,cur_x,cur_y)

    def move10(self,B,N,cur_x,cur_y):

        lis = [(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
        if (self.count9 != 15):
            self.count9 += 1
            return lis[self.count9-1]
        else:
            return self.move11(B,N,cur_x,cur_y)

    def move11(self,B,N,cur_x,cur_y):

        lis = [(1,0),(1,0),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]
        if (self.count10 != 15):
            self.count10 += 1
            return lis[self.count10-1]
        else:
            return self.move12(B,N,cur_x,cur_y)

    def move12(self,B,N,cur_x,cur_y):

        lis = [(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(0,-1),(0,-1),(0,-1),(0,-1),(0,-1)]
        if (self.count11 != 15):
            self.count11 += 1
            return lis[self.count11-1]
        else:
            return self.move1(B,N,cur_x,cur_y)

    def move1(self,B,N,cur_x,cur_y):
        self.step+=1

        if B[cur_x][(cur_y+N+1)%N]==0:
            return (0,1)

        if B[cur_x][(cur_y+N-1)%N]==0:
            return (0,-1)

        if B[(cur_x+1)%N][cur_y]==0:
            return (1,0)

        if B[(cur_x+N-1)%N][cur_y]==0:
            return (-1,0)

        return self.closest_empty(B,N,cur_x,cur_y) # random.choice([(1,0),(0,1),(-1,0),(0,-1)])



    def closest_empty(self,B,N,cur_x,cur_y):
        dis=2*N+1
        best = {"x":cur_x,"y":cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i
                        best["y"] = j

        # Pick the direction to go in

        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)


        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)


        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)


        return (0,0)



#p2 = player_two()
#for i in range(100):
#    p2.move()
