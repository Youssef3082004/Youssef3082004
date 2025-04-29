import pandas as pd
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


root = Tk()
root.geometry("600x500+500+150")
root.title("Heart Attack Predictor")
root.config(bg="#F4D03F")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\heart-attack.ico")
root.resizable(False,False)
import warnings
warnings.filterwarnings("ignore")


# ======================================================== Variables ==========================================
age = IntVar()
gender = StringVar()
impluse = IntVar()
pressurehight = IntVar()
pressurelow = IntVar()
glucose = StringVar()
kcm = StringVar()
troponin = StringVar()

#======================================================== Clear ===============================================
age.set("")
gender.set("GENDER")
impluse.set("")
pressurehight.set("")
pressurelow.set("")
glucose.set("")
kcm.set("")
troponin.set("")

# ======================================================= Data Mining =======================================
data = pd.read_csv("D:\\Python\\Projects\\Heart Attack.csv")
mapping_data = {"negative":0 , "positive":1}
data["Sick"]=data["class"].map(mapping_data)
data.drop("class",inplace=True,axis=1)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train , x_test , y_train , y_test = train_test_split(x,y,shuffle=False,test_size=0.2,random_state=0)
mms = StandardScaler()
mms_X_train = mms.fit_transform(x_train)
mms_x_test = mms.transform(x_test)
classifier = RandomForestClassifier(n_estimators=100,random_state=0)
classifier.fit(mms_X_train,y_train)

#========================================================= Functions =========================================

def predict():
    try:
        if gender.get()=="Male":
            new_gender = 1
        elif gender.get() == "Famale":
            new_gender = 0
        else:
            messagebox.showerror("Error","Please Choose Gender")
        test = pd.DataFrame({"age":[age.get()],"gender":[new_gender],"impluse":[impluse.get()],
                             "pressurehight":[pressurehight.get()],"pressurelow":[pressurelow.get()],"glucose":[float(glucose.get())],
                             "kcm":[float(kcm.get())],"troponin":[float(troponin.get())]})
        norm = mms.transform(test)
        predict = classifier.predict(norm)
        if predict == 0:
            lbl = Label(fr3,text="According to the patient's diagnosis and analysis,\n he will not suffer a cardiac arrest",bg="#0B2F3A",fg="#12C600",font=("Arial",15,"bold"))
            lbl.place(x=60,y=20)
        else:
            text_1 = "According to the diagnosis and analysis of the patient,\n he will suffer from a heart attack,"
            +"\n and to avoid this condition,\n he must stay away from\n smoking, eating sugars and unhealthy fats,"
            +"\n and stay away from tension, nervousness, and psychological pressure."
            lbl = Label(fr3,text=text_1,bg="#0B2F3A",fg="#FF0400",font=("Arial",13,"bold"))
            lbl.place(x=17,y=0)
    except:  
            messagebox.showerror("Error","You should Enter Only Valid Numbers")
        
            

def clear(): 
    age.set("")
    gender.set("GENDER")
    impluse.set("")
    pressurehight.set("")
    pressurelow.set("")
    glucose.set("")
    kcm.set("")
    troponin.set("")
    fr3 = Frame(root,bg="#0B2F3A")
    fr3.place(x=0,y=368,width=600,height=140)

def exit(): 
    ques =  messagebox.askyesno("EXIT","Do you really want to Exit")
    if ques == 1:
       root.destroy()
    else: 
        return

# ======================================================== Frames ============================================= 
fr1 = Frame(root,bg="#0B2F3A")
fr1.place(x=0,y=39,width=600,height=285)

fr2 = Frame(root,bg="#0B2F3A")
fr2.place(x=0,y=326,width=600,height=40)

fr3 = Frame(root,bg="#0B2F3A")
fr3.place(x=0,y=368,width=600,height=140)
# ========================================================= Labels ============================================= 
l1 = Label(root,bg="#0B2F3A",fg="gold",text="Patient Analysis",font=("Pacifico",12))
l1.pack(fill=X)

l2 = Label(fr2,bg="#0B2F3A",fg="gold",text="Prediction",font=("Pacifico",12))
l2.pack(fill=X)

age_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Age :",font=("Calibri",16,"bold"))
age_label.place(x=3,y=20)

glucose_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Glucose :",font=("Calibri",16,"bold"))
glucose_label.place(x=3,y=70)

impulse_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Impluse :",font=("Calibri",16,"bold"))
impulse_label.place(x=3,y=120)

pressureheight_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Pressure Hight :",font=("Calibri",16,"bold"))
pressureheight_label.place(x=3,y=170)

gender_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Gender :",font=("Calibri",16,"bold"))
gender_label.place(x=300,y=20)

troponin_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Troponin :",font=("Calibri",16,"bold"))
troponin_label.place(x=300,y=70)

kcm_label = Label(fr1,bg="#0B2F3A",fg="gold",text="KCM :",font=("Calibri",16,"bold"))
kcm_label.place(x=300,y=120)

pressurelow_label =  Label(fr1,bg="#0B2F3A",fg="gold",text="Pressure Low :",font=("Calibri",16,"bold"))
pressurelow_label.place(x=300,y=170)

# ============================================== Entries ======================================================

age_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=age)
age_entry.place(x=160,y=23,width=110,height=30)

glucose_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=glucose)
glucose_entry.place(x=160,y=73,width=110,height=30)

impluse_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=impluse)
impluse_entry.place(x=160,y=123,width=110,height=30)

pressureheight_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=pressurehight)
pressureheight_entry.place(x=160,y=173,width=110,height=30)

gender_combobox = ttk.Combobox(fr1,values=("Male","Famale"),font=("impact",15),textvariable=gender,justify="center")
gender.set("GENDER")
gender_combobox.place(x=460,y=23,width=110,height=30)

troponin_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=troponin)
troponin_entry.place(x=460,y=73,width=110,height=30)

kcm_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=kcm)
kcm_entry.place(x=460,y=123,width=110,height=30)

pressurelow_entry = Entry(fr1,bd=4,justify="center",font=("Arial",12,"bold"),textvariable=pressurelow)
pressurelow_entry.place(x=460,y=173,width=110,height=30)

# =================================================== Buttons ================================================= 
predict_button = Button(fr1,text="Result",font=("impact",15),bg="#23D500",command=predict,bd=4)
predict_button.place(x=122,y=230,width=100)

clear_button = Button(fr1,text="Delete",font=("impact",15),bg="gold",command=clear,bd=4)
clear_button.place(x=252,y=230,width=100)

exit_button = Button(fr1,text="Exit",font=("impact",15),bg="red",command=exit,bd=4)
exit_button.place(x=382,y=230,width=100)

root.mainloop()