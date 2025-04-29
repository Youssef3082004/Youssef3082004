from tkinter import * 
from tkinter import messagebox


root = Tk()
root.geometry("600x500+500+150")
root.title("Edit Distance Calculator")
root.config(bg="#F4D03F")
root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\spacing.ico")
root.resizable(False,False)

# ======================================================== Variables ==========================================
Word_1 = StringVar()
Word_2 = StringVar()
#========================================================= Functions =========================================

def LevenshteinD():
    word1 = Word_1.get()
    word2 = Word_2.get()
    m = len(word1)
    n = len(word2)
    if m == 0 and n == 0 :
        messagebox.showerror("Error","You Did't Enter two Words.\n          Please Try Again")
    elif word1 =="":
        messagebox.showerror("Error","You Did't Enter the First Word.\n          Please Try Again")
    elif word2 =="":
        messagebox.showerror("Error","You Did't Enter the Second Word.\n          Please Try Again")
    else:
   
        table = [] 
        for i in range(m + 1):
        
            row = []
            for i in range(n + 1):
                row.append(0)  
            table.append(row)  
        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = min(table[i - 1][j] + 1,  
                                    table[i][j - 1] + 1,  
                                    table[i - 1][j - 1])  
                
                else:
                    table[i][j] = min(table[i - 1][j] + 1, 
                                    table[i][j - 1] + 1,  
                                    table[i - 1][j - 1] + 2)  
        lbl = Label(fr3,text=f"Number of Edit Distances between two Words = {table[-1][-1]} ",bg="#0B2F3A",fg="#12C600",font=("Arial",15,"bold"))
        lbl.place(x=60,y=20)

    
def clear():
    Word_1.set("")
    Word_2.set("")
    fr3 = Frame(root,bg="#0B2F3A")
    fr3.place(x=0,y=368,width=600,height=140)
    
def Exit():
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
l1 = Label(root,bg="#0B2F3A",fg="gold",text="Edit Distance",font=("Pacifico",12))
l1.pack(fill=X)

l2 = Label(fr2,bg="#0B2F3A",fg="gold",text="Number Of Operations",font=("Pacifico",12))
l2.pack(fill=X)

word1_label = Label(fr1,bg="#0B2F3A",fg="gold",text="First Word :",font=("Calibri",19,"bold"))
word1_label.place(x=3,y=40)

word2_label = Label(fr1,bg="#0B2F3A",fg="gold",text="Second Word :",font=("Calibri",19,"bold"))
word2_label.place(x=3,y=150)

# ============================================== photos =====================================================
box1 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\minus-big-symbol (1).png")
sub_box1 = box1.subsample(2,2)
box1_label = Label(root,image=sub_box1,bg="#0B2F3A")
box1_label.place(x=200,y=60)

box2 = PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\minus-big-symbol (1).png")
sub_box2 = box2.subsample(2,2)
box2_label = Label(root,image=sub_box2,bg="#0B2F3A")
box2_label.place(x=200,y=160)

# ============================================== Entries ======================================================
word1_entry = Entry(root,bd=0,justify="center",font=("Arial",20,"bold"),textvariable=Word_1,cursor="hand2",bg="#F4D03F")
word1_entry.place(x=220,y=70,width=220,height=55)

word2_entry = Entry(root,bd=0,justify="center",font=("Arial",20,"bold"),textvariable=Word_2,bg="#F4D03F",cursor="hand2")
word2_entry.place(x=220,y=170,width=220,height=55)

# =================================================== Buttons ================================================= 
predict_button = Button(fr1,text="Calculate",font=("impact",15),bg="#23D500",command=LevenshteinD,bd=4)
predict_button.place(x=122,y=230,width=100)

clear_button = Button(fr1,text="Clear",font=("impact",15),bg="gold",command=clear,bd=4)
clear_button.place(x=252,y=230,width=100)

exit_button = Button(fr1,text="Exit",font=("impact",15),bg="red",command=exit,bd=4)
exit_button.place(x=382,y=230,width=100)

root.mainloop()