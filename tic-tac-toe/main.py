def sum(a,b,c):
    return a+b+c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("X won the match")
            return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("O won the match")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn=1 #1 for x and 0 for O
    print("Welcome to Tic-tac-toe")
    while(True):
        printBoard(xstate,zstate)
        if(turn==1):
           print("x's chance")
           value = int(input("please enter a value: "))
           xstate[value]=1
        else:
           print("O's chance")
           value = int(input("please enter a value:1 "))  
           zstate[value]=1
           cwin=checkwin(xstate,zstate)
           if(cwin!=-1):
               print("Match Over! ")
               break
           turn=1-turn

        
