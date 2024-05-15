def printBoard():
    print(f"0 | 1 | 2 ")
    print(f"--|---|---")
    print(f"3 | 4 | 5 ")
    print(f"--|---|---")
    print(f"7 | 8 | 9 ")
    

if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0]
    turn=1 #1 for x and 0 for O
    print("Welcome to Tic-tac-toe")
    while(True):
        if(turn==1):
           print("x's chance")
           value = int(input("please enter a value!"))
           xstate[value]=1
        else:
           print("O's chance")
           value = int(input("please enter a value!"))  
           ystate[value]=1

        printBoard();
        break;
