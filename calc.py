from tkinter import * 

pro = Tk()
pro.geometry("600x355+500+150")
pro.title("Calculator")
pro.config(bg="#283747")
pro.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\calculator.ico")
pro.resizable(False,False)
# ------------------------ Functions -----------------------
exp=''

def equal():
    global exp 
    try:
        total = str(eval(exp))
        equation.set(total)
        exp = total
    
    except ValueError :
        equation.set("Invalid Error")
        
    except ZeroDivisionError :
        equation.set("Zero Division Error")
   
    except:
        equation.set("Error")
        exp=' '
        
def press(number):
    global exp
    exp = exp + str(number)
    equation.set(exp)
        
def clear ():
    global exp
    equation.set("")
    exp = ' '
# ------------------- Design ------------------

La = Label(pro,text="Simple Calculator",font=("impact", 20), bg='#34495E')
La.place(x=0 , y=0 , width=600 , height=50)

#--------------- Entry -----------------
equation = StringVar()
calc_entry = Entry(pro,bd=4,textvariable=equation, font=("Arial", 20))
calc_entry.place(x= 0 , y= 50 , width=600 , height=50)



# ---------------------------------- Buttons -------------------------

#---------------- Column_1 -------------------
Button_1 = Button(pro,text='1',bd=4,command=lambda:press(1),font=('impact',20 ,'bold'))
Button_1.place(x=0 , y=104 , width=150 ,height=50)

Button_4 = Button(pro,text='4', bd=4 ,command=lambda:press(4), font=('impact', 20))
Button_4.place(x=0,y=155,width=150,height=50)

Button_7 = Button(pro,text='7', bd=4 ,command=lambda:press(7), font=('impact', 20))
Button_7.place(x=0,y=205,width=150,height=50)

Button_comma = Button(pro,text='.', bd=4 , command=lambda:press("."),font=('impact', 20))
Button_comma.place(x=0,y=255,width=150,height=50)

Button_Ans = Button(pro,text='Exit', bd=4 , font=('impact', 20),command=pro.quit,bg='#D35400')
Button_Ans.place(x=0,y=305,width=150,height=50)



# -------------- Column_2 ---------------------

Button_2 = Button(pro,text='2', bd=4 ,command=lambda:press(2), font=('impact', 20))
Button_2.place(x=151,y=104,width=150,height=50)

Button_5 = Button(pro,text='5', bd=4 ,command=lambda:press(5), font=('impact', 20))
Button_5.place(x=151,y=155,width=150,height=50)

Button_8 = Button(pro,text='8', bd=4 ,command=lambda:press(8), font=('impact', 20))
Button_8.place(x=151,y=205,width=150,height=50)

Button_0 = Button(pro,text='0', bd=4 ,command=lambda:press(0), font=('impact', 20))
Button_0.place(x=151,y=255,width=150,height=50)

Button_1 = Button(pro,text='(', bd=4 , command=lambda:press("("),font=('impact', 20))
Button_1.place(x=151,y=305,width=150,height=50)


# ---------------- Column_3 ----------------------

Button_3 = Button(pro,text='3', bd=4 ,command=lambda:press(3), font=('impact', 20))
Button_3.place(x=301,y=104,width=150,height=50)

Button_6 = Button(pro,text='6', bd=4 , command=lambda:press(6),font=('impact', 20))
Button_6.place(x=301,y=155,width=150,height=50)

Button_9 = Button(pro,text='9', bd=4 , command=lambda:press(9),font=('impact', 20))
Button_9.place(x=301,y=205,width=150,height=50)

Button_2 = Button(pro,text='=', bd=4 , font=('impact', 20),command=equal)
Button_2.place(x=301,y=255,width=150,height=50)

Button_2 = Button(pro,text=')', bd=4 , command=lambda:press(")"),font=('impact', 20))
Button_2.place(x=301,y=305,width=150,height=50)


# ------------------ Column_4 ----------------------

Button_plus = Button(pro,text='+', bd=4 ,command=lambda:press("+"), font=('impact', 20))
Button_plus.place(x=451,y=104,width=150,height=50)

Button_muinus = Button(pro,text='-', bd=4 , command=lambda:press("-"),font=('impact', 20))
Button_muinus.place(x=451,y=155,width=150,height=50)

Button_multplication = Button(pro,text='×', bd=4 ,command=lambda:press("×"), font=('impact', 20))
Button_multplication.place(x=451,y=205,width=150,height=50)

Button_divide = Button(pro,text='÷', bd=4 ,command=lambda:press("/"), font=('impact', 20))
Button_divide.place(x=451,y=255,width=150,height=50)

Button_clear = Button(pro,text='C', bd=4 ,command=clear, font=('impact', 20),bg='#D35400')
Button_clear.place(x=451,y=305,width=150,height=50)



pro.mainloop()