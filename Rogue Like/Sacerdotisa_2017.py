import tkinter
import random

PROGRAM_NAME = " Sacerdotisa "
CN_play_area_y = 20 #y (formerly n)
CN_play_area_x = CN_play_area_y*2 #x (formerly o)
CN_root = tkinter.Tk() # root window
CN_root.title(PROGRAM_NAME) # name
CN_root.geometry('800x440') # size x y
#CN_root.wm_iconbitmap("favicon.ico") # icon
CN_root.resizable(False,False) # no resize
CN_text = tkinter.Text(CN_root,background='black',\
                    foreground='black',font=('Courier',12)) # txt setup - monospaced

#generate build data
CN_roomminsize = int(CN_play_area_y/7)     # constraints to keep rooms
CN_roommaxsize = CN_play_area_y/2     # from spilling over boundaries
CN_worldminsize = int(CN_play_area_y/5) # and fit nicely
CN_worldmaxX = (CN_play_area_x-(CN_play_area_y/2))-2 # product of trial and error
CN_worldmaxY = (CN_play_area_y/2)-2

#classes
class CN_Board:
    def __init__(self,name,sizey,sizex,message,lvl):
        self.name = name
        self.sizey = sizey
        self.sizex = sizex
        self.contents = [["#" for i in range(CN_play_area_x)]for i in range(CN_play_area_y)]
        self.message = message
        self.lvl = lvl
        self.monster_home = 0
    def CN_no_obstruction(self, yco, xco): # checks obstruction before moving
        if CN_play_board.contents[yco][xco] != CN_wall.icon:
            if CN_play_board.contents[yco][xco] != CN_ghost.icon:
                if CN_play_board.contents[yco][xco] != CN_monster.icon:
                    return True
    def CN_make_mov(self, co_select, value): # automates move process
        self.contents[CN_player.yco][CN_player.xco] = "."
        if co_select == "xco":
            CN_player.xco  = CN_player.xco + value
            self.contents[CN_player.yco][CN_player.xco] = CN_player.icon
        elif co_select == "yco":
            CN_player.yco = CN_player.yco + value
            self.contents[CN_player.yco][CN_player.xco] = CN_player.icon
        #door fix - incase door is stepped on and disappears
        if CN_play_board.contents[CN_door.yco][CN_door.xco] == " ":
            CN_play_board.contents[CN_door.yco][CN_door.xco] = CN_door.icon
        elif CN_play_board.contents[CN_door.yco][CN_door.xco] == ".":
            CN_play_board.contents[CN_door.yco][CN_door.xco] = CN_door.icon

class CN_Inhabitant:
    def __init__(self,name,icon,yco,xco,health,score):
        self.name = name
        self.icon = icon
        self.yco = yco
        self.xco = xco
        self.health = health
        self.score = score
        self.key = False # useful for interactions

class CN_Room:
    def __init__(self,name,icon):
        self.name = name
        self.icon = icon
        self.yco = random.randrange(CN_worldminsize,CN_worldmaxY)
        self.xco = random.randrange(CN_worldminsize,CN_worldmaxX)
        self.ysize = random.randrange(CN_roomminsize,CN_roommaxsize)
        self.xsize = random.randrange(CN_roomminsize,CN_roommaxsize)
        self.midx = self.xco + int(self.xsize/2)
        self.midy = self.yco + int(self.ysize/2)
    def CN_room_build(self): # my ever first method
        for i in range(self.xco,(self.xco + self.xsize)):
            for j in range(self.yco,(self.yco + self.ysize)):
                CN_play_board.contents[j][i] = " "

class CN_Question:
    def __init__(self,question,answer1,answer2,answer3,anscorr):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.anscorr = anscorr
        self.asking = 0 # which question is being asked
        self.list = [] # list of asked questions
    def CN_question_right(self, answer):
        if answer == CN_ghost_qs.anscorr:
            CN_player.score = 1
            CN_ghost.score = 1
            CN_player.health += 2
            CN_play_board.contents[CN_ghost.yco][CN_ghost.xco] = " "
        else:
            CN_play_board.contents[CN_ghost.yco][CN_ghost.xco] = " "
            CN_player.score = 0
            CN_ghost.score = 1

class CN_Index:            # used to save coords to be tagged for colours
    def __init__(self):
        self.player = 0
        self.ghost = 0
        self.monster = 0
        self.door = 0
        self.pm = 0 # message
        self.pm_e = 0 # message end
        self.ph = 0 # health
        self.ph_e = 0
        self.pk = 0 # key
        self.pk_e = 0
        self.big_box = [] # theres a load of these
        self.mid_box = [] # so they go in a list
        self.sma_box = [] # or three
        self.nw = 0 # corners of 'lighted' area
        self.ne = 0
        self.sw = 0
        self.se = 0
        self.welcome = 0
        self.welcome_e = 0

#state for door/ghost/monster
class CN_GameState:
    def __init__(self):
        self.in_sight = False

class CN_TextArt:
    def __init__(self):
        self.art = ""

CN_welcome_text = CN_TextArt()
CN_welcome_text.art = """
         ____  ____  ____  _____ ____  ____  ____  _____  _  ____  ____  
        / ___\/  _ \/   _\/  __//  __\/  _ \/  _ \/__ __\/ \/ ___\/  _ \  
        |    \| / \||  /  |  \  |  \/|| | \|| / \|  / \  | ||    \| / \|  
        \___ || |-|||  \_ |  /_ |    /| |_/|| \_/|  | |  | |\___ || |-||  
        \____/\_/ \|\____/\____\\\_/\_\\\____/\____/  \_/  \_/\____/\_/ \\|

           You awake in a very dark room, the floor is cold like stone.
                          It is so dark you cannot see.
           After what seems like an eternity of groping your way around
                            you come upon a trapdoor.
            As you explore its workings with your hands you hear a click
              The trapdoor springs open and you go falling through...
                                 W/A/S/D to move
                           Contextual control on screen
                             You need keys for doors
                            Watch out for the monster
                    Moving to a new room costs one health point
                             Try to find your way out
                                  Before you die
                                    good luck
                                    <spacebar>    """

CN_progress_text = CN_TextArt()
CN_progress_text.art = """

      █     █░▓█████  ██▓     ██▓       ▓█████▄  ▒█████   ███▄    █ ▓█████
     ▓█░ █ ░█░▓█   ▀ ▓██▒    ▓██▒       ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓█   ▀
     ▒█░ █ ░█ ▒███   ▒██░    ▒██░       ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒███ 
     ░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒██░       ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ 
     ░░██▒██▓ ░▒████▒░██████▒░██████▒   ░▒████▓ ░ ████▓▒░▒██░   ▓██░░▒████▒
      ░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
      ▒ ░ ░   ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░    ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
      ░   ░     ░     ░ ░     ░ ░       ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░    ░  
      ░       ░  ░    ░  ░    ░  ░      ░        ░ ░           ░    ░  ░
                                                                          """

CN_ghost_text_chat = CN_TextArt()
CN_ghost_text_chat.art = """
                 .--,  
                /  (  
               /    \  
              /      \   
             /  0  0  \  
     ((()   |    ()    |   ())) - - - Greetings wanderer,  
     \  ()  (  .____.  )  ()  /       I have a question for you...  
      |` \_/ \  `'""'`/ \_/ `|  
      |       `.'--'.`       |  
       \        `'""'`      /  
        \                  /  
         `.              .' 
          |`             |  _.'|  
          |              `-'  /  
          \                 .'  
           `.____________.-'         """

CN_ghost_text_right_1 = CN_TextArt()
CN_ghost_text_right_1.art = """
                ___
              _/ ..\  
             ( \  0/__  
              \    \__)  
              /     \   
             /      _\   
             `""``       """

CN_ghost_text_wrong = CN_TextArt()
CN_ghost_text_wrong.art = """
                     .-.  
        heehee      /aa \_  
                  __\-  / )                 .-.  
        .-.      (__/    /        haha    _/oo \   
      _/ ..\       /     \               (  v  /__  
     ( \  u/__    /       \__             \/   ___)  
      \    \__)   \_.-._._   )  .-.       /     \   
      /     \             `-`  / ee\_    /       \_  
   __/       \               __\  o/ )   \_.-.__   )  
  (   _._.-._/     hoho     (___   \/           '-'  
   '-'                        /     \   
                            _/       \    teehee  
                           (   __.-._/               """

CN_monster_text = CN_TextArt()
CN_monster_text.art = """  
         	   { }   { }  
         	   //     \\\  
           	 \\\  `' //  
         	 ___======___  
         	/ __\====/__ \   
         	 / / ==== \ \   
         	  |   ==   |  
         	      ||     
         	      ||    3 
         	      \\\===//    """

CN_you_died_text = CN_TextArt()
CN_you_died_text.art = """
              _ _               _  _         _   
             | | | ___  _ _   _| |<_> ___  _| |  
             \   // . \| | | / . || |/ ._>/ . |  
              |_| \___/`___| \___||_|\___.\___|   """

CN_you_win_text = CN_TextArt()
CN_you_win_text.art = """
                      _______                      _______  _        _   
            |\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /|( )  
            ( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( || |  
             \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | || |  
              \   /  | |   | || |   | |  | |( )| || |   | || (\ \) || |  
               ) (   | |   | || |   | |  | || || || |   | || | \   |(_)  
               | |   | (___) || (___) |  | () () || (___) || )  \  | _   
               \_/   (_______)(_______)  (_______)(_______)|/    )_)(_)  """

#functions
def CN_cursor_pos(): # current position of cursor in text box 
    return CN_text.index(tkinter.INSERT)
 
#hall func
def CN_carve_halls(gofrom,goto,target,opt ):
    if opt == 2:
        for i in range(gofrom,goto):
            CN_play_board.contents[i][target] = " "
    elif opt == 1:
        for i in range(gofrom,goto):
            CN_play_board.contents[target][i] = " "

def CN_make_level(): # create level
    #build rooms
    CN_room1 = CN_Room("One","1")
    CN_room2 = CN_Room("Two","2")
    CN_room3 = CN_Room("Three","3")
    CN_room4 = CN_Room("Four","4")
    CN_room1.CN_room_build()
    CN_room2.CN_room_build()
    CN_room3.CN_room_build()
    CN_room4.CN_room_build()
    #first carve halls
    CN_carve_halls(CN_room1.midy+1,CN_room2.midy+1,CN_room1.midx,2)
    CN_carve_halls(CN_room1.midx+1,CN_room2.midx-1,CN_room2.midy,1)
    CN_carve_halls(CN_room2.midy,CN_room1.midy,CN_room1.midx,2)
    CN_carve_halls(CN_room2.midx,CN_room1.midx,CN_room2.midy,1)
    CN_carve_halls(CN_room2.midy+1,CN_room3.midy+1,CN_room2.midx,2)
    CN_carve_halls(CN_room2.midx-1,CN_room3.midx-1,CN_room3.midy,1)
    CN_carve_halls(CN_room3.midy,CN_room2.midy,CN_room2.midx,2)
    CN_carve_halls(CN_room3.midx,CN_room2.midx,CN_room3.midy,1)
    CN_carve_halls(CN_room4.midy,CN_room3.midy,CN_room3.midx,2)
    CN_carve_halls(CN_room4.midx,CN_room3.midx,CN_room4.midy,1)
    CN_carve_halls(CN_room3.midy,CN_room4.midy+1,CN_room3.midx,2)
    CN_carve_halls(CN_room3.midx+1,CN_room4.midx-1,CN_room4.midy,1)
    #set locations
    CN_player.xco = CN_room1.midx
    CN_player.yco = CN_room1.midy
    CN_door.xco = CN_room2.midx
    CN_door.yco = CN_room2.midy
    CN_ghost.xco = CN_room2.midx
    CN_ghost.yco = CN_room2.midy
    CN_key.xco = CN_room3.midx
    CN_key.yco = CN_room3.midy
    CN_play_board.contents[CN_player.yco][CN_player.xco] = CN_player.icon
    CN_play_board.contents[CN_door.yco][CN_door.xco] = CN_door.icon
    CN_play_board.lvl = CN_play_board.lvl + 1
    #decide wether to spawn monster
    if CN_play_board.lvl == CN_play_board.monster_home:
        CN_monster.yco = CN_room4.midy
        CN_monster.xco = CN_room4.midx
        CN_play_board.contents[CN_monster.yco][CN_monster.xco] = CN_monster.icon
    CN_play_board.message = "Room %s" % CN_play_board.lvl
    ##place and recess door into wall
    if CN_play_board.contents[CN_door.yco - 1][CN_door.xco] == CN_wall.icon:
        CN_door.yco = CN_door.yco - 1
    while CN_play_board.contents[CN_door.yco - 1][CN_door.xco] == " ":
        CN_door.yco = CN_door.yco - 1
        if CN_play_board.contents[CN_door.yco - 1][CN_door.xco] == CN_wall.icon:
            CN_door.yco = CN_door.yco - 1
    #decide wether to spawn ghost
    rand_ghostx = random.randrange(1,4)
    if rand_ghostx == 1:
        CN_play_board.contents[CN_ghost.yco][CN_ghost.xco] = CN_ghost.icon
    else:
        CN_play_board.contents[CN_ghost.yco][CN_ghost.xco] = " "
        CN_ghost.yco = 0
        CN_ghost.xco = 0
    CN_play_board.contents[CN_key.yco][CN_key.xco] = CN_key.icon
    CN_play_board.contents[CN_player.yco][CN_player.xco] = CN_player.icon

#welcome
def CN_welcome_screen(event):
    CN_text.delete(1.0,'end')
    CN_indexed.welcome = CN_cursor_pos()
    CN_text.insert('end', CN_welcome_text.art)
    CN_indexed.welcome_e = CN_cursor_pos()
    CN_text.tag_add("view_welcome", CN_indexed.welcome, CN_indexed.welcome_e)
    CN_text.tag_config("view_welcome", background="black", foreground="white")
    CN_text.see('end')

#main event - key press
def CN_on_key_press(event):
    if CN_ghost.key == True: # indicates we are interacting with ghost that wants 1-3 ans
        if event.char == "1":
            CN_ghost_qs.CN_question_right(CN_ghost_qs.answer1)
        elif event.char == "2":
            CN_ghost_qs.CN_question_right(CN_ghost_qs.answer2)
        elif event.char == "3":
            CN_ghost_qs.CN_question_right(CN_ghost_qs.answer3)
        CN_ghost.key = False
    #main player movements
    if event.char == "w":
        if CN_play_board.CN_no_obstruction(CN_player.yco - 1, CN_player.xco) == True:
            CN_play_board.CN_make_mov("yco", -1)
    elif event.char == "s":
        if CN_play_board.CN_no_obstruction(CN_player.yco + 1, CN_player.xco) == True:
            CN_play_board.CN_make_mov("yco", 1)
    elif event.char == "a":
        if CN_play_board.CN_no_obstruction(CN_player.yco, CN_player.xco -1) == True:
            CN_play_board.CN_make_mov("xco", -1)
    elif event.char == "d":
        if CN_play_board.CN_no_obstruction(CN_player.yco, CN_player.xco +1) == True:
            CN_play_board.CN_make_mov("xco", 1)
    #to quit
    elif event.char == "x":
        CN_root.destroy()
    # progress level when door.score 1
    if CN_player.yco == CN_door.yco:  
        if CN_player.xco == CN_door.xco:
            if CN_player.key == True:
                CN_door.score = 1
    # register player picking up key
    if CN_player.yco == CN_key.yco:
        if CN_player.xco == CN_key.xco:
            CN_player.key = True
    #elif event.char == "b":    # debug jump to next room
    #    CN_door.score = 1

def CN_ghost_chat(event):
    if CN_ghost.key == True:
        
        CN_text.delete(1.0,'end')
        CN_indexed.welcome = CN_cursor_pos()
        CN_text.insert('end', CN_ghost_text_chat.art)
        CN_text.insert('end', "\n\n\t")
        CN_text.insert('end', CN_ghost_qs.question)
        CN_text.insert('end', "\n\t\t")
        CN_text.insert('end', CN_ghost_qs.answer1)
        CN_text.insert('end', "\n\t\t")
        CN_text.insert('end', CN_ghost_qs.answer2)
        CN_text.insert('end', "\n\t\t")
        CN_text.insert('end', CN_ghost_qs.answer3)
        CN_indexed.welcome_e = CN_cursor_pos()
        CN_text.tag_add("view_welcome", CN_indexed.welcome, CN_indexed.welcome_e)
        CN_text.see('end')
        CN_ghost_qs.list.append(CN_ghost_qs.asking)

def CN_ghost_result(event):
    if CN_ghost.score == 1:
        CN_ghost.score = 0
        CN_text.delete(1.0,'end')
        CN_text.insert('end', "\n")
        CN_indexed.welcome = CN_cursor_pos()
        CN_text.insert('end', "\t", "\n")
        if CN_player.score == 1:
            ghost_outcomes = ('right!', 'exactly!', 'good!', 'precisely!')
            CN_text.insert('end',random.choice(ghost_outcomes))
            CN_text.insert('end',CN_ghost_text_right_1.art)
            CN_text.insert('end', "\n\n\n\t\t<spacebar>\n")
        elif CN_player.score == 0:
            CN_text.insert('end',"\n\n\t\tNot the answer I was looking for\n")
            CN_text.insert('end',CN_ghost_text_wrong.art)
            CN_text.insert('end',"\n\t\t<spacebar>\n")
        CN_text.insert('end', "\n")
        CN_indexed.welcome_e = CN_cursor_pos()
        CN_text.tag_add("view_welcome", CN_indexed.welcome, CN_indexed.welcome_e)
        CN_text.see('end')
        CN_ghost.score = 0
        CN_player.score = 0
        
def CN_monster_attack(event):
    if CN_monster.key == True:
        CN_text.delete(1.0,'end')
        CN_text.insert('end', "\n\n")
        CN_indexed.welcome = CN_cursor_pos()
        CN_text.insert('end', "\n\n\t\tA monster attacks!\n")
        CN_text.insert('end', CN_monster_text.art)
        CN_text.insert('end', "\n\n\t\tYou lose 5 health points")
        CN_text.insert('end', "\n\n\t\tbut the monster dies")
        CN_text.insert('end', "\n")
        CN_indexed.welcome_e = CN_cursor_pos()
        CN_text.tag_add("view_welcome", CN_indexed.welcome, CN_indexed.welcome_e)
        CN_text.see('end')
        CN_player.health -= 5
        CN_monster.key = False
        CN_play_board.contents[CN_monster.yco][CN_monster.xco] = " "

def CN_progress_level(event): # tries to run every move      
    if CN_door.score == 1:
        #set question for level
        CN_rand_quest = random.randrange(1,15)
        # check it hasnt already been asked
        while CN_rand_quest in CN_ghost_qs.list:
            CN_rand_quest = random.randrange(1,15)
        if CN_rand_quest == 1: # generate questions for level
            quest_1 = ["Who are you looking for?", "1. The Monster", "2. The way out", \
                          "3. A friend", "2. The way out"]       # store in list and unpack below
            CN_ghost_qs.asking = 1
        elif CN_rand_quest == 2:
            quest_1 = ["What is the colour of night?", "1. Darkness", "2. Pitch", \
                          "3. Sanguine, my Brother", "3. Sanguine, my Brother"]
            CN_ghost_qs.asking = 2
        elif CN_rand_quest == 3:
            quest_1 = ["For whom does the bell toll?", "1. He", "2. Me", "3. Thee", "3. Thee"]
            CN_ghost_qs.asking = 3
        elif CN_rand_quest == 4:
            quest_1 = ["What is your name?", "1. What is YOUR name?", "2. I do not know", \
                          "3. Mind your business", "2. I do not know"]
            CN_ghost_qs.asking = 4
        elif CN_rand_quest == 5:
            quest_1 = ["Where do the Aos Sí sleep?", "1. Under the Sidhe mound", "2. In their beds", \
                          "3. They aren't asleep", "1. Under the Sidhe mound"]
            CN_ghost_qs.asking = 5
        elif CN_rand_quest == 6:
            quest_1 = ["Which is the Hindu sun mantra?", "1. Om Mani Padme Hum", "2. Gāyatrī", \
                          "3. Shanti", "2. Gāyatrī"]
            CN_ghost_qs.asking = 6
        elif CN_rand_quest == 7:
            quest_1 = ["Which frost giant formed earth?", "1. Ymir", "2. Atla", "3. Vé", "1. Ymir"]
            CN_ghost_qs.asking = 7
        elif CN_rand_quest == 8:
            quest_1 = ["Which sun-god bore Bast?", "1. Nyambi", "2. Savitr", "3. Ra", "3. Ra"]
            CN_ghost_qs.asking = 8
        elif CN_rand_quest == 9:
            quest_1 = ["Who identifies with venus?", "1. Athena", "2. Ares", "3. Aphrodite", "3. Aphrodite"]
            CN_ghost_qs.asking = 9
        elif CN_rand_quest == 10:
            quest_1 = ["Which is the spider trickster?", "1. Anansi", "2. Buluku", "3. Shango", "1. Anansi"]
            CN_ghost_qs.asking = 10
        elif CN_rand_quest == 11:
            quest_1 = ["Hel is whose daughter?", "1. Loki", "2. Odin", "3. Baldr", "1. Loki"]
            CN_ghost_qs.asking = 11
        elif CN_rand_quest == 12:
            quest_1 = ["Which is the rain god?", "1. Tlaloc", "2. Tepeyollotl", "3. Tezcatlipoca", "1. Tlaloc"]
            CN_ghost_qs.asking = 12
        elif CN_rand_quest == 13:
            quest_1 = ["Which is Danu goddess of?", "1. Land", "2. Water", "3. Both", "3. Both"]
            CN_ghost_qs.asking = 13
        elif CN_rand_quest == 14:
            quest_1 = ["Did you leave the oven on?", "1. No", "2. Yes", "3. I don't know", "1. No"]
            CN_ghost_qs.asking = 14
        CN_ghost_qs.question, CN_ghost_qs.answer1, CN_ghost_qs.answer2, CN_ghost_qs.answer3, CN_ghost_qs.anscorr = quest_1 # unpack list
        CN_progress_screen(1)
        CN_player.key = False
        CN_player.health = CN_player.health - 1
        #score out old
        CN_play_board.contents = [[CN_wall.icon for i in range(CN_play_area_x)]for i in range(CN_play_area_y)]
        #generate new data
        CN_make_level()
        # turn function off
        CN_door.score = 0

#progress screem
def CN_progress_screen(event):
    CN_text.delete(1.0,'end')
    CN_indexed.welcome = CN_cursor_pos()
    CN_text.insert('end', "\n")
    CN_text.insert('end', CN_progress_text.art)
    CN_text.insert('end', "\n\n")
    CN_text.insert('end', "\t\tRoom ")
    CN_text.insert('end', CN_play_board.lvl)
    CN_text.insert('end', " complete")
    CN_text.insert('end', "\n") # big tuple of options to pick a choice from
    random_message = ('\n\tYou may not be there yet, but you are closer than you were', '\n\tProgress always comes at a price', \
                      '\n\tThe moon is nourished by supernal light', '\n\tSome ghosts need telling twice', \
                      '\n\tQuit now. While you\'re ahead', '\n\tYou should not be here', \
                      '\n\tYou\'ll need luck \n\tIf you wish to escape this place', '\n\tSome paths just cannot be followed', \
                      '\n\tThe ghost will block your view', '\n\tYou are looking well, Peorð', '\n\tSanguine is the colour of night', \
                      '\n\tYou\'ll find the Aos Sí under the Sidhe', '\n\tThere are legends of an invisible key')
    CN_text.insert('end', random.choice(random_message))
    CN_indexed.welcome_e = CN_cursor_pos()
    CN_text.tag_add("view_welcome",CN_indexed.welcome, CN_indexed.welcome_e)
    CN_text.see('end')

def CN_view_square(y_cor,x_cor): # function controlling lighted area around player
    cor_min = -3 # size of biggest box
    cor_max = 4 # reduced each time loop runs
    for i_square in range(3): # getting the coords of 3 increasingly small boxes
        for y_view in range(cor_min, cor_max): # relative to players location
            for x_view in range(cor_min, cor_max): # to colour tag 'view'
                if y_cor == CN_player.yco + y_view: # this loops seems prettiest way
                    if x_cor == CN_player.xco + x_view: # but a bit confusing
                        if i_square == 0:
                            CN_indexed.big_box.append(CN_cursor_pos())
                            if CN_play_board.contents[CN_player.yco + y_view][CN_player.xco + x_view] == CN_door.icon: # if door is in sight tag coords
                                CN_indexed.door = CN_cursor_pos()
                                CN_door_state.in_sight = True  # good opportunity to determine if in view
                            if CN_play_board.contents[CN_player.yco + y_view][CN_player.xco + x_view] == CN_ghost.icon: # ghost in sight
                                CN_indexed.ghost = CN_cursor_pos()
                                CN_ghost_state.in_sight = True
                            if CN_play_board.contents[CN_player.yco + y_view][CN_player.xco + x_view] == CN_monster.icon: # monster
                                CN_indexed.monster = CN_cursor_pos()
                                CN_monster_state.in_sight = True  
                        elif i_square == 1:
                            CN_indexed.mid_box.append(CN_cursor_pos())
                        elif i_square == 2:
                            CN_indexed.sma_box.append(CN_cursor_pos())
                            if CN_play_board.contents[CN_player.yco + y_view][CN_player.xco + x_view] == CN_ghost.icon: # if ghost is within touch
                                CN_ghost.key = True # great opportunity to determine if in touch
                            if CN_play_board.contents[CN_player.yco + y_view][CN_player.xco + x_view] == CN_monster.icon: # if monster within touch
                                CN_monster.key = True
        cor_min = cor_min + 1 # make the 'box' smaller with each loop iteration
        cor_max = cor_max - 1

#print to screen
def CN_print_screen(event):
    # make sure door is showing - it might have been stepped on
    if CN_player.yco != CN_door.yco:
        if CN_player.xco != CN_door.xco:
            CN_play_board.contents[CN_door.yco][CN_door.xco] = CN_door.icon
    #store lists for coords of area surrounding player
    CN_indexed.big_box = [] # empty the lists each time
    CN_indexed.mid_box = []
    CN_indexed.sma_box = []
    #prepare some variables
    CN_door_state.in_sight = False
    CN_ghost_state.in_sight = False
    CN_monster_state.in_sight = False
    CN_text.delete(1.0,'end')  # clears all text
    CN_text.insert('end','\n')
    #set display message colour and print
    CN_indexed.pm = CN_cursor_pos()
    CN_text.insert('end','\t\t\t' + CN_play_board.message + '\n')
    CN_indexed.pm_e = CN_cursor_pos()
    CN_text.insert('end','\t')
    #loops through the dimensions of the grid / list, checks values, displays contents, prints GUI.
    for y_cor in range(CN_play_area_y):      
        for x_cor in range(CN_play_area_x):
            CN_view_square(y_cor,x_cor) # call the function to colour tag viewable area
            if y_cor == CN_player.yco -3: 
                if x_cor == CN_player.xco - 3:
                    CN_indexed.nw = CN_cursor_pos() # get coords of relative corners for roundness
            if y_cor == CN_player.yco -3:
                if x_cor == CN_player.xco + 3:
                    CN_indexed.ne = CN_cursor_pos()
            if y_cor == CN_player.yco +3:
                if x_cor == CN_player.xco - 3:
                    CN_indexed.sw = CN_cursor_pos()
            if y_cor == CN_player.yco +3:
                if x_cor == CN_player.xco + 3:
                    CN_indexed.se = CN_cursor_pos()       
            # tags player index for colour
            if CN_play_board.contents[y_cor][x_cor] == CN_player.icon:
                CN_indexed.player = CN_cursor_pos()
            #finally gets around to printing contents and gui
            CN_text.insert('end',CN_play_board.contents[y_cor][x_cor])
            ### ^ main part of function!
        if y_cor == 3:
            CN_indexed.ph = CN_cursor_pos() # get index of and display gui health
            CN_text.insert('end',"\tHealth: ")
            CN_text.insert('end',CN_player.health)
            CN_indexed.ph_e = CN_cursor_pos()
        elif y_cor == 5:
            CN_indexed.pk = CN_cursor_pos() # key
            CN_text.insert('end',"\tKey: ")
            if CN_player.key == True:
                CN_text.insert('end',"Yes") # turn boolean into text
            elif CN_player.key == False:
                CN_text.insert('end',"No")
            CN_indexed.pk_e = CN_cursor_pos()
        # end of line, newline time.. 
        if x_cor == CN_play_area_x -1: # if x axis is at total -1 do newline. like a typewriter
            CN_text.insert('end',"\n\t")
    CN_text.insert('end',"\n")
    CN_text.see('end') # scroll to end # probably unecessary
    CN_tag_config_colour() # run the colour config function

def CN_tag_config_colour():
    #add tags
    for i in range(49):   # this is y_view * x_view in view square, for each loop iteration 
        CN_text.tag_add("big_box",CN_indexed.big_box[i]) # biggest square darkest
    for i in range(25):
        CN_text.tag_add("mid_box",CN_indexed.mid_box[i]) # mid square medium
    for i in range(9):
        CN_text.tag_add("sma_box",CN_indexed.sma_box[i]) # small square lightest
    #player colour
    CN_text.tag_add("player",CN_indexed.player) # tag index
    #message colour
    CN_text.tag_add("view_pm",CN_indexed.pm, CN_indexed.pm_e)
    #gui colours
    CN_text.tag_add("view_ph",CN_indexed.ph,CN_indexed.ph_e)
    CN_text.tag_add("view_pk",CN_indexed.pk,CN_indexed.pk_e)
    # check nobody is standing over door and it is in view before config colour
    # this lets us use different colour, but keeps it invisible rest of time
    if CN_play_board.contents[CN_door.yco][CN_door.xco] == CN_door.icon:
        if CN_door_state.in_sight == True:
            CN_text.tag_add("door",CN_indexed.door) # tag index 
    if CN_play_board.contents[CN_ghost.yco][CN_ghost.xco] == CN_ghost.icon: #tag ghost if visible
        if CN_ghost_state.in_sight == True:
            CN_text.tag_add("ghost",CN_indexed.ghost) # tag index
    if CN_play_board.contents[CN_monster.yco][CN_monster.xco] == CN_monster.icon: #tag monster if visible
        if CN_monster_state.in_sight == True:
            CN_text.tag_add("monster",CN_indexed.monster) # tag index
    #tag view corners last
    CN_text.tag_add("dark",CN_indexed.nw)
    CN_text.tag_add("dark",CN_indexed.ne)
    CN_text.tag_add("dark",CN_indexed.sw)
    CN_text.tag_add("dark",CN_indexed.se)
    #colours config
    #view shades
    CN_text.tag_config("big_box",background="black",foreground="gray10") #big dark box
    CN_text.tag_config("mid_box",background="black",foreground="gray18") # medium lighter box
    CN_text.tag_config("sma_box",background="black",foreground="gray35") # small lightest box
    CN_text.tag_config("player",background="black",foreground="green2") #player
    CN_text.tag_config("view_pm",background="black",foreground="white") #level message
    CN_text.tag_config("view_ph",background="black",foreground="red") #health
    CN_text.tag_config("view_pk",background="black",foreground="white") #key
    CN_text.tag_config("dark",background="black",foreground="black") #corners
    CN_text.tag_config("door",background="black",foreground="yellow") #door
    CN_text.tag_config("ghost",background="black",foreground="white")  #ghost
    CN_text.tag_config("monster",background="black",foreground="red") #monster

def CN_death(event):
    if CN_player.health < 0:
        CN_text.delete(1.0,'end')
        CN_text.insert('end', "\n")
        CN_indexed.welcome = CN_cursor_pos()
        CN_text.insert('end', "\t", "\n")
        CN_text.insert('end', CN_you_died_text.art)
        CN_text.insert('end', "\n\t\t")
        CN_text.insert('end', "\n\n\n\n\t\tGame \tover")
        CN_text.insert('end', "\n")
        CN_indexed.welcome_e = CN_cursor_pos()
        CN_text.tag_add("view_welcome", CN_indexed.welcome, CN_indexed.welcome_e)
        CN_text.see('end')
        #CN_ghost.score = 0
        #CN_player.score = 0

def CN_player_won(event):
    if CN_play_board.lvl == CN_number_of_levels:
        CN_text.delete(1.0,'end')
        CN_text.insert('end', "\n")
        CN_indexed.welcome = CN_cursor_pos()
        CN_text.insert('end', "\t", "\n")
        CN_text.insert('end', CN_you_win_text.art)
        CN_text.insert('end', "\n\t")
        CN_text.insert('end', "\n\n\n\n\t\t\tYou \tEscaped")
        CN_text.insert('end', "\n")
        CN_indexed.welcome_e = CN_cursor_pos()
        CN_text.tag_add("view_welcome", CN_indexed.welcome, CN_indexed.welcome_e)
        CN_text.see('end')

#populate classes
CN_indexed = CN_Index() # create indexed object
CN_door_state = CN_GameState()
CN_ghost_state = CN_GameState()
CN_monster_state = CN_GameState()
CN_room1 = CN_Room("One","1")
CN_room2 = CN_Room("Two","2")
CN_room3 = CN_Room("Three","3")
CN_room4 = CN_Room("Four","4")
CN_play_board = CN_Board("Level One",CN_play_area_y,CN_play_area_x,"Room 1",0)
CN_player = CN_Inhabitant("Player", "i",CN_room1.midy,CN_room1.midx,10,0) # player.score tracks question award
CN_door = CN_Inhabitant("Door","D",CN_room2.midy,CN_room2.midx,5,0)    # door scor tracks visibility
CN_ghost = CN_Inhabitant("Ghost","G",CN_room2.midy,CN_room2.midx,5,False) # CN_ghost.score tracks question status
CN_key = CN_Inhabitant("Key","⚷",CN_room3.midy-1,CN_room3.midx,5,0)
CN_wall = CN_Inhabitant("Wall","#",0,0,0,0)
CN_monster = CN_Inhabitant("Monster", "M",CN_room4.midy,CN_room4.midx,10,0)
CN_ghost_qs= CN_Question("What are you doing here?", "1. Exploring", "2. Lost", "3. Lonely", "1. Exploring" )

#randomise number of levels
CN_number_of_levels = int(random.randrange(11, 15))
#randomise monster appearence location
CN_play_board.monster_home = int(random.randrange(3,CN_number_of_levels -2))
CN_make_level()

#prog starts
#CN_print_screen(1) # debug
CN_welcome_screen(1) # junk value = 1
CN_text.pack() # text fill window # use (expand=True, fill='both') but performance
CN_root.bind('<KeyPress>',CN_on_key_press) # player press button
CN_root.bind('<KeyPress>',CN_print_screen,add="+") # additional function
CN_root.bind('<KeyPress>',CN_progress_level,add="+")
CN_root.bind('<KeyPress>',CN_ghost_chat,add="+")
CN_root.bind('<KeyPress>',CN_ghost_result,add="+")
CN_root.bind('<KeyPress>',CN_death,add="+")
CN_root.bind('<KeyPress>',CN_monster_attack,add="+")
CN_root.bind('<KeyPress>',CN_player_won,add="+")
CN_root.mainloop() # looping
