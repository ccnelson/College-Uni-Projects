##CHRIS NELSON NHC 2017

import view as v # imports 3 other files from this directory
import model as m # refers to functions / classes from these with v. m.
import functions as f # or f. prefix. hit_check() stayed local for efficiency
                                                    
dat = m.Datastore() # instantiate class 
p1 = m.Player()     # see def __init__() for variables in class definitions
p2 = m.Player()     # found in model.py (m.) - now p1 and p2 can 
                    # represent players one and two

                             # hit_check handles score, hit log update, and ship map update
def hit_check(player, x, y): # collision detection, send it a player and some coordinates -
    if player == 1:          # the player is shooting, the coords are a target in y,x format
        if p2.ship_grid[int(y)][int(x)] == "#": # is it a ship? 
            print("\t\tHIT!")   # congratulate
            p1.score += 1       # increment score
            p1.hit_grid[int(y)][int(x)] = "X"   # log hit on hit_grid
            p2.ship_grid[int(y)][int(x)] = "~"  # remove section of hit ship
        else:
            print("\t\tMISS")
            p1.hit_grid[int(y)][int(x)] = "0" # log miss on hit_grid
    elif player == 2:
        if p1.ship_grid[int(y)][int(x)] == "#": # same again for player 2... could put
                                                 # this whole function in a loop or
            print("\t\tHIT!!")                  # external function, but its clear,
            p2.score += 1                       # short, and important, so maybe not
            p2.hit_grid[int(y)][int(x)] = "X"
            p1.ship_grid[int(y)][int(x)] = "~"
        else:
            print("\t\tMISS")
            p2.hit_grid[int(y)][int(x)] = "0"

# program starts here
v.clear_screen()            # clear screen
v.title_print(dat.title)    # show title
v.roll_up()                 # move screen contents up a little
input("\tPress enter")        # prompt input
v.clear_screen()            
v.title_print(dat.instructions) # show instructions
input("\tPress enter")
v.roll_up()
v.grid_print(p1.ship_grid, p1.wid, p1.hei) # show player the grid
f.ship_place(1, 1, p1.ship_grid)    # request player 1 place ship 1
v.grid_print(p1.ship_grid, p1.wid, p1.hei) # provide feedback of placement
input("\tPress enter to continue...") # error checking in f.ship_place() in functions.py
f.ship_place(1, 2, p1.ship_grid)    # request player 1 place ship 2
v.grid_print(p1.ship_grid, p1.wid, p1.hei)
input("\tPress enter to continue...")
f.ship_place(1, 3, p1.ship_grid)
v.grid_print(p1.ship_grid, p1.wid, p1.hei)
print("\tPLAYER TWO'S TURN... PRESS ENTER TO CLEAR") # switch player warning
input()
v.clear_screen() # lots of newlines so player 2 doesnt see players 1's ships
v.clear_screen()
v.clear_screen()
input("\tPress enter to continue...")
v.grid_print(p2.ship_grid, p2.wid, p2.hei)
f.ship_place(2, 1, p2.ship_grid) # request player 2 place ship 1
v.grid_print(p2.ship_grid, p2.wid, p2.hei)
input("\tPress enter to continue...")
f.ship_place(2, 2, p2.ship_grid)
v.grid_print(p2.ship_grid, p2.wid, p2.hei)
input("\tPress enter to continue...")
f.ship_place(2, 3, p2.ship_grid)
v.grid_print(p2.ship_grid, p2.wid, p2.hei)
print("\tBATTLE BEGINNING... PRESS ENTER TO CLEAR") # battle part starts here
input()
v.clear_screen()
v.clear_screen()
v.clear_screen()
v.clear_screen()
input("\tPress enter to continue...")
player_1 = True                             # player_1 is boolean for the toggling
while (p1.score != 9 and p2.score != 9):    # each player has 9 ship parts, +1 score each
    if player_1 == True:
        player = 1 # make indicator an integer
    else:
        player = 2
    if player_1 == True:
        v.grid_print(p1.hit_grid, p1.wid, p1.hei) # show player their hit_grid
    else:
        v.grid_print(p2.hit_grid, p2.wid, p2.hei)
    x = input("\n\tPlayer " + str(player) + " please input X target coordinates\n")
    x = f.force_valid(x, 0, 7)
    y = input("\n\tPlayer " + str(player) + " please input Y target coordinates\n")
    y = f.force_valid(y, 0, 7)
    v.roll_up()
    hit_check(player, x, y) # collision detection, hit_grid updates, and player feedback
    if player_1 == True:
        v.grid_print(p1.hit_grid, p1.wid, p1.hei) # show player their hits / misses
    else:
        v.grid_print(p2.hit_grid, p2.wid, p2.hei)
    print("\nPlayer 1 score: " + str(p1.score)) # Display both scores, so players
    print("Player 2 score: " + str(p2.score)) # know when hit
    player_1 = not player_1 # toggle player_1 value between True and False
    input("\tPress enter to continue...")
    v.clear_screen()

if p1.score == 9:                   # turn based system means only one player can win
    print("\tPlayer one wins\n\n")    # as soon as a player score reaches 9, game over,
elif p2.score == 9:                 # as player has 9 ship blocks and get +1 score
    print("\tPlayer two wins\n\n")    # for each destroyed

print("\tGame over")                # shhh... i know - i know, just be glad it happened
input()

