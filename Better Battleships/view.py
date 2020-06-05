#CHRIS NELSON NHC 2017 
def grid_print(grid, wid, hei): # give it an array & dimensions
    print("")                   # itll print list as a rectangle
    print("\t 01234567")        # horizontal grid coords help
    for i in range(hei):        # with corrdinates automatically
        for j in range(wid):    # set so we can refer to screen
            if j == 0:          # locations via grid[y][x]
                print("\t", end="") # <formatting tabs in front of each line
                print(i, end="")    # vertical grid coords help
            print(grid[i][j], end="") # <print list contents
            if j == (wid-1):        # arrays index from 0, width-1 prompts \n
                print("\n", end="") # supress print() auto carriage return with end=""
                                    # Just using print("") would be more obscure
def title_print(title):             
    print(title, end="") # prints exactly what we send

def clear_screen(): # clears immediate
    print("\n"*20)  # screen contents

def roll_up():      # moves screen
    print("\n"*10)  # contents up a bit
