from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import pymysql


class Gym:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.minsize(1540,800)
        self.root.configure(bg="White")
        self.root.resizable(TRUE,TRUE)
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\barbell.ico")
        self.root.title("GYM")
        l1 = Label(self.root,text="Record progress in weights", bg="#F1C40F" , font=("impact",20))
        l1.pack(fill=X)
        
        # ------------------- variables ------------------------- 
        
        self.week_var = StringVar()
        self.Exercise_var = StringVar()
        self.weight_var = StringVar()
        self.iteration_var = StringVar()
        self.delete = StringVar()
        self.exe_table = StringVar()
        self.search_combo = StringVar()
        self.search_var = StringVar()
        
        # -------------------------------- frame -----------------------

        
        #------------------ frame 1 --------------------
        fr1 =Frame(self.root,bg="#7B7D7D")
        fr1.place(x=1230,y=40 ,width=310,height=350)
        
        l1= Label(fr1,text="Week & number",font=("impact",15), bg="#7B7D7D")
        l1.pack()
        week_Entry = Entry(fr1,bd=4 ,font=("New Timer Roman",15),textvariable=self.week_var,justify="center")
        week_Entry.pack()
        
        l2 = Label(fr1,text="Exercise", font=("impact",15), bg="#7B7D7D")
        l2.pack()
        exercise_Entry = Entry(fr1,bd=4 ,font=("New Timer Roman",15),textvariable=self.Exercise_var,justify="center")
        exercise_Entry.pack()
        
        l3 = Label(fr1,text="Weight", font=("impact",15), bg="#7B7D7D")
        l3.pack()
        weight_Entry = Entry(fr1,bd=4 ,font=("New Timer Roman",15),textvariable=self.weight_var,justify="center")
        weight_Entry.pack()
        
        l4 = Label(fr1,text="Iteration", font=("impact",15), bg="#7B7D7D")
        l4.pack()
        Iteration_Entry = Entry(fr1,bd=4 ,font=("New Timer Roman",15),textvariable=self.iteration_var,justify="center")
        Iteration_Entry.pack()
        
        l5 = Label(fr1,text=" Delete Accroding (Week & Number)", font=("impact",15), bg="#7B7D7D" , fg="#FA1212")
        l5.pack()
        round_Entry = Entry(fr1,bd=4 ,font=("New Timer Roman",15),textvariable=self.delete ,justify="center")
        round_Entry.pack()
        
        # ---------------------- Button Feilds ----------------
        
        fr2 = Frame(self.root,bg="#7B7D7D")
        fr2.place(x= 1230 , y= 390, width=310  ,height=410)
        
        lbl_Tables = Label(fr2,text="Exercise :", font=("impact", 20), bg="black",fg="#F1C40F")
        lbl_Tables.pack(fill= X)
        
        exe_combobox = ttk.Combobox(fr2 , values=('chest','back','shoulder','arm','leg'),font=("impact",15),textvariable=self.exe_table)
        exe_combobox.place(x= 80 ,y=50,width=150 , height= 40)
        
        Button_label_fields = Label(fr2 , text="Button Feilds" , font=("impact", 15), fg="#F1C40F",bg="black")
        Button_label_fields.place(x= 0 , y= 100, width=310)
        
        show_button = Button(fr2,text="show",font=("impact",15), bd=4 , command=self.show_data)
        show_button.place(x= 80 , y= 140 ,width=150 , height= 40)
        
        add_button = Button(fr2,text="Add",font=("impact",15),bd=4,command=self.Add_data)
        add_button.place(x= 80 , y= 180 ,width=150 , height= 40)
        
        update_button = Button(fr2,text="Update",font=("impact",15),bd=4,command=self.update)
        update_button.place(x= 80 , y= 220 ,width=150 , height= 40)
        
        delete_button = Button(fr2,text="Delete",font=("impact",15),bd=4 , command=self.delete_data)
        delete_button.place(x= 80 , y= 260 ,width=150 , height= 40)
        
        clear_button = Button(fr2,text="Clear",font=("impact",15),bd=4 , command=self.clear_data)
        clear_button.place(x= 80 , y= 300 ,width=150 , height= 40)
        
        Exit_button = Button(fr2,text="Exit",font=("impact",15),bd=4, command=root.quit,bg="#FA1212")
        Exit_button.place(x= 80 , y= 340 ,width=150 , height= 40)
        
        # ------------------------ Search Bar -------------------------
        
        fr3 =Frame(self.root,bg="#7B7D7D")
        fr3.place(x=0 , y= 40 , width=1230 , height=80)
        
        lbl_search = Label(fr3,text="Search Bar",font=("impact",15),bg="black",fg="#F1C40F")
        lbl_search.pack(fill=X)
        
        lbl_search1 = Label(fr3,text="Search Accroding to:",font=("impact",15),bg="gray")
        lbl_search1.place(x= 0 , y=40, width=200,height=30)
        
        search_combobox = ttk.Combobox(fr3,values=("Week_number","Exercise","Weight","Iteration"),font=("impact",15),textvariable=self.search_combo)
        search_combobox.place(x= 200,y=40 , width=200, height=30 )
        
        lbl2 = Label(fr3,text="search for :",font=("impact",15),bg="gray")
        lbl2.place(x= 500,y=40,width=200,height=30)
        
        search_entry = Entry(fr3,bd=4 ,font=("New Times Roman",15),textvariable=self.search_var)
        search_entry.place(x= 650 , y= 40 , width=200 , height=30)
        
        Search_Button = Button(fr3,text="Search",font=("impact",15),command=self.search_data)
        Search_Button.place(x=950,y= 40,width=151 , height= 30)
        
        
        # --------------------- database Form ------------------------
        fr4 = Frame(self.root,bg= "white")
        fr4.place(x=0 , y=120 , width=1230 ,height=680)
        #---------------- scrol bar ------------------------------
        scrollbar_y = Scrollbar(fr4,orient="vertical")
        # --------------------- treeview ---------------------
        
        self.gym_detail= ttk.Treeview(fr4,columns=("Week_number","Exercise","Weight", "Iteration"), xscrollcommand= scrollbar_y.set) 
        self.gym_detail.place(x=0 , y=0,width=1230,height=680)
        scrollbar_y.pack(fill=Y,side=LEFT)
        scrollbar_y.config(command=self.gym_detail.yview)
        
        self.gym_detail['show'] = 'headings'
        self.gym_detail.heading('Week_number', text ='Week & number' )
        self.gym_detail.heading('Exercise',text='Exercise')
        self.gym_detail.heading('Weight',text='Weight')
        self.gym_detail.heading('Iteration',text='Iteration')
        
        self.gym_detail.column('Week_number',width=20)
        self.gym_detail.column('Exercise',width=20)
        self.gym_detail.column('Weight',width=20)
        self.gym_detail.column('Iteration',width=20)
       
        
        #---------------- Functions ----------------------------
     # ---------------------- add_data ----------------------------   
    def Add_data (self):
        if self.week_var.get()== '' or self.Exercise_var.get()=='' or self.weight_var.get()=='' or self.iteration_var.get() =='' or self.exe_table.get()==''  : 
            messagebox.showwarning("Warning","You must Add all data")    
        else:
            con = pymysql.connect( host="localhost", user="root", password="123456", database="gym")
            cur = con.cursor()   
            cur.execute("insert into "+ str(self.exe_table.get()) +" values (%s,%s,%s,%s)",(self.week_var.get(),self.Exercise_var.get(),self.weight_var.get(),self.iteration_var.get()))
            con.commit()
            self.show_data()
            self.clear_data()
            con.close()
      
            
        
        # ----------------------- show_data --------------------
    def show_data(self):
        con = pymysql.connect( host="localhost", user="root", password="123456", database="gym")
        cur = con.cursor()  
        cur.execute("Select * from "+ self.exe_table.get())
        rows = cur.fetchall()
        if len(rows)!= 0 : 
            self.gym_detail.delete(*self.gym_detail.get_children())
            for row in rows:
                self.gym_detail.insert("",END,values=row)
        messagebox.showinfo("SUCCESS","THE DATA IS SHOWN NOW")
        
        con.commit()
        con.close()
        
    # -------------------------------- update_data --------------------- 
    
    def update (self):
        con = pymysql.connect( host="localhost", user="root", password="123456", database="gym")
        cur = con.cursor()  
        cur.execute("Update " + str(self.exe_table.get()) +" set Exercise = %s , Weight = %s , Iteration = %s where Week_number = %s",(self.Exercise_var.get(),self.weight_var.get(),self.iteration_var.get(),self.week_var.get()))
        con.commit()
        self.show_data()
        self.clear_data()
        con.close()
        
    # ------------------------ delete _data ---------------------
    
    def delete_data(self): 
        con = pymysql.connect( host="localhost", user="root", password="123456", database="gym")
        cur = con.cursor()  
        cur.execute("delete from " + str(self.exe_table.get()) +" where Week_number = %s ",(self.delete.get()))
        con.commit()
        self.show_data()
        self.clear_data()
        messagebox.showinfo("SUCCESS","DELTED")
        con.close()
        
        
    # -------------------- clear ------------------
    
    def clear_data(self):
        self.week_var.set('')
        self.Exercise_var.set('')
        self.weight_var.set('')
        self.iteration_var.set('')
        self.delete.set('')
        self.search_var.set('')
        
        
        
    # ------------------- search data ---------------------------
            
    def search_data(self):
        if self.exe_table.get()=='' and self.search_combo.get()=='':
            messagebox.showwarning("WARNING","CHECK YOUR ADDED DATA")
        elif self.exe_table.get()=='':
            messagebox.showwarning("WARNING","YOU FORGOT TO ADD THE TABLE")
        elif self.search_combo.get()=='':
            messagebox.showwarning("WARNING","YOU FORGET TO ADD WHICH DATA FOR SEARCH")
        else:
            con = pymysql.connect( host="localhost", user="root", password="123456", database="gym")
            cur = con.cursor()  
            cur.execute("Select * from " +str(self.exe_table.get())+ " where " +str(self.search_combo.get())+ " like '%"+str(self.search_var.get())+ "%'")
            rows = cur.fetchall()
            if len(rows)!= 0 : 
                self.gym_detail.delete(*self.gym_detail.get_children())
                for row in rows:
                    self.gym_detail.insert("",END,values=row)
            messagebox.showinfo("SUCCESS","THE DATA UPDATED")
            con.commit()
            con.close()
               
root = Tk()
ob = Gym(root)
root.mainloop()