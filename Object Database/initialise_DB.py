# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# DATABASE INITIALISATION MODULE

import ZODB, ZODB.FileStorage, persistent, BTrees.OOBTree, transaction
import classes as c

storage = ZODB.FileStorage.FileStorage('./database/Data.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

root.mainline = BTrees.OOBTree.BTree()
root.admin = BTrees.OOBTree.BTree()
root.structure = BTrees.OOBTree.BTree()

root.admin['1'] = c.Organiser() # admin purposes

### THESE COMMENTED OUT ENTRIES ARE WHERE A DB COULD BE PRE-POPULATED
### the latest key in classes.py would be incremented to reflect the last entry

#root.mainline['1'] = c.Root() 
#root.mainline['2'] = c.Actor()
#root.mainline['3'] = c.Item()
#root.mainline['4'] = c.Action()
#root.mainline['5'] = c.Place()
#root.mainline['6'] = c.Player()
#root.mainline['7'] = c.NonPlayer()
#root.mainline['8'] = c.Monster()
#root.mainline['9'] = c.Animal()
#root.mainline['10'] = c.Armour()
#root.mainline['11'] = c.Weapon()
#root.mainline['12'] = c.Gear()
#root.mainline['13'] = c.Food()
#root.mainline['14'] = c.Magic()
#root.mainline['15'] = c.Spell()
#root.mainline['16'] = c.Skill()
#root.mainline['17'] = c.Quest()
#root.mainline['18'] = c.Encounter()
#root.mainline['19'] = c.Location()
#root.mainline['20'] = c.Building()
#root.mainline['21'] = c.Lodging()



root.structure['1'] = c.Root() # structural model
root.structure['2'] = c.Actor()
root.structure['3'] = c.Item()
root.structure['4'] = c.Action()
root.structure['5'] = c.Place()
root.structure['6'] = c.Player()
root.structure['7'] = c.NonPlayer()
root.structure['8'] = c.Monster()
root.structure['9'] = c.Animal()
root.structure['10'] = c.Armour()
root.structure['11'] = c.Weapon()
root.structure['12'] = c.Gear()
root.structure['13'] = c.Food()
root.structure['14'] = c.Magic()
root.structure['15'] = c.Spell()
root.structure['16'] = c.Skill()
root.structure['17'] = c.Quest()
root.structure['18'] = c.Encounter()
root.structure['19'] = c.Location()
root.structure['20'] = c.Building()
root.structure['21'] = c.Lodging()


transaction.commit()

for pair in root.mainline.iteritems():
    print(pair)

db.close()
