# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# README FILE

#############################################
############# REQUIREMENTS ##################

Python 3.6 or above
ZODB

to install ZODB:

open a terminal and navigate to 
\Python\Python36-32\Scripts

type the following:

./pip install ZODB

follow any further instructions

#############################################
############ FIRST TIME SETUP ###############

##### EXISTING DATABASE ######

unzip database.zip

place database folder in same dirctory as main.py
(db folder should contain 4 Data.fs.x files)

run main.py

##### FRESH DATABASE #####

create empty folder named 'database' in same directory as main.py

execute initialise_DB.py

(this will create an empty database, overwriting any database that exists)


##############################################
############### LAUNCH #######################

execute main.py

##############################################
################ DATA ########################

the database is stored in \database in the following files:

Data.fs
Data.fs.index
Data.fs.lock
Data.fs.tmp

These files can be copied and stored as backups, and restored accordingly.

#####################################################
#################  MISC HELP ########################

************************************
to add a category u need to edit:

classes.py - descendants of root (and update latest key in Ograniser class)
Z_mod.py - database add_to_db function
initialise_DB - structure database

************************************
regarding names:

emyrs will remove spaces from names of additions, and new parameter names
emyrs will remove numbers from names of additions
emyrs will not let you edit an entries name, group, or parent
if you add a parameter name that already exists, youll get a None instead
you can add many objects with the same name, as their index will differ

#########################################