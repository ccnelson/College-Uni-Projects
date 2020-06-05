# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# HELPER FUNCTION MODULE

def gclass_info(n, obj):
    ''' obtain obj info using n as index '''
    y = type(obj).mro()
    y = y[n]
    y = str(y)
    y = y[16:-2]
    return y           

def read_until_space(x):
    ''' reads x until it reaches a space and returns result '''
    y = ""
    for i in x:
            if i != " ":
                y = y + i
            else:
                return y
    return y