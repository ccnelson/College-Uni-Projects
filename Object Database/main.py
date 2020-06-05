# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# MAIN MODULE

import Z_mod as z
import TK_mod as tkm

zodb = z.DatabaseManager()
x_gui = tkm.GUI_Manager(zodb)

x_gui.build_GUI()
x_gui.run_mainloop()

zodb.end_db()
