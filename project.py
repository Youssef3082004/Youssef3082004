from tkinter import * 
from tkinter import ttk
import pymysql

class Student: 
    # ------------------------ interface for application ----------------------
    
    def __init__(self,root):
        self.root = root 
        self.root.geometry('1530x800+-10+0')
        self.root.title("System for Schools")
        self.root.configure(background = '#797D7F')
        self.root.resizable(True,False)
        self.root.iconbitmap('C:\\Users\\Computec\\Downloads\\Icons\\school.ico')
        l1 = Label(self.root,text='School System',font=('impact',20,'italic'), bg='#3498DB', fg= 'Black')
        l1.pack(fill='x')
        # --------------------- Variables ------------------------------
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.Address_var = StringVar()
        self.Gender_var = StringVar()
        self.delete_var = StringVar()
        self.Search_Var = StringVar()
        self.combosearch = StringVar()
        
        # --------------------- tools for application ------------------------
        
        fr1 = Frame(self.root,bg='white')
        fr1.place(x =1230 , y=40 , width= 300 ,height=500)
        
        lbl_Id = Label(fr1, text='Student ID', fg= 'black', bg='white', font=('impact',15))
        lbl_Id.pack()
        entry_ID= Entry(fr1,bd=4,textvariable=self.id_var)
        
        entry_ID.pack()
        
        lbl_name = Label(fr1, text='Student Name', fg= 'black', bg='white', font=('impact',15))
        lbl_name.pack()
        entry_name= Entry(fr1,bd=4,textvariable=self.name_var)
        entry_name.pack()
        
        lbl_age = Label(fr1, text='Student Age', fg= 'black', bg='white', font=('impact',15))
        lbl_age.pack()
        entry_age= Entry(fr1,bd=4,textvariable=self.age_var)
        entry_age.pack()
        
        lbl_email = Label(fr1, text='Student E-mail', fg= 'black', bg='white', font=('impact',15))
        lbl_email.pack()
        entry_email= Entry(fr1,bd=4,textvariable=self.email_var)
        entry_email.pack()
        
        lbl_phone = Label(fr1, text='Student Phone', fg= 'black', bg='white', font=('impact',15))
        lbl_phone.pack()
        entry_phone= Entry(fr1,bd=4,textvariable=self.phone_var)
        entry_phone.pack()
        
        lbl_address = Label(fr1, text='Student Address', fg= 'black', bg='white', font=('impact',15))
        lbl_address.pack()
        entry_address= Entry(fr1,bd=4,textvariable=self.Address_var)
        entry_address.pack()
        
        lbl_gender = Label(fr1, text='Student Gender', fg= 'black', bg='white', font=('impact',15))
        lbl_gender.pack()
        ch = ttk.Combobox(fr1,values=('Male','Famale'),state='readonly',font=('impact',10),textvariable=self.Gender_var)
        ch.pack()
        
        lbl_del = Label(fr1, text='Delete Student', fg= 'red', bg='white', font=('impact',15))
        lbl_del.pack()
        entry_del= Entry(fr1,bd=4,textvariable=self.delete_var)
        entry_del.pack()
        
        # ----------------- Buttons -------------------
        
        fr2 = Frame(self.root, bg= '#45B39D')
        fr2.place(x =1230 , y=520 , width= 300 ,height=280)
        
        lbl_Buttons = Label(fr2, text='Buttons Field', bg='#3498DB', fg= 'Black', font=('impact'))
        lbl_Buttons.pack(fill=X)
        
        add_button = Button(fr2, text='Add', font='impact', bg='#95A5A6', bd=4,command=self.Add_student)
        add_button.place(x=80 , y= 40, width=150 , height= 30)
        
        show_button = Button(fr2, text='Show', font='impact', bg='#95A5A6', bd=4,command=self.show_data)
        show_button.place(x=80 , y= 70, width=150 , height= 30)
        
        update_button = Button(fr2, text='Update', font='impact', bg='#95A5A6', bd=4,command=self.update)
        update_button.place(x=80 , y= 100, width=150 , height= 30)
         
        clear_button = Button(fr2, text='Clear', font='impact', bg='#95A5A6', bd=4, command=self.clear_entry)
        clear_button.place(x=80 , y= 130, width=150 , height= 30)
         
        delete_button = Button(fr2, text='Delete', font='impact', bg='#95A5A6', bd=4, command=self.delete_data)
        delete_button.place(x=80 , y= 160, width=150 , height= 30)
         
        exit_button = Button(fr2, text='Exit', font='impact', bg='red', bd=4, command= root.quit)
        exit_button.place(x=80 , y= 190, width=150 , height= 30)
        
        # -------------------------- Search Bar ----------------------------
        
        fr3 = Frame(self.root , bg= 'White')
        fr3.place(x=0 , y= 40 , width=1230, height=60)
        
        lbl_search = Label(fr3 , text='Search for Student :', bg='white', font=('impact'))
        lbl_search.place(x=10, y= 15)
        
        ch_search = ttk.Combobox(fr3,values=('ID', 'name_' , 'Phone', 'E_mail', 'Address'), font=('impact',10),textvariable=self.combosearch)
        ch_search.place(x=200 , y= 20)
        
        search_entry= Entry(fr3,bd= 4,textvariable=self.Search_Var)
        search_entry.place(x=500 , y=20 )
        
        search_button = Button(fr3,text='Search',font='impact', bg='#95A5A6', bd=4,command=self.search_data)
        search_button.place(x=750, y=15, width=150,height=30)
        
        # ------------------------ detail frame ------------------------
        
        fr4 = Frame(self.root, bg='#BDC3C7')
        fr4.place(x=0 ,y = 100 , width=1230,height=700)
        # ---------  scrollbar -----------
        scroll_x = Scrollbar(fr4,orient=HORIZONTAL)
        scroll_y = Scrollbar(fr4,orient=VERTICAL)
        # -------- treeview -------------
        self.student_table = ttk.Treeview(fr4,columns=('ID','Name','Age','E-mail','Phone','Address','Gender'),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        self.student_table.place(x= 0 , y= 0,width=1210,height=680)
        scroll_x.pack(fill=X,side=BOTTOM)
        scroll_y.pack(fill=Y , side=RIGHT)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show']= 'headings'
        self.student_table.heading('ID',text='ID')
        self.student_table.heading('Name',text='Name')
        self.student_table.heading('Age',text='Age')
        self.student_table.heading('E-mail',text='E-mail')
        self.student_table.heading('Phone',text='Phone')
        self.student_table.heading('Address',text='Address')
        self.student_table.heading('Gender',text='Gender')
        
        self.student_table.column('ID',width=20)
        self.student_table.column('Name', width=120)
        self.student_table.column('Age',width=20)
        self.student_table.column('E-mail',width=20)
        self.student_table.column('Phone',width=120)
        self.student_table.column('Address',width=120)
        self.student_table.column('Gender', width=20)
        self.student_table.bind("<ButtonRelease-1>",self.cursour)
        
       
    # ---------------- add -----------------
        self.show_data()
    def Add_student(self):
        con = pymysql.connect( host="localhost", user="root", password="123456", database="student")
        cur = con.cursor()                                           #  excute و fetchall بتخليني اقدر  من خلالها ان انا اعمل 
        cur.execute("insert into students values (%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),self.name_var.get(),self.age_var.get(),self.email_var.get(),self.phone_var.get(),self.Address_var.get(),self.Gender_var.get()))
        con.commit()
        self.show_data()
        self.clear_entry()
        con.close()  
        
    # ------------------- show ---------------    
    def show_data(self): 
        con = pymysql.connect( host="localhost", user="root", password="123456", database="student") # اتصال بالداتابيز 
        cur = con.cursor()                                         #  excute و fetchall بتخليني اقدر  من خلالها ان انا اعمل  
        cur.execute("Select * from students")                      # sql بتنفذ كود لغة 
        rows = cur.fetchall()                                      # بيظهر كل البيانات الموجودة في الداتابيز
        if len(rows) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
        con.commit()
        con.close()
        
    # -------------------- delete ----------------
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="123456", database="student")
        cur = con.cursor()                                                #  excute و fetchall بتخليني اقدر  من خلالها ان انا اعمل 
        cur.execute("delete from students where ID = (%s)",(self.delete_var.get()))
        con.commit()
        self.show_data()
        self.delete_var.set('')
        con.close()
        
    # ------------------ clear Data from Entries ----------------------  
    def clear_entry(self):
        self.id_var.set('')
        self.name_var.set('')
        self.age_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.Address_var.set('')
        self.Gender_var.set('')
        
    # ------------------ Search --------------------------
    def search_data (self): 
        con = pymysql.connect( host="localhost", user="root", password="123456", database="student")
        cur = con.cursor()   
        cur.execute("Select * from students where " + str(self.combosearch.get())+ " like '%"+ str(self.Search_Var.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
        con.commit()
        con.close()
        
        
    # ------------------- cursour ------------------ 
    
    def cursour (self,ev):
        data=self.student_table.focus()
        data2 = self.student_table.item(data)
        row = data2['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.age_var.set(row[2])
        self.email_var.set(row[3])
        self.phone_var.set(row[4])
        self.Address_var.set(row[5])
        self.Gender_var.set(row[6])
        
    # -------------------- Update --------------------
    
    def update(self):
        con = pymysql.connect( host="localhost", user="root", password="123456", database="student")
        cur = con.cursor()   
        cur.execute("update students set name_ = %s , Age = %s ,E_mail = %s ,phone = %s , Address = %s , Gender = %s where ID = %s",(self.name_var.get(),self.age_var.get(),self.email_var.get(),self.phone_var.get(),self.Address_var.get(),self.Gender_var.get(),self.id_var.get()))
        con.commit()
        self.show_data()
        self.clear_entry()
        con.close()  
        
root = Tk()
ob = Student(root)
root.mainloop()