from tkinter import *
from tkinter import messagebox
import phonenumbers 
from phonenumbers import carrier , timezone , geocoder






root = Tk()
root.geometry("400x300+570+290")
root.title("Phone Number search")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\Apple.ico")
root.resizable(False,False)
root.config(bg="#424949")
phone = StringVar()


    

def search():
    try:  
        
        phonenumber = phone.get() 
        entered_number = phonenumbers.parse(phonenumber)
        geo = geocoder.description_for_number(entered_number,"en")
        cari = carrier.name_for_number(entered_number,"en")
        timez = timezone.time_zones_for_number(entered_number)
        f1 = Frame(root,bg="#424949")
        f1.place(x=0,y=150,width=400,height=190)
        geo_lbl = Label(f1,text=geo,font=("impact",15),fg="black",bg="#424949")
        geo_lbl.pack()
        cari_lbl = Label(f1,text=cari,font=("impact",15),fg="red",bg="#424949")
        cari_lbl.pack()
        time_lbl = Label(f1,text=timez,font=("impact",15),fg="black",bg="#424949")
        time_lbl.pack()
        
        
    except:
        messagebox.showerror("WARNING","THE STRING SUPPLIED DIDN'T SEEM TO BE A PHONE NUMBER")
        en.insert(0,"+")
        
def clear():
    phone.set("+")
    f2 = Frame(root,bg="#424949")
    f2.place(x=0,y=150,width=400,height=190)
    
            
l1 = Label(root,text="Search for Number",font=("Pacifico",15),fg="#FAD000",bg="Black")
l1.pack(fill=X)
en = Entry(root,bd=6,font=("Arial",15),justify="center",textvariable=phone)
en.insert(0,"+")
en.pack()
btn = Button(root,bd=4,text="Search",command=search,font=("Pacifico",12),bg="#FAD000",fg="Black",width=10)
btn.place(x=85,y=85)
btn1 = Button(root,bd=4,text="Clear",command=clear,font=("Pacifico",12),bg="#FAD000",fg="Black",width=10)
btn1.place(x=205,y=85)

root.mainloop()
