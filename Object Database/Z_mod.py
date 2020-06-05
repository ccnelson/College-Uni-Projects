# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# ZODB MODULE

import ZODB, ZODB.FileStorage, transaction
import classes as c
import os.path, time

class _DatabaseManager():
    def __init__(self):
        self.storage = ZODB.FileStorage.FileStorage('./database/Data.fs')
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root

    def end_db(self):
        self.db.close()

    def read_by_index(self, index):
        x = []
        for a in vars(self.root.mainline[str(index)]):
            x.append("%s : %s" % (a, str(getattr(self.root.mainline[str(index)], a))))
        return x

    def return_attr_type(self, index, param):
        x = getattr(self.root.mainline[str(index)], param)
        y = type(x)
        return y

    def return_params(self, index):
        x = []
        for a in vars(self.root.mainline[str(index)]):
            x.append(a)
        return x

    def return_param_value(self, index, param):
        x = getattr(self.root.mainline[str(index)], param)
        return x

    def return_name(self, index):
        x = self.root.mainline[str(index)].name
        return x

    def readall_db(self):
        x = [ [ "%s   |   %s   |   %s" % (j, self.root.mainline[j].group, self.root.mainline[j].name) ] 
        for j in self.root.mainline ]  
        return x

    def read_group(self, group):
        """ returns a list of related objects, group and parent """
        x = [ [ "%s   |   %s   |   %s" % (j, self.root.mainline[j].group, self.root.mainline[j].name) ] 
        for j in self.root.mainline if self.root.mainline[j].group == group or 
            self.root.mainline[j].parent == group]
        return x

    def return_lvl_1(self):
        x = []
        for i in range(1, len(self.root.structure)):
            if self.root.structure[str(i)].level == 1:
                x.append(self.root.structure[str(i)].group)
        return x
    
    def lvl_2_parent_filter(self, value):
        x = []
        for i in range(1, len(self.root.structure)+1):
            if self.root.structure[str(i)].parent == value:
                x.append(self.root.structure[str(i)].group)
        return x

    def add_to_db(self, name, group):
        self.root.admin['1'].latest_key += 1
        if group == "Building":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Building()
        elif group == "Location":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Location()
        elif group == "Lodging":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Lodging()
        elif group == "Player":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Player()
        elif group == "NonPlayer":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.NonPlayer()
        elif group == "Monster":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Monster()
        elif group == "Animal":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Animal()
        elif group == "Armour":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Armour()
        elif group == "Weapon":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Weapon()
        elif group == "Gear":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Gear()
        elif group == "Food":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Food()
        elif group == "Magic":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Magic()
        elif group == "Spell":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Spell()
        elif group == "Skill":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Skill()
        elif group == "Quest":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Quest()
        elif group == "Encounter":
            self.root.mainline[str(self.root.admin['1'].latest_key)] = c.Encounter()
        
        else:
            print("group unknown")
        self.root.mainline[str(self.root.admin['1'].latest_key)].name = name
        transaction.commit()
    
    def update_record(self, index, attribute, value):
        """ updates attr of record at index with value """
        setattr(self.root.mainline[str(index)], str(attribute), value)
        transaction.commit()

    def delete_from_db(self, index):
        """ deletes a db entry via index """
        del self.root.mainline[str(index)]
        transaction.commit()
    
    def db_info(self):
        """ return a string with db info """
        y = "STATS\n%i active records\n%s\nmodified %s\nlatest key used %i" % (len(self.root.mainline), 
            self.storage._file_name, time.ctime(os.path.getmtime(self.storage._file_name)), self.root.admin['1'].latest_key)
        return y

_databasemanager = _DatabaseManager() # dunders = singleton pattern

def DatabaseManager(): return _databasemanager

