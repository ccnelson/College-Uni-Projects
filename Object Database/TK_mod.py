# CHRIS NELSON
# EMYRS OBJECT DB
# NHC 2018
# TKINTER MODULE

import tkinter as tk
import art as a
import functions as f

art = a.Art()

class GUI_Manager():
    def __init__(self, zodb):
        self.root = tk.Tk()
        self.root.title("Emyrs: OBJECT DATABASE MANAGER v.1 Chris Nelson NHC 2018")
        #self.root.iconbitmap('icon.ico')
        #self.bg = "bisque2"
        #self.fg = "purple4"
        self.bg = "black"
        self.fg = "lawn green"
        self.root.configure(bg=self.bg)
        self.zodb = zodb
        self.count = 0
        self.scratch = ""
        self.scratch_del = None
        self.tmp_ID = 0
        self.add_button_list = []
        self.lvl1 = self.zodb.return_lvl_1()
        self.v = tk.BooleanVar() # tk var which links to radio buttons
        self.w = tk.IntVar()
        
    #################################
    # internal build widget methods #

    def _build_frame(self, par, col, row):
        x = tk.LabelFrame(par, bg=self.bg, fg=self.fg)
        x.grid(column=col, row=row)
        return x

    def _build_frame_label(self, par, lbl, col, row):
        x = tk.LabelFrame(par, text=lbl, bg=self.bg, fg=self.fg)
        x.grid(column=col, row=row)
        return x
        
    def _build_button(self, par, lbl, col, row, exe):
        x = tk.Button(par, text=lbl, bg=self.bg, fg=self.fg, command=exe)
        x.grid(column=col, row=row, padx=5, pady=5, ipadx=5, ipady=5)
        return x

    def _build_label(self, par, lbl, size, col, row):
        x = tk.Label(par, text=lbl, font=("Courier", size), bg=self.bg, fg=self.fg)
        x.grid(column=col, row=row)
        return x

    def _build_text(self, par, content, size, col, row, h, w):
        x = tk.Text(par, font=("Courier", size), bg=self.bg, fg=self.fg, height=h, width=w, insertbackground=self.bg, highlightthickness=0)
        x.insert('end', content)
        x.grid(column=col, row=row)
        return x

    def _build_entry(self, par, col, row):
        x = tk.Entry(par)
        x.grid(column=col, row=row)
        return x

    def _build_listbox(self, par, col, row):
        x = tk.Listbox(par, cursor='hand2', bg=self.bg, fg=self.fg, selectmode=tk.SINGLE, height=23, width=40)
        x.grid(column=col, row=row)
        return x

    ############################################
    # interactive methods / internal functions #

    def update_anim(self):
        ''' animates LSI on welcome screen via .after '''
        self.text_anim_1.delete(1.0, 'end')
        self.text_anim_2.delete(1.0, 'end')
        self.text_anim_1.insert('end', art.animation[self.count])
        self.text_anim_2.insert('end', art.animation[self.count])
        self.text_anim_1.grid()
        self.text_anim_2.grid()
        self.count +=1
        if self.count == 8:
            self.count = 0
        self.root.after(100, self.update_anim)
    
    def end_emyrs(self):
        self.root.destroy()

    def top_level_cat_but_builder(self, frame, command):
        ''' builds dynamics buttons based on database content '''
        for i in self.add_button_list:
            i.destroy()
        self.add_button_list = []
        for i, name in enumerate(self.lvl1):
            self.add_button_list.append(self._build_button(frame, name, i, 0, 
                                            lambda j=i: command(self.lvl1[j])))
        else: 
            self.add_button_list.append(self._build_button(frame, "home", i+2, 0, 
                                            self.go_home))

    def mid_level_cat_but_builder(self, frame, name, command1, command2):
        ''' same as above but for 2nd lvl '''
        for i in self.add_button_list:
            i.destroy()
        x = self.zodb.lvl_2_parent_filter(name)
        for i, n in enumerate(x):
            self.add_button_list.append(self._build_button(frame, n, i, 0, 
                                            lambda j=n: command1(j)))
        else: 
            self.add_button_list.append(self._build_button(frame, "BACK", i+1, 0, 
                                            command2))
            self.add_button_list.append(self._build_button(frame, "home", i+2, 0, 
                                            self.go_home))

    ########### testing / debug ###############

    def do_nothing(self):
        print("I didnt do a thing")

    def test_print(self, x):
        print(x)

    ########### GUI ################
    
    ### view ###

    def go_to_view(self):
        ''' switch the view frame '''
        self.frame_view_categories.configure(text="View")
        for i in self.add_button_list:
            i.destroy()
        self.listbox_view_a.delete(0, 'end')
        self.listbox_view_b.delete(0, 'end')
        for i, a in enumerate(self.zodb.readall_db()):
            self.listbox_view_a.insert(i, a)
        self.top_level_cat_but_builder(self.frame_view_categories, self.view_category_clicked )
        self.frame_welcome.grid_remove()
        self.frame_view.grid()

    def view_category_clicked(self, name):
        ''' category button clicked '''
        self.frame_view_categories.configure(text="View %s" % (name))
        self.mid_level_cat_but_builder(self.frame_view_categories, name, self.filter_view, self.go_to_view)
        self.listbox_view_a.delete(0, 'end')
        self.listbox_view_b.delete(0, 'end')
        self.filter_view(name)

    def filter_view(self, grp):
        ''' filter main listbox by grp'''
        self.listbox_view_a.delete(0, 'end')
        self.listbox_view_b.delete(0, 'end')
        for i, a in enumerate(self.zodb.read_group(grp)):
            self.listbox_view_a.insert(i, a)

    def listbox_view_a_select(self, mouse): # mouse is dummy parameter passed from click
        """ filter 2nd listbox by active content of first """
        self.listbox_view_b.delete(0, 'end')
        y = self.listbox_view_a.get(tk.ACTIVE) # get active selection
        b = ''.join(filter(lambda z: z.isdigit(), str(y))) # strip all but numbers
        x = self.zodb.read_by_index(b) # therefore names shouldnt include no's
        for i, j in enumerate(x):
            self.listbox_view_b.insert(i, j)

    ### add ###
    
    def go_to_add(self):
        ''' switch to add frame '''
        self.frame_add_categories.configure(text="Add")
        self.frame_add_entry.grid_remove()
        self.top_level_cat_but_builder(self.frame_add_categories, self.add_category_clicked)
        self.frame_add.grid()
        self.frame_welcome.grid_remove()
    
    def add_category_clicked(self, name):
        self.frame_add_categories.configure(text="Add %s" % (name))
        ''' category button clicked '''
        self.mid_level_cat_but_builder(self.frame_add_categories, name, self.show_add_entry, self.go_to_add)
    
    def show_add_entry(self, group):
        ''' show txt entry frame '''
        self.frame_add_entry.grid()
        self.scratch = group

    def add_button_save(self):
        ''' save txt entry '''
        x = self.add_entry.get()
        y = ''.join(filter(lambda z: z.isalpha(), str(x))) # strip numbers
        self.zodb.add_to_db(y, self.scratch)
        self.add_entry.delete(0, 'end')
        self.frame_add_entry.grid_remove()

    ### edit ###

    def go_to_edit(self):
        ''' swtch to edit frame '''
        self.frame_edit_categories.configure(text="Edit")
        self.frame_edit_entry.grid_remove()
        self.listbox_edit_a.delete(0, 'end')
        self.listbox_edit_b.delete(0, 'end')
        self.top_level_cat_but_builder(self.frame_edit_categories, self.edit_category_clicked)
        self.frame_edit.grid()
        self.frame_welcome.grid_remove()
        self.frame_edit_entry_param.grid_remove()
        self.frame_edit_entry_param_input.grid_remove()

    def edit_category_clicked(self, name):
        ''' category button clicked '''
        self.frame_edit_categories.configure(text="Edit %s" % (name))
        self.frame_edit_entry.grid_remove()
        self.frame_edit_entry_param.grid_remove()
        self.frame_edit_entry_param_input.grid_remove()
        self.mid_level_cat_but_builder(self.frame_edit_categories, name, self.filter_edit, self.go_to_edit)
        self.filter_edit(name)
    
    def filter_edit(self, grp):
        ''' fiter main listbox by grp '''
        self.listbox_edit_b.delete(0, 'end')
        self.frame_edit_entry.grid_remove()
        self.frame_edit_entry_param.grid_remove()
        self.frame_edit_entry_param_input.grid_remove()
        self.listbox_edit_a.delete(0, 'end')
        for i, a in enumerate(self.zodb.read_group(grp)):
            self.listbox_edit_a.insert(i, a)

    def listbox_edit_a_select(self, mouse): # mouse is dummy parameter passed from click
        ''' filer 2nd listbox by active content of first '''
        self.frame_edit_entry.grid_remove()
        self.listbox_edit_b.delete(0, 'end')
        y = self.listbox_edit_a.get(tk.ACTIVE) # get active selection
        b = ''.join(filter(lambda z: z.isdigit(), str(y))) # strip all but numbers
        self.tmp_ID = b
        x = self.zodb.read_by_index(b) # therefore names shouldnt include no's
        for i, j in enumerate(x):
            self.listbox_edit_b.insert(i, j)
        self.edit_param_label.configure(text=self.zodb.return_name(self.tmp_ID))
        self.frame_edit_entry_param.grid()
        

    def edit_entry_show(self, mouse):
        ''' show edit entry frame '''
        self.frame_edit_entry_radio.grid_remove()
        self.frame_edit_entry_spinbox.grid_remove()
        self.frame_edit_entry_text.grid_remove()
        x = str(self.listbox_edit_b.get(tk.ACTIVE))
        y = f.read_until_space(x)
        z = self.zodb.return_attr_type(self.tmp_ID, y)
        if z == int:
            self.dynamic_spinbox.delete(0, 'end')
            self.dynamic_spinbox.insert('end', self.zodb.return_param_value(self.tmp_ID, y))
            self.frame_edit_entry_spinbox.grid()
        elif z == str:
            self.dynamic_entry.delete(0, 'end')
            self.dynamic_entry.insert('end', self.zodb.return_param_value(self.tmp_ID, y))
            self.frame_edit_entry_text.grid()
        elif z == bool:
            self.v.set(self.zodb.return_param_value(self.tmp_ID, y))   # v.set() allows changing of content of
            self.frame_edit_entry_radio.grid()                         # radio buttons to match param

        y = self.zodb.return_name(self.tmp_ID) + "\n" + y 
        self.edit_entry_label.configure(text=y)
        self.frame_edit_entry.grid()


    def edit_save_entry(self):
        ''' save txt input '''
        x = str(self.listbox_edit_b.get(tk.ACTIVE))
        y = f.read_until_space(x)
        if y == "group" or y == "parent" or y == "name" :
            self.dynamic_entry.delete(0, 'end')    
            return
        self.zodb.update_record(self.tmp_ID, y, self.dynamic_entry.get())
        self.listbox_edit_a_select(1)
        self.dynamic_entry.delete(0, 'end')
        self.frame_edit_entry.grid_remove()

    def edit_save_spinbox(self):
        ''' save int input '''
        x = str(self.listbox_edit_b.get(tk.ACTIVE))
        y = f.read_until_space(x)
        if y == "group" or y == "parent":
            self.dynamic_spinbox.delete(0, 'end')    
            return
        self.zodb.update_record(self.tmp_ID, y, self.dynamic_spinbox.get())
        self.listbox_edit_a_select(1)
        self.dynamic_spinbox.delete(0, 'end')
        self.frame_edit_entry.grid_remove()

    def edit_save_radio(self):
        ''' save bool input '''
        x = str(self.listbox_edit_b.get(tk.ACTIVE))
        y = f.read_until_space(x)
        if y == "group" or y == "parent":
            return
        self.zodb.update_record(self.tmp_ID, y, self.v.get())
        self.listbox_edit_a_select(1)
        self.frame_edit_entry.grid_remove()

    def edit_param_input(self):
        ''' show add param frame '''
        self.frame_edit_entry_param_input.grid()
        self.edit_param_entry.delete(0, 'end')

    def edit_param_input_save(self):
        ''' save new param '''
        z = self.w.get()
        x = self.edit_param_entry.get()
        y = f.read_until_space(x)
        if z == 0:
            self.zodb.update_record(self.tmp_ID, y, 0) 
        elif z == 1:
            self.zodb.update_record(self.tmp_ID, y, "empty")
        elif z == 2:
            self.zodb.update_record(self.tmp_ID, y, False)
        self.listbox_edit_a_select(1)
        self.frame_edit_entry_param_input.grid_remove()
        
    ### delete ###

    def go_to_delete(self):
        ''' show delete frame '''
        self.frame_del_categories.configure(text="Delete")
        self.listbox_del.delete(0, 'end')
        self.top_level_cat_but_builder(self.frame_del_categories, self.del_category_cilcked)
        self.frame_welcome.grid_remove()
        self.frame_delete.grid()

    def del_category_cilcked(self, name):
        ''' category button clicked '''
        self.frame_del_categories.configure(text="Delete %s" % (name))
        self.mid_level_cat_but_builder(self.frame_del_categories, name, self.filter_delete, self.go_to_delete)
        self.filter_delete(name)

    def filter_delete(self, grp):
        ''' filter main listbox by grp '''
        self.scratch_del = grp
        self.listbox_del.delete(0, 'end')
        for i, a in enumerate(self.zodb.read_group(grp)):
            self.listbox_del.insert(i, a)

    def delete_record(self):
        ''' delete chosen record '''
        y = self.listbox_del.get(tk.ACTIVE)
        b = ''.join(filter(lambda z: z.isdigit(), str(y)))
        self.zodb.delete_from_db(b)
        self.filter_delete(self.scratch_del)

    ### home ###

    def go_home(self):
        ''' hide all frames and show welcome '''
        self.label_welcome_dbinfo.configure(text=self.zodb.db_info())
        self.frame_welcome.grid()
        self.frame_view.grid_remove()
        self.frame_add.grid_remove()
        self.frame_add_entry.grid_remove()
        self.frame_delete.grid_remove()
        self.frame_edit.grid_remove()
        self.frame_edit_entry.grid_remove()

    #####################################
    ### main methods called from main ###

    def build_GUI(self):
        ''' use helper functions to create GUI '''
        ### welcome ###
        # main frame
        self.frame_welcome = self._build_frame(self.root, 0, 0)
        self.label_welcome_logo = self._build_label(self.frame_welcome, art.title, 8, 1, 0)
        self.text_anim_1 = self._build_text(self.frame_welcome, "", 3, 0, 0, 23, 40)
        self.text_anim_2 = self._build_text(self.frame_welcome, "", 3, 2, 0, 23, 40)
        self.button_welcome_exit = self._build_button(self.frame_welcome, "exit", 2, 2, self.end_emyrs)
        self.label_welcome_dbinfo = self._build_label(self.frame_welcome, self.zodb.db_info(), 8, 0, 4)
        self.label_welcome_dbinfo.grid(columnspan=3)
        # buttons frame
        self.frame_welcome_buttons = self._build_frame_label(self.frame_welcome, "actions", 1, 1)
        self.button_welcome_view = self._build_button(self.frame_welcome_buttons, "View", 0, 1, self.go_to_view)
        self.button_welcome_add = self._build_button(self.frame_welcome_buttons, "Add", 1, 1, self.go_to_add)
        self.button_welcome_edit = self._build_button(self.frame_welcome_buttons, "Edit", 2, 1, self.go_to_edit)
        self.button_welcome_delete = self._build_button(self.frame_welcome_buttons, "Delete", 3, 1, self.go_to_delete)
        
        ### view ###
        # main frame
        self.frame_view = self._build_frame(self.root, 0, 0)
        # category frame
        self.frame_view_categories = self._build_frame_label(self.frame_view, "View", 0, 0)
        self.frame_view_categories.grid(columnspan=2)
        self.listbox_view_a = self._build_listbox(self.frame_view, 0, 1)
        self.listbox_view_b = self._build_listbox(self.frame_view, 1, 1)
        self.listbox_view_a.bind("<Double-Button-1>", self.listbox_view_a_select)

        ### add ###
        # main frame #
        self.frame_add = self._build_frame(self.root, 0, 0)
        self.add_logo = self._build_label(self.frame_add, art.logo, 5, 0, 0)
        # category frame #
        self.frame_add_categories = self._build_frame_label(self.frame_add, "Add", 0, 1)
        self.frame_add_entry = self._build_frame_label(self.frame_add, "enter name:", 0, 2)
        self.add_entry = self._build_entry(self.frame_add_entry, 0, 0)
        self.add_entry_button = self._build_button(self.frame_add_entry, "SAVE", 1, 0, self.add_button_save)

        ### edit ###
        # main frame #
        self.frame_edit = self._build_frame(self.root, 0, 0)
        self.label_edit_logo = self._build_label(self.frame_edit, art.logo, 3, 0, 0)
        self.label_edit_logo.grid(columnspan=2)
        self.listbox_edit_a = self._build_listbox(self.frame_edit, 0, 2)
        self.listbox_edit_a.configure(height=15)
        self.listbox_edit_a.bind("<Double-Button-1>", self.listbox_edit_a_select)
        self.listbox_edit_b = self._build_listbox(self.frame_edit, 1, 2)
        self.listbox_edit_b.configure(height=15)
        self.listbox_edit_b.bind("<Double-Button-1>", self.edit_entry_show)
        # category frame #
        self.frame_edit_categories = self._build_frame_label(self.frame_edit, "Edit", 0, 1)
        self.frame_edit_categories.grid(columnspan=2)
        # entry frame #
        self.frame_edit_entry = self._build_frame_label(self.frame_edit, "EDIT PARAMETER:", 2, 2)
        self.edit_entry_label = self._build_label(self.frame_edit_entry, "property", 10, 0, 0)
        # int
        self.frame_edit_entry_spinbox = self._build_frame_label(self.frame_edit_entry, "integer", 0, 1)
        self.dynamic_spinbox = tk.Spinbox(self.frame_edit_entry_spinbox, from_=-100, to=1000, width=10, bg=self.bg, fg='red', insertbackground="red", buttonbackground=self.bg)
        self.dynamic_spinbox.grid(column=0, row=0)
        self.dynamic_spinbox.delete(0, 'end')
        self.dynamic_spinbox.insert('end', "0")
        self.dynamic_spinbox_button = self._build_button(self.frame_edit_entry_spinbox, "SAVE", 0, 1, self.edit_save_spinbox)
        # txt
        self.frame_edit_entry_text = self._build_frame_label(self.frame_edit_entry, "string", 0, 2) 
        self.dynamic_entry = self._build_entry(self.frame_edit_entry_text, 0, 0)
        self.dynamic_entry.configure(bg=self.bg, fg='red', insertbackground=self.fg)
        self.dynamic_entry_button = self._build_button(self.frame_edit_entry_text, "SAVE", 0, 1, self.edit_save_entry)
        # bool
        self.frame_edit_entry_radio = self._build_frame_label(self.frame_edit_entry, "boolean", 0, 3)
        self.dynamic_radio_true = tk.Radiobutton(self.frame_edit_entry_radio, text="true", variable=self.v, value=True, bg=self.bg, fg='red', indicatoron=False, selectcolor=self.fg)
        self.dynamic_radio_false = tk.Radiobutton(self.frame_edit_entry_radio, text="false", variable=self.v, value=False, bg=self.bg, fg='red', indicatoron=False, selectcolor=self.fg)
        self.dynamic_radio_true.grid(column=0, row=0)
        self.dynamic_radio_false.grid(column=1, row=0)
        self.dynamic_radio_button = self._build_button(self.frame_edit_entry_radio, "SAVE", 0, 1, self.edit_save_radio)
        # param entry frames #
        # option
        self.frame_edit_entry_param = self._build_frame(self.frame_edit, 1, 4)
        self.edit_param_label = self._build_label(self.frame_edit_entry_param, "type", 8, 0, 0)
        self.button_edit_add_param = self._build_button(self.frame_edit_entry_param, "ADD PARAM", 0, 3, self.edit_param_input)
        self.button_edit_add_param.grid(padx=1, pady=1, ipadx=0, ipady=0)
        # extended
        self.frame_edit_entry_param_input = self._build_frame_label(self.frame_edit, "input", 0, 4)
        self.edit_param_input_label = self._build_label(self.frame_edit_entry_param_input, "enter name", 8, 0, 3)
        self.edit_param_radio_int = tk.Radiobutton(self.frame_edit_entry_param_input, text="int", variable=self.w, value=0, bg=self.bg, fg='red', indicatoron=False, selectcolor=self.fg)
        self.edit_param_radio_str = tk.Radiobutton(self.frame_edit_entry_param_input, text="str", variable=self.w, value=1, bg=self.bg, fg='red', indicatoron=False, selectcolor=self.fg)
        self.edit_param_radio_boo = tk.Radiobutton(self.frame_edit_entry_param_input, text="bool", variable=self.w, value=2, bg=self.bg, fg='red', indicatoron=False, selectcolor=self.fg)
        self.edit_param_radio_int.grid(column=0, row=0, padx=1, pady=0, ipadx=8, ipady=0)
        self.edit_param_radio_str.grid(column=0, row=1, padx=1, pady=0, ipadx=8, ipady=0)
        self.edit_param_radio_boo.grid(column=0, row=2, padx=3, pady=0, ipadx=3, ipady=0)
        self.edit_param_entry = self._build_entry(self.frame_edit_entry_param_input, 0, 4)
        self.edit_param_entry.configure(bg=self.bg, fg='red', insertbackground=self.fg)
        self.edit_param_button = self._build_button(self.frame_edit_entry_param_input, "SAVE", 1, 4, self.edit_param_input_save)

        ### delete ###
        # main frame
        self.frame_delete = self._build_frame(self.root, 0, 0)
        self.label_del_logo = self._build_label(self.frame_delete, art.sure, 5, 0, 0)
        self.label_del_logo.grid(columnspan=2)
        self.listbox_del = self._build_listbox(self.frame_delete, 0, 2)
        self.listbox_del.configure(height=15)
        self.button_del = self._build_button(self.frame_delete, "DELETE", 1, 2, self.delete_record)
        # category frame
        self.frame_del_categories = self._build_frame_label(self.frame_delete, "Delete", 0, 1)
        self.frame_del_categories.grid(columnspan=2)
        
        ################## last thing to do ####################
        ######## hide all main frames except welcome ###########
        self.frame_view.grid_remove()
        self.frame_add.grid_remove()
        self.frame_add_entry.grid_remove()
        self.frame_delete.grid_remove()
        self.frame_edit.grid_remove()
        self.frame_edit_entry.grid_remove()
        self.frame_edit_entry_radio.grid_remove()
        self.frame_edit_entry_spinbox.grid_remove()
        self.frame_edit_entry_text.grid_remove()
        self.frame_edit_entry_param.grid_remove()
        self.frame_edit_entry_param_input.grid_remove()

        #####################
        ### testing space ###
        
        #####################
        #####################

    def run_mainloop(self):
        ''' call mainloop function - with after() for animations '''
        self.root.after(0, self.update_anim)
        self.root.mainloop()



