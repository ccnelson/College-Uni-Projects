#CHRIS NELSON NHC 2017
def check_isnum(num, low, high): # checks is num and in range
    try:                            # using in_range() it returns false with error info
        val = int(num)              # if not a number, and in range
    except ValueError:
        print("Not a number")# player feedback
        return False
    if in_range(int(num), low, high) == False: # uses function below
        return False
    return True
    
def in_range(num, low, high): # range function for check_isnum()
    if num < low:
        print("Too low") # player feedback
        return False
    elif num > high:
        print("Too high")
        return False
    return True

def force_valid(i, L, H): # takes input (if invalid gets input), returns a number between L & H
    while check_isnum(i, L, H) == False: # this checks it is within allowed boundaries
        i = input()                         # and valid. ship is 3x, grid is 0-7
        print( "" + str(L) + " to " + str(H)) # giving us 0-5 valid horizontal placement
    return i
                                    # loop to get allignment, and coords, lots
def ship_place(player, ship, grid): # of error catching makes this long.
    done = False                    # input is valid, in range, and non-conflicting
    while done == False:            # also actually places ships using grid object
        # allignment
        print("\n\tPlayer " + str(player) + " please enter ship " + str(ship) + " allignment")
        print("\t0 = horizontal - 1 = vertical") # request & input provide constraints
        allignment = input()                    # get input
        allignment = force_valid(allignment, 0, 1) # force it to be valid
        allignment = int(allignment)  # we know its ok to cast to int at this point
        if allignment == 0:             # feedback confirmation for player
            print("Horizontal")
        elif allignment == 1:
            print("Vertical")
        # x coordinate
        print("\n\tPlayer " + str(player) + " please enter ship " + str(ship) + " X coordinate")
        x_co = input()              # requesting x coord
        if allignment == 0:
            x_co = force_valid(x_co, 0, 5) # force a 0-5 input
        elif allignment == 1:               # placing from top-left-most ship corner
            x_co = force_valid(x_co, 0, 7) # force a 0-7 input
        x_co = int(x_co)            # cast to integer
        print("X coord: ", x_co)
        # y coordinate
        print("\n\tPlayer " + str(player) + " please enter ship " + str(ship) + " Y coordinate")
        y_co = input()
        if allignment == 0:
            y_co = force_valid(y_co, 0, 7)
        elif allignment == 1:
            y_co = force_valid(y_co, 0, 5)
        y_co = int(y_co)
        print("Y coord: ", y_co)
        
	## add it to the board
        if allignment == 0:
            if ship == 2 or 3:                  # we dont need to check ship 1 for overlaps
                if grid[y_co][x_co] == "#":     # but 2 and 3 we do
                    print("\n\tOverlap TRY AGAIN") # warn player
                    continue                        # reset loop to allow player to change
                elif grid[y_co][x_co + 1] == "#":   # allignment
                    print("\n\tOverlap TRY AGAIN")  # the overlap warnings are the only
                    continue                        # reason this is a loop, allowing
                elif grid[y_co][x_co + 2] == "#":   # a reset to the ship placement
                    print("\n\tOverlap TRY AGAIN")
                    continue
            grid[y_co][x_co] = "#"        # store ship in grid object at chosen location
            grid[y_co][x_co + 1] = "#"    # ship is 3x, allignment horizontal so
            grid[y_co][x_co + 2] = "#"    # addition handles other ship parts
            done = True             # ship has been placed and loop can end
        elif allignment == 1:
            if ship == 2 or 3:      # same again for vertical allignment
                if grid[y_co][x_co] == "#":
                    print("\n\tOverlap TRY AGAIN")
                    continue
                elif grid[y_co + 1][x_co] == "#": # y coord increment for overlap check
                    print("\n\tOverlap TRY AGAIN")
                    continue
                elif grid[y_co + 2][x_co] == "#":
                    print("\n\tOverlap TRY AGAIN")
                    continue
            grid[y_co][x_co] = "#"        # vertical placement sees y coord incremented
            grid[y_co + 1][x_co] = "#"      # for ship part placement
            grid[y_co + 2][x_co] = "#"
            done = True

