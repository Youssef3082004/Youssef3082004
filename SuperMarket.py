from tkinter import * 
from tkinter import messagebox
import webbrowser
import pymysql
 
pro = Tk()
pro.geometry("800x450+280+50")
pro.resizable(False,False)
pro.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\store.ico")
pro.title("Mangement System for Supermarket")
l1 = Label(pro,text="Login Page",bg="#0B2F3A",fg="#F1C40F",font=("lobster",17))
l1.pack(fill="x")
# ---------------------- varibales -----------------------
username = StringVar()
password = StringVar()
# --------------------------------- def ----------------------

web1 = "https://www.facebook.com/youssef.awadalla.75"
web2 = "https://www.instagram.com/youssefmustafa232/"
web3 = "https://t.me/youssefmustafa232"
web4 = "https://api.whatsapp.com/qr/GVKMM5CQQQ5YF1?autoload=1&app_absent=0"
def open1():
    webbrowser.open_new(web1)
def open2():
    webbrowser.open_new(web2) 
def open3():
    webbrowser.open_new(web3)
def open4():
    webbrowser.open_new(web4)
    
def signup():
    try:
        con = pymysql.connect(host="localhost", passwd="123456" , user= "root" , database="secretdata")
        cur = con.cursor()
        cur.execute("insert into supermarket values (%s,%s)",(username.get(),password.get()))
        con.commit()
        messagebox.showinfo("SUCCESS","Username and Password Successfully Saved")
        clear()
        con.close()
    except :
        messagebox.showerror("WARNING","SOMETHING WRONG")
    
def login(): 
    con = pymysql.connect(host="localhost", passwd="123456" , user= "root" , database="secretdata")
    cur = con.cursor()
    cur.execute("select * from supermarket where username = %s and password_ = %s ",(username.get(),password.get()))
    
    result = cur.fetchall()
    if result:
        ##lbl.config(text="Done",fg="green" , font=("impact",15))
        messagebox.showinfo("SUCCESS","Correct")
        pro.destroy()
        from SuperMarket2 import Super
        clear()
    else:
        ##lbl.config(text="invalid",fg="red" , font=("impact",15))
        messagebox.showerror("WARNING","Invalid Username or Password")
  
        
def clear (): 
    username.set("")
    password.set("")

# ------------------------- first frame -----------------------------
f1= Frame(pro , width=230 , height=420 , bg="#0B2F3A")
f1.place(x=571 , y=41 )

l1_f1 = Label(f1,text="Developer Accounts",font=("Pacifico",15),bg="#0B2F3A",fg="white")
l1_f1.place(x= 15,y=60,width=200,height=50 )

l2_f1 = Label(f1,text="Developed BY Youssef Mustafa",font=("Pacifico",10),bg="#0B2F3A",fg="#FFCC00")
l2_f1.place(x= 15,y=10,width=200,height=50 )

b1_f1 = Button(f1 ,text="Facebook", font=("Arial",15),background="#F1C40F",command=open1)
b1_f1.place(x=40,y=130,width=150,height=40 )

b2_f1 = Button(f1 ,text="Instagram", font=("Arial",15),background="#F1C40F",command=open2)
b2_f1.place(x=40,y=180,width=150,height=40 )

b3_f1 = Button(f1 ,text="WhatsApp", font=("Arial",15),background="#F1C40F",command=open4)
b3_f1.place(x=40,y=230,width=150,height=40 )

b4_f1 = Button(f1 ,text="telegram", font=("Arial",15),background="#F1C40F",command=open3)
b4_f1.place(x=40,y=280,width=150,height=40 )

b6_f1 = Button(f1 ,text="Exit", font=("impact",15),command=pro.quit , bg="red")
b6_f1.place(x=40,y=330,width=150,height=40 )

# -------------------- second frame --------------------------------------

photo = PhotoImage(file=r"C:\\Users\\Computec\\Downloads\\PNG Icons\\supermarket.png")
ph=photo.subsample(2,2)
label_photo = Label(pro , image = ph)
label_photo.place(x=20,y=40,width=512,height=300)

f2 = Frame(pro,bg="#0B2F3A",width=570,height=130)
f2.place(x=0,y=320)

b1_f2 = Button(f2,text="LOGIN",font=("impact",15),bg="#F1C40F",command=login)
b1_f2.place(x=400,y=15,width=150 , height=40)

b2_f2 = Button(f2,text="SIGN UP",font=("impact",15),bg="#F1C40F", command=signup)
b2_f2.place(x=400,y=55,width=150 , height=40)

l1_f2 = Label(f2,text="username :",font=("impact",20),fg="white",bg="#0B2F3A")
l1_f2.place(x= 10 , y= 15 ,width=150)

l2_f2 = Label(f2,text="password :",font=("impact",20),fg="white",bg="#0B2F3A")
l2_f2.place(x=10,y=60 , width=150)

e1 = Entry(f2,font=("Times New Roman",15),justify='center' ,textvariable=username)
e1.place(x= 170 , y=20 , width=200,height=30 )

e2 = Entry(f2,font=("Times New Roman",15),justify='center',textvariable=password,show="*")
e2.place(x= 170 , y=65 , width=200,height=30 )

lbl = Label(f2,text="",bg="#0B2F3A")
lbl.place(x=445 , y= 95 )
























pro.mainloop()