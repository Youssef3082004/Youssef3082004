from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import os


root = Tk()
root.geometry("500x300+550+200")
root.title("Control")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\control-panel.ico")
root.config(bg="white")
root.resizable(False,False)

# ================================= Variables =================================

time = IntVar()
time_combo = StringVar()

# ================================ Functions ===================================
def shutdown():
    if time_combo.get() == "":
        messagebox.showwarning("WARNING","SOMETHING WROMG IN TIME DATA")
    elif time.get() == 0 and (time_combo.get() != "" or time_combo.get()=="TIME UNIT"):
        op=messagebox.askyesno("WARNING","DO YOU WANT TO CLOSE YOUR DEVICE NOW ?")
        if op == YES:
            os.system(("Shutdown /s /t 0"))
        else:
            return      
    elif time_combo.get() == "Hour":
        time_hour = time.get()*3600
        os.system(f"Shutdown /s /t {time_hour}")
    elif time_combo.get() == "Minuit":
        time_min = time.get()*60
        os.system(f"Shutdown /s /t {time_min}")    
    else:
        os.system((f"Shutdown /s /t {time.get()}"))
 

def restart():
    if time_combo.get() == "":
        messagebox.showwarning("WARNING","SOMETHING WROMG IN TIME DATA")
    elif time.get() == 0 and (time_combo.get() != "" or time_combo.get()=="TIME UNIT"):
        op=messagebox.askyesno("WARNING","DO YOU WANT TO RESTART YOUR DEVICE NOW ?")
        if op == YES:
            os.system(("Shutdown /r /t 0"))
        else:
            return
    elif time_combo.get() == "Hour":
        time_hour = time.get()*3600
        os.system(f"Shutdown /r /t {time_hour}")
    elif time_combo.get() == "Minuit":
        time_min = time.get()*60
        os.system(f"Shutdown /r /t {time_min}")
    else:
        os.system((f"Shutdown /r /t {time.get()}"))
        
def cancel():
    op = messagebox.askyesno("WARNING","DO YOU WANT TO CANCEL SHUTDOWN/RESTART OPERATION NOW ?") 
    if op == YES:
        os.system("shutdown /a")
    else:
        return    
# =================================== Interface ===================================

# ------------------------ frame --------------------------
f1 = Frame(root,bg="#03045e")
f1.place(x=0,y=37,width=500,height=265)
# --------------------------- Label ---------------------------
l1 = Label(root,text="Control For Computer",bg="#023e8a",fg="White",font=("Lobster",15))
l1.pack(fill=X)
l2= Label(f1,text="Shutdown or Restart After:",bg="#03045e",fg="white",font=("Lobster",14))
l2.place(x=10,y=60)
l3 = Label(f1,text="AS",bg="#03045e",fg="white",font=("Lobster",14))
l3.place(x=335,y=60)
# ------------------------ Entry ------------------------------
Time_sp= Spinbox(f1,textvariable=time,from_=0 , to=500,font=("Impact",15),justify="center",bd=4)
time.set(0)
Time_sp.place(x=220,y=60,width=100,height=30)

# -------------------- comboBox ---------------------------- 
search_combobox = ttk.Combobox(f1,values=("Hour","Minuit","Seconds"),font=("impact",15),textvariable=time_combo,justify="center")
time_combo.set("TIME UNIT")
search_combobox.place(x= 380,y=60 , width=110, height=31 )

# ---------------------- Buttons ----------------------------  
shutdown_photo = PhotoImage(file=r"C:\\Users\\Computec\Downloads\\PNG Icons\\power-on.png")
res1 = shutdown_photo.subsample(8,8)
restart_photo = PhotoImage(file=r"C:\\Users\\Computec\Downloads\\PNG Icons\\reloading.png")
res2 = restart_photo.subsample(8,8)
cancel_photo = PhotoImage(file=r"C:\\Users\\Computec\Downloads\\PNG Icons\\multiply.png")
res3 = cancel_photo.subsample(8,8)
b1= Button(f1,image=res1,compound=TOP,command=shutdown,fg="white",bg="#f24134",text="SHUTDOWN",font=("lobster",10),bd=4)
b1.place(x=100,y=150)
b2= Button(f1,image=res2,compound=TOP,command=restart,bg="#f24134",fg="white",text="RESTART",font=("lobster",10),bd=4)
b2.place(x=215,y=150)
b3 = Button(f1,image=res3,compound=TOP,command=cancel,bg="#f24134",fg="white",text="CANCEL",font=("lobster",10),bd=4)
b3.place(x=320,y=150)

mainloop()