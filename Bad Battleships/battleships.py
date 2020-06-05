import time                                                                 # lets us play with time
import random

plist1=[["~","~","~","~","~","~","~","~"],                                  # multidimensional lists allow visual representation
        ["~","~","~","~","~","~","~","~"],                                  # this is player ones ship location
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"]]

pshots1=[[0,0,0,0,0,0,0,0],                                                 # this is player ones taken shots
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

plist2=[["~","~","~","~","~","~","~","~"],                                  # player two ship location
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"],
        ["~","~","~","~","~","~","~","~"]]


pshots2=[[0,0,0,0,0,0,0,0],                                                 # player twos taken shots
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

p1x=0                                                                       # player one x coord. p1x. Not lower case L! they look similar
p1y=0                                                                       # player one y coord

p2x=0                                                                       # player twos coords
p2y=0

p1s1x=9
p1s1y=9
p1s1a=9
p1s2x=9
p1s2y=9
p1s2a=9
p2s1x=9
p2s1y=9
p2s1a=9
p2s2x=9
p2s2y=9
p2s2a=9

p1ships=0
p2ships=0

playerinputerror=0                                                          # for flagging errors

turn=0
player=0                                                                    # players whose turn it is
direction="0"                                                               # players axis choice for prompts
allignstorage=0

gstatus="0"

def randomchar():
    r = random.randrange(1, 27)
    if r == 1:
        return "A"
    elif r == 2:
        return "B"
    elif r == 3:
        return "C"
    elif r == 4:
        return "D"
    elif r == 5:
        return "E"
    elif r == 6:
        return "F"
    elif r == 7:
        return "G"
    elif r == 8:
        return "H"
    elif r == 9:
        return "I"
    elif r == 10:
        return "J"
    elif r == 11:
        return "K"
    elif r == 12:
        return "L"
    elif r == 13:
        return "M"
    elif r == 14:
        return "N"
    elif r == 15:
        return "O"
    elif r == 16:
        return "P"
    elif r == 17:
        return "Q"
    elif r == 18:
        return "R"
    elif r == 19:
        return "S"
    elif r == 20:
        return "T"
    elif r == 21:
        return "U"
    elif r == 22:
        return "V"
    elif r == 23:
        return "W"
    elif r == 24:
        return "X"
    elif r == 25:
        return "Y"
    elif r == 26:
        return "Z"

def countunitxtorand(p):
    z=0
    if p == 1:
        for i in range(0, 8):
            for j in range(0, 8):
                if plist1[i][j] == "X":
                    z = z + 1
                    plist1[i][j] = randomchar()
    if p == 2:
        for i in range(0, 8):
            for j in range(0, 8):
                if plist2[i][j] == "X":
                    z = z + 1
                    plist2[i][j] = randomchar()
    return z

def quickdisplay(p):
    print("\n")
    if p == 1:
        for i in range(0, 8):
            for j in range(0, 8):
                print(plist1[i][j], " ", end="")
            if j == 7:
                print("\n")
    if p == 2:
        for i in range(0, 8):
            for j in range(0, 8):
                print(plist2[i][j], " ", end="")
            if j == 7:
                print("\n")

def shotdisplay(p):
    if p == 1:
        for k in range(0, 8):
            for l in range(0, 8):
                print(pshots1[k][l], " ", end="")
            if l == 7:
                print("\n")
    if p == 2:
        for k in range(0,8):
            for l in range(0,8):
                print(pshots2[k][l], " ", end="")
            if l == 7:
                print("\n")
            


def gamescreen(p):                                                          # function to print map. prototype
    if p == 1:
        print("\n" * 64)
        print("Turn: ", turn)
        print("\t\t- - - - - - - - - -")
        print("\t\t|",plist1[0][0],plist1[0][1],plist1[0][2],plist1[0][3],plist1[0][4],plist1[0][5],plist1[0][6],plist1[0][7],"|")
        print("\t\t|",plist1[1][0],plist1[1][1],plist1[1][2],plist1[1][3],plist1[1][4],plist1[1][5],plist1[1][6],plist1[1][7],"|")
        print("\t\t|",plist1[2][0],plist1[2][1],plist1[2][2],plist1[2][3],plist1[2][4],plist1[2][5],plist1[2][6],plist1[2][7],"|")
        print("\t\t|",plist1[3][0],plist1[3][1],plist1[3][2],plist1[3][3],plist1[3][4],plist1[3][5],plist1[3][6],plist1[3][7],"|")
        print("\t\t|",plist1[4][0],plist1[4][1],plist1[4][2],plist1[4][3],plist1[4][4],plist1[4][5],plist1[4][6],plist1[4][7],"|")
        print("\t\t|",plist1[5][0],plist1[5][1],plist1[5][2],plist1[5][3],plist1[5][4],plist1[5][5],plist1[5][6],plist1[5][7],"|")
        print("\t\t|",plist1[6][0],plist1[6][1],plist1[6][2],plist1[6][3],plist1[6][4],plist1[6][5],plist1[6][6],plist1[6][7],"|")
        print("\t\t|",plist1[7][0],plist1[7][1],plist1[7][2],plist1[7][3],plist1[7][4],plist1[7][5],plist1[7][6],plist1[7][7],"|")
        print("\t\t- - - - - - - - - -")

    elif p == 2:
        print("\n" * 64)
        print("Turn: ", turn)
        print("\t\t- - - - - - - - - -")
        print("\t\t|",plist2[0][0],plist2[0][1],plist2[0][2],plist2[0][3],plist2[0][4],plist2[0][5],plist2[0][6],plist2[0][7],"|")
        print("\t\t|",plist2[1][0],plist2[1][1],plist2[1][2],plist2[1][3],plist2[1][4],plist2[1][5],plist2[1][6],plist2[1][7],"|")
        print("\t\t|",plist2[2][0],plist2[2][1],plist2[2][2],plist2[2][3],plist2[2][4],plist2[2][5],plist2[2][6],plist2[2][7],"|")
        print("\t\t|",plist2[3][0],plist2[3][1],plist2[3][2],plist2[3][3],plist2[3][4],plist2[3][5],plist2[3][6],plist2[3][7],"|")
        print("\t\t|",plist2[4][0],plist2[4][1],plist2[4][2],plist2[4][3],plist2[4][4],plist2[4][5],plist2[4][6],plist2[4][7],"|")
        print("\t\t|",plist2[5][0],plist2[5][1],plist2[5][2],plist2[5][3],plist2[5][4],plist2[5][5],plist2[5][6],plist2[5][7],"|")
        print("\t\t|",plist2[6][0],plist2[6][1],plist2[6][2],plist2[6][3],plist2[6][4],plist2[6][5],plist2[6][6],plist2[6][7],"|")
        print("\t\t|",plist2[7][0],plist2[7][1],plist2[7][2],plist2[7][3],plist2[7][4],plist2[7][5],plist2[7][6],plist2[7][7],"|")
        print("\t\t- - - - - - - - - -")

    else:
        print("\n" * 64)
        print("\t\tx - x x x - x x x x")
        print("\t\tx x x - x x x x - x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx s h a t t l e x x")
        print("\t\tx - x b i p s x x x")
        print("\t\tx x x x x x - x x x")
        print("\t\tx x - x x x x x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x - x x x - x x")
        print("\t\tx x x x x x x x x x")
        time.sleep(0.1)
        print("\n" * 64)
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx s h a t t l e x x")
        print("\t\tx x x b i p s x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x x x x x x x x")
        print("\t\tx x x x x x x x x x")
        time.sleep(0.1)
        print("\n" * 64)
        print("\t\t- n - - - - - - - -")                    # - - - - - - - - - -
        print("\t\t- V - - - C O D - -")                    # | - - - - - - - - |
        print("\t\t- - - - - - - - - -")                    # | - - - C O D - - |
        print("\t\t- s h a t t l e - -")                    # | - n - - - - - - |
        print("\t\t- - - b i p s - - -")                    # | - V - - - - - - |
        print("\t\t- - - - - - - - - -")                    # | - - - M - - - - |
        print("\t\t- - M - - - < O > -")                    # | - - - O - < O > |
        print("\t\t- - O - - - - - - -")                    # | - - - V - - - - |
        print("\t\t- - V - - - - - - -")                    # | - - - - - - - - |
        print("\t\t- - - - - - - - - -")                    # - - - - - - - - - -
        time.sleep(0.5)

def ncguts(x, p, d, L, H):                                                  # x is the coord being checked, p is the player, d is the direction
    try:                                                                    # nc guts exists because of need to check for number over and over
        val = int(x)                                                        # try checks to see wether this converts to a number
    except ValueError:                                                      # if not we get error
        playerinputerror = 1                                                # which is flagged to power loop
        print("\n\t That's not a number \n\n")
        while playerinputerror == 1:                                        # loop keeps prompting for valid input
            x = inputcoords(x, p, d, L, H)
            try:                                                            # loop keeps going until valid
                val = int(x)                                        
            except ValueError:
                playerinputerror = 1
                print("\n\t That's not a number\n\n")                       # still not a number? its as if someone is trying to break it!
            else:
                playerinputerror = 0                                        # finally get a number and break from loop
                x = val                                                     # dont forget to actually convert the string now we know its valid
    else:
        x = val                                                             # and dont forget it might not error at all
    return x

def inputnumchecker(x, p, d, L, H):                                         # x is the coord being checked, p is the player, d is the direction
    x = ncguts(x, p, d, L, H)                                               # ncguts ensures we have a number
    while int(x) < L or int(x) > H:                                         # but theres no guarantee itll be in range
        print("\n\n\t Not in range ", L, end="")
        print("-", H, end="")
        x=input("\n\n")                                                     # loop prompt for new input if not
        x = ncguts(x, p, d, L, H)                                           # check new input is a number
    return x                                                                # return valid value

def inputcoords(x, p, d, L, H):                                             # decided this was common enough to warrant a function
    print("\n\n\t Player", p, " enter", d, " data:", L, "-", H)
    x=input("\n\n\n\n\n")
    return x
                                                                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def turntaker(p, t):                                                        # X AND Y ARE REVERSED HERE
    x = 0
    y = 0
    L = 1
    H = 6
    d = "x"                                                                 # WE TELL USER WE ARE ASKING FOR X, BUT ASSIGN TO Y
    y = inputcoords(y, p, d, L, H)                                          # AND VICE VERSA
    y = inputnumchecker(y, p, d, L, H )                                     # IF YOU DECIDE TO FIX THIS PROPERLY
    y = int(y)                                                              # THIS SECTION WILL NEED TO BE REVERSED     
    d = "y"                                                                 # OR SOMETHING
    x = inputcoords(x, p, d, L, H)                                          # I HAVENT HAD BREAKFAST YET
    x = inputnumchecker(x, p, d, L, H)                                      #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    x = int(x)
    allignstorage=int(input("\n\t\tFacing 1.horizontal 2.vertical: "))      #   bigger boats
    L = 1
    H = 2
    allignstorage=inputnumchecker(allignstorage, p, d, L, H)
    if p == 1:
        plist1[x][y] = "X"                                                  # This where the magic happens
        if allignstorage == 1:                                              # the ships get printed to the lists
            plist1[x][y+1] = "X"                                            #
            plist1[x][y-1] = "X"                                            #
        elif allignstorage == 2:                                            #
            plist1[x+1][y] = "X"                                            #
            plist1[x-1][y] = "X"
        else:
            print("Error printing boats")
        
    elif p == 2:
        plist2[x][y] = "X"
        if allignstorage == 1:
            plist2[x][y+1] = "X"
            plist2[x][y-1] = "X"
        elif allignstorage == 2:
            plist2[x+1][y] = "X"
            plist2[x-1][y] = "X"
        else:
            print("Error printing boats")
        
    else:
        print("Error - p is not 1 or 2 in turntaker function")
    return y, x, allignstorage

print("\t\t--------Welcome--------")
print("\t\t----------to-----------")
print("\t\t------Shipplebats------")                                        # nice name
print("\t\tYou have one ship in a ")
print("\t\t---stretch of water----")
print("\t\t-----------------------")
print("\t\t-You and your oponent--")
print("\t\tinhabit seperate areas-")
print("\t\t-so coordinates are ---")
print("\t\t-relative. In other----")
print("\t\t-words its entirely----")
print("\t\tpossible to have chosen")
print("\t\t-the same coordinates--")
print("\t\t-----------------------")

time.sleep(0.5)                                                             # computers need rest too
#print("\n" * 64)                                                            # print 64 new lines. clear screen
gamescreen(player)
time.sleep(0.5)


gstatus=input("\n\n\t\t(S)tart e(X)it: \n\n\t\t")

while gstatus != "X":
    print("\n\n\tPlayer 1 take the controls. Player 2 look away\n\n")
    player = 1
    turn = 1
    p1s1x, p1s1y, p1s1a = turntaker(player, turn)
    gamescreen(player)
    input("\n\n\t X is your ship. Press enter\n\n")
    print("\n" * 64)
    turn = 2
    p1s2x, p1s2y, p1s2a = turntaker(player, turn)
    gamescreen(player)
    input("\n\n\t X is your ship. Press enter\n\n")
    print("\n" * 64)

    print("\n\n\tPlayer 2 take the controls. Player 1 look away\n\n")
    player = 2
    turn = 3
    p2s1x, p2s1y, p2s1a = turntaker(player, turn)
    gamescreen(player)
    input("\n\n\t X is your ship. Press enter\n\n")
    print("\n" * 64)
    turn = 4
    p2s2x, p2s2y, p2s2a = turntaker(player, turn)
    gamescreen(player)
    input("\n\n\t X is your ship. Press enter\n\n")
    print("\n" * 64)

    p1ships = countunitxtorand(1)
    if p1ships < 6:
        print("Player one has placed two ships in the same area, \n \t\tBoth boats sink")
        print("\n\n\tPlayer two wins by default")
        gstatus = "X"


    p2ships = countunitxtorand(2)
    if p2ships < 6:
        print("Player two has placed two ships in the same area, \n \t\tBoth boats sink")
        print("\n\n\tPlayer one wins by default")
        gstatus = "X"

    while gstatus != "X":
        print("Player 1 take the controls. Both can look. Let battle commence!\n\n")
        input("Press enter\n\n")

        print("p1s1x: ", p1s1x, "p1s1y: ", p1s1y, "p1s1a: ", p1s1a)
        print("p1s2x: ", p1s2x, "p1s2y: ", p1s2y, "p1s2a: ", p1s2a)
        print("p2s1x: ", p2s1x, "p2s1y: ", p2s1y, "p2s1a: ", p2s1a)
        print("p2s2x: ", p2s2x, "p2s2y: ", p2s2y, "p2s2a: ", p2s2a)

        quickdisplay(1)
        print("player one has ", p1ships)
        shotdisplay(1)

        quickdisplay(2)
        print("player two has ", p2ships)
        shotdisplay(2)
    
        input()





