from tkinter import *
from tkinter import messagebox
import sys


root = Tk()
root.geometry("900x600+350+75")
root.resizable(False,False)
root.config(bg="#00ADB5")
root.title("Register")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\cpu.ico")

input = StringVar()
N_shifts = StringVar()
Bits = []
input.set("0")
N_shifts.set("0")


def load_data(): 
    global Bits
    Bits.clear()
    numburs = list(input.get())
    for x in numburs:
        Bits.append(int(x))
    register_label.config(text=f"Regster Content = {Bits}")
    output_label.config(text=f"Regster intial Content = {Bits}")
        
          
def Shift_Right():
        for x in range(1):
            number = N_shifts.get()
            Bits.insert(x,int(number))
            Bits.pop(-1)  
        register_label.config(text=f"Regster Content = {Bits}")
    
             
def Shift_left():
        for x in range(1):
            Number = N_shifts.get()
            Bits.append(int(Number))
            Bits.pop(0)
            register_label.config(text=f"Regster Content = {Bits}")
    
        
def Clear():
    global Bits
    Bits.clear()
    input.set("0")
    N_shifts.set("0")
    register_label.config(text=f"Regster Content = {Bits}")
    output_label.config(text=f"Regster intial Content = {Bits}")

    
def complement():
    global Bits
    for x in range(len(Bits)):
        if Bits[x] == 0 :
            Bits[x] = 1
        else:
            Bits[x] = 0
    register_label.config(text=f"Regster Content = {Bits}")
    
    
            
def Shift_Right_circulate():
        for x in range(1):
            last = Bits[-1]
            Bits.insert(0,last)
            Bits.pop(-1)
        register_label.config(text=f"Regster Content = {Bits}")
   

def Shift_Left_circulate():
        for x in range(1):
            First = Bits[0]
            Bits.append(First)
            Bits.pop(0)
        register_label.config(text=f"Regster Content = {Bits}")
    

def exit():
    ques =  messagebox.askyesno("EXIT","Do You Really Want to Exit?")
    if ques == 1:
        root.destroy()
        sys.exit()
    else: 
        return

# ========================================================= photos =====================================================   
frame = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (5).png")
frame_label = Label(root,image=frame,bg="#00ADB5")
frame_label.place(x=-2,y=80)

frame2 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (8).png")
frame_label2 = Label(root,image=frame2,bg="#00ADB5")
frame_label2.pack()

cpu_photo = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\cpu.png")
cpu_photo_2 = cpu_photo.subsample(5,5)
cpu_label2 = Label(root,image=cpu_photo,bg="#EEEEEE")
cpu_label2.place(x=352,y=3)

entry = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (6).png")

button = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\Rectangle 1 (7).png")

# ======================================================== frames =======================================================
frame_2 = Frame(root,bg="#393E46")
frame_2.place(x=0,y=190,width=900,height=50)

frame_3 = Frame(root,bg="#393E46")
frame_3.place(x=0,y=350,width=900,height=50)

# ========================================================= Entries =====================================================
entry_frame = Label(root,image=entry,bg="#393E46")
entry_frame.place(x=285,y=95)
input_Entry = Entry(root,bd=0,justify="center",font=("Arial Black",20,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",insertbackground="#00ADB5",textvariable=input)
input_Entry.place(x=300,y=110,width=320,height=55)

entry_frame = Label(root,image=entry,bg="#393E46")
entry_frame.place(x=285,y=255)
N_shifts_Entry = Entry(root,bd=0,font=("Arial Black",20,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",insertbackground="#00ADB5",textvariable=N_shifts,justify="center")
N_shifts_Entry.place(x=300, y=270 , width=320 , height=55)

# ========================================================= Labels =====================================================
input_label = Label(root,text="Register",font=("Pacifico",23),bg="#EEEEEE",fg="#00ADB5")
input_label.place(x=420,y=2)

input_label = Label(root,text="Content",font=("Arial Black",25,"bold"),bg="#393E46",fg="#EEEEEE")
input_label.place(x=120,y=110)

N_shifts_label = Label(root,text="Input",font=("Arial Black",25,"bold"),bg="#393E46",fg="#EEEEEE")
N_shifts_label.place(x=150,y=270)

output_label = Label(frame_2,font=("Arial Black",20,"bold"),bg="#393E46",fg="#EEEEEE")
output_label.config(text=f"Regster intial Content = {Bits}")
output_label.pack()

register_label = Label(frame_3,font=("Arial Black",20,"bold"),bg="#393E46",fg="#EEEEEE")
register_label.config(text=f"Regster Content = {Bits}")
register_label.pack()

# =================================================================== Buttons ======================================
button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=70,y=420)
load_button = Button(root,text="load",font=("Arial Black",15,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",bd=0,command=load_data,activeforeground="#00ADB5")
load_button.place(x=90,y=430,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=270,y=420)
sh_right_circulate_button = Button(root,text="Right circulate",font=("Arial Black",11,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=Shift_Right_circulate)
sh_right_circulate_button.place(x=290,y=430,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=470,y=420)
sh_left_circulate_button = Button(root,text="left circulate",font=("Arial Black",11,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=Shift_Left_circulate)
sh_left_circulate_button.place(x=490,y=430,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=670,y=420)
clear_button = Button(root,text="clear",font=("Arial Black",15,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=Clear)
clear_button.place(x=690,y=430,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=70,y=510)
complement_button = Button(root,text="Complement",font=("Arial Black",13,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=complement)
complement_button.place(x=90,y=520,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=270,y=510)
shift_right_button = Button(root,text="Shift Right",font=("Arial Black",15,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=Shift_Right)
shift_right_button.place(x=290,y=520,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=470,y=510)
shift_left_button = Button(root,text="Shift Left",font=("Arial Black",15,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=Shift_left)
shift_left_button.place(x=490,y=520,width=125,height=60)

button_frame= Label(root,image=button,bg="#393E46")
button_frame.place(x=670,y=510)
exit_button = Button(root,text="Exit",font=("Arial Black",15,"bold"),bg="#EEEEEE",fg="#00ADB5",cursor="hand2",activeforeground="#00ADB5",bd=0,command=exit)
exit_button.place(x=690,y=520,width=125,height=60) 

root.mainloop()