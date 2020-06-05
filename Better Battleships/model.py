#CHRIS NELSON NHC 2017
class Player:
    def __init__(self):
        self.wid = 8 # width of grid
        self.hei = 8 # height of grid
        self.ship_grid = [["~" for i in range(self.wid)]for i in range(self.hei)]
        self.hit_grid = [["~" for i in range(self.wid)]for i in range(self.hei)]
        self.score = 0              # list comprehension sets up our 
                                    # grids, one for ships, one to track targets
class Datastore:
    def __init__(self):             # multiline comments for formatting
        self.title = """
 _______  _______  _______  _______  ___      _______ 
|  _    ||   _   ||       ||       ||   |    |       |
| |_|   ||  |_|  ||_     _||_     _||   |    |    ___|
|       ||       |  |   |    |   |  |   |    |   |___ 
|  _   | |       |  |   |    |   |  |   |___ |    ___|
| |_|   ||   _   |  |   |    |   |  |       ||   |___ 
|_______||__| |__|  |___|    |___|  |_______||_______|

             (        )  (    (    (     
             )\ )  ( /(  )\ ) )\ ) )\ )  
            (()/(  )\())(()/((()/((()/(  
             /(_))((_)\  /(_))/(_))/(_)) 
            (_))   _((_)(_)) (_)) (_))   
            / __| | || ||_ _|| _ \/ __|  
            \__ \ | __ | | | |  _/\__ \  
            |___/ |_||_||___||_|  |___/  
        
        """
        self.instructions = """
    
   Player one will place their ships, followed by player two.
     Players have three ships, they are shaped 3x1 : ###
         Place these ships vertically or horizontally
 Ship coordinates are measured from the upper-left-most corner
                  Coordinates start at zero
 Ships must be placed within grid, and not on top of each other
          Once ships are placed, battle will commence
        To sink a ship, a player must hit its three sections
            On target grid, X means HIT, 0 means miss
 To achieve victory, a player must sink all their opponents ships
     Hit markers can become miss markers if you fire on them!

         01234567                  |    01234567
        0~~~~~~~~                  |   0~~~~~~~~
        1~~~~~~~~                  |   1~~~~~~~~
        2~~~~~~~~   THE "!" IS AT  |   2~~~~~~~~   IF VERTICAL
        3~!~~~~~~   X = 1          |   3~#~~~~~~   WOULD PRODUCE
        4~~~~~~~~   Y = 3          |   4~#~~~~~~   THE SHIP SHOWN
        5~~~~~~~~                  |   5~#~~~~~~
        6~~~~~~~~                  |   6~~~~~~~~
        7~~~~~~~~                  |   7~~~~~~~~

        """

