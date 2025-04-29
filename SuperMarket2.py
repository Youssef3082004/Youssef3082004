from tkinter import * 
import random
from tkinter import messagebox
import datetime

class Super:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1500x800+20+0") 
        self.root.title("Managment System for Supermarket")
        self.root.resizable(False,False)
        self.root.config(bg="#F1C40F")
        self.root.iconbitmap("C:\\Users\\Computec\\Downloads\\Icons\\store.ico")
        l1 = Label(self.root,text="Home",bg="#0B4C5F",fg="white",font=("Lobster",20))
        l1.pack(fill="x")
        
        # --------- food frame variables ----------
        self.rice = IntVar()
        self.pasta = IntVar()
        self.bread = IntVar()
        self.flour = IntVar()
        self.wheat = IntVar()
        self.corn = IntVar()
        self.salt = IntVar()
        self.bulgur = IntVar()
        self.oats = IntVar()
        self.suger = IntVar()
        self.paprika = IntVar()
        self.bean =IntVar()
        self.hummus = IntVar()
        self.lintil = IntVar()
        self.cowpea = IntVar()
        self.milk =IntVar()
        self.water = IntVar()
        
        # ----------------- elec frame variables ------------ 
        self.tv = IntVar()
        self.mobile = IntVar()
        self.laptop = IntVar()
        self.computer = IntVar()
        self.wash = IntVar()
        self.refr = IntVar()
        self.iron = IntVar()
        self.filter = IntVar()
        self.bioler = IntVar()
        self.oven = IntVar()
        self.mixer = IntVar()
        self.vaccum = IntVar()
        self.microwave = IntVar()
        self.fan = IntVar()
        self.wallfan = IntVar()
        self.keyboard = IntVar()
        self.mouse = IntVar()
        
        # ------------------- kitchen tools frame variables --------------
        self.spoon = IntVar()
        self.fork = IntVar()
        self.knifr = IntVar()
        self.grater = IntVar()
        self.dishs = IntVar()
        self.ovenpan = IntVar()
        self.cookingsuit = IntVar()
        self.tray = IntVar()
        self.cuban = IntVar()
        self.glassbottel = IntVar()
        self.tablecloth = IntVar()
        self.pan = IntVar()
        self.frayingpan = IntVar()
        self.airfrayer = IntVar()
        
        # --------------------- other varibles ---------------------------------
        self.name = StringVar()
        self.phone = StringVar()
        self.number = StringVar()
        self.totalfood = StringVar()
        self.totalelec = StringVar()
        self.totalkitchen = StringVar()
        self.totalf = StringVar()
        self.totale = StringVar()
        self.totalk = StringVar()
        
        
        x= random.randint(1,99999)
        self.number.set(str(x))

    # ----------------------- customer frame -----------------------
        customer_frame = Frame(self.root,bd=4,bg="#0B4C5F")
        customer_frame.place(x=0,y=47,width=350,height=250)
        
        customer_data= Label(customer_frame,text="Customer Data",bg="#0B4C5F",fg="red",font=("lobster",20))
        customer_data.place(x=75 ,y=0 )
        
        Customer_name= Label(customer_frame,text="Customer Name : ", bg="#0B4C5F",fg="white",font=("New Times Roman",12))
        Customer_name.place(x= 5, y=45)
        
        Customer_phone= Label(customer_frame,text="Customer Phone : ", bg="#0B4C5F",fg="white",font=("New Times Roman",12))
        Customer_phone.place(x= 5, y=80)
        
        bill_number= Label(customer_frame,text="Bill Number : ", bg="#0B4C5F",fg="white",font=("New Times Roman",12))
        bill_number.place(x= 5, y=115)
        
        ent_name=Entry(customer_frame,justify="center",font=("New Times Roman",12),textvariable=self.name)
        ent_name.place(x=150,y=47)

        ent_phone=Entry(customer_frame,justify="center",font=("New Times Roman",12),textvariable=self.phone)
        ent_phone.place(x=150,y=82)
        
        bill_number=Entry(customer_frame,justify="center",font=("New Times Roman",12),textvariable=self.number)
        bill_number.place(x=150,y=117)
        
        search_Btn = Button(customer_frame,text="Search",font=("impact",15),bg="#F1C40F",command=self.search)
        search_Btn.place(x=100 , y=160 ,width=150,height=40)
        title = Label(customer_frame,text="[ Bills Details ]",font=("impact",15),fg="red",bg="#0B4C5F")
        title.place(x=110 , y=210 )

        
        # ---------------------- Bills ------------------------------- 
        
        bill_frame= Frame(self.root,bg="#0B4C5F")
        bill_frame.place(x=0,y=295 , width=350,height=383)
        
        Scrollbar_y = Scrollbar(bill_frame,orient=VERTICAL)
        Scrollbar_y.pack(side=LEFT,fill=Y)
        self.textarea = Text(bill_frame,yscrollcommand=Scrollbar_y)
        Scrollbar_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH)
        
        # ------------------------ make bill -----------------
        
        makebill_frame = Frame(self.root, bg="#0B4C5F")
        makebill_frame.place(x=0 , y=680,width=700,height=200)
        
        Fatora = Button(makebill_frame,text="Export the Bill",bg="#F1C40F",font=("impact",15),width=13,height=1,command=self.save)
        Fatora.place(x=0,y=10)
        
        total_price = Button(makebill_frame,text="Total Price",bg="#F1C40F",font=("impact",15),width=13,height=1,command=self.total)
        total_price.place(x=150,y=10)
        
        Exit = Button(makebill_frame,text="Exit",bg="red",font=("impact",15),width=13,height=1,command=self.root.quit)
        Exit.place(x=0,y=60)
        
        clear = Button(makebill_frame,text="Clear",bg="#F1C40F",font=("impact",15),width=13,height=1,command=self.clear)
        clear.place(x=150,y=60)
        
        lbl_food = Label(makebill_frame,text="Total Food Cost:",bg="#0B4C5F",fg="#F1C40F",font=("Impact",15))
        lbl_food.place(x=290,y=10)
        
        lbl_elec = Label(makebill_frame,text="Total Electric Tools Cost:",bg="#0B4C5F",fg="#F1C40F",font=("Impact",15))
        lbl_elec.place(x=290,y=40)
        
        lbl_houseware = Label(makebill_frame,text="Total Housewares Cost:",bg="#0B4C5F",fg="#F1C40F",font=("Impact",15))
        lbl_houseware.place(x=290,y=70)
        
        food_entry = Entry(makebill_frame,width=25,font=("Arial",10),textvariable=self.totalfood)
        food_entry.place(x=500,y=15)
        
        elec_entry = Entry(makebill_frame,width=25,font=("Arial",10),textvariable=self.totalelec)
        elec_entry.place(x=500,y=45)
        
        houseware_entry = Entry(makebill_frame,width=25,font=("Arial",10),textvariable=self.totalkitchen)
        houseware_entry.place(x=500,y=75)
        
        # --------------------------- Food Frame --------------------------- 
        
        food_frame = Frame(self.root,bg="#0B4C5F")
        food_frame.place(x=1100,y=47,width=398,height=750)
        
        lbl=Label(food_frame,text="Food Section",bg="#0B4C5F",fg="#F1C40F",font=("Lobster",25))
        lbl.pack()
        
        rice_lbl = Label(food_frame,text="Rice :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        rice_lbl.place(x=10,y=50)
        
        pasta_lbl = Label(food_frame,text="Pasta :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        pasta_lbl.place(x=10,y=90)
        
        bread_lbl = Label(food_frame,text="Bread :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        bread_lbl.place(x=10,y=130)
        
        floar_lbl = Label(food_frame,text="Floar :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        floar_lbl.place(x=10,y=170)
        
        wheat_lbl = Label(food_frame,text="Wheat :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        wheat_lbl.place(x=10,y=210)
        
        corn_lbl = Label(food_frame,text="Corn:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        corn_lbl.place(x=10,y=250)
        
        salt_lbl = Label(food_frame,text="Salt :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        salt_lbl.place(x=10,y=290)
        
        bulgur_lbl = Label(food_frame,text="Bulgur :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        bulgur_lbl.place(x=10,y=330)
        
        oats_lbl = Label(food_frame,text="Oats :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",18))
        oats_lbl.place(x=10,y=370)
        
        Suger_lbl = Label(food_frame,text="Suger :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        Suger_lbl.place(x=10,y=410)
        
        paprika_lbl = Label(food_frame,text="Paprika:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        paprika_lbl.place(x=0,y=450)
        
        bean_lbl = Label(food_frame,text="Bean :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        bean_lbl.place(x=10,y=490)
        
        hummus_lbl = Label(food_frame,text="Hummus:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        hummus_lbl.place(x=0,y=530)
        
        Lintil_lbl = Label(food_frame,text="Lintil :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        Lintil_lbl.place(x=10,y=570)
        
        cowpea_lbl = Label(food_frame,text="Cowpea:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        cowpea_lbl.place(x=0,y=610)
        
        water_lbl = Label(food_frame,text="Water :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        water_lbl.place(x=10,y=650)
        
        milk_lbl = Label(food_frame,text="Milk :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        milk_lbl.place(x=10,y=690)
        
        rice_ent = Entry(food_frame,font=("Arial",15),textvariable=self.rice)
        rice_ent.place(x=140,y=60,width=150,height=20)
        
        pasta_ent = Entry(food_frame,font=("Arial",15),textvariable=self.pasta)
        pasta_ent.place(x=140,y=100,width=150,height=20)
        
        bread_ent = Entry(food_frame,font=("Arial",15),textvariable=self.bread)
        bread_ent.place(x=140,y=140,width=150,height=20)
        
        flour_ent = Entry(food_frame,font=("Arial",15),textvariable=self.flour)
        flour_ent.place(x=140,y=180,width=150,height=20)
        
        wheat_ent = Entry(food_frame,font=("Arial",15),textvariable=self.wheat)
        wheat_ent.place(x=140,y=220,width=150,height=20)
        
        corn_ent = Entry(food_frame,font=("Arial",15),textvariable=self.corn)
        corn_ent.place(x=140,y=260,width=150,height=20)
        
        salt = Entry(food_frame,font=("Arial",15),textvariable=self.salt)
        salt.place(x=140,y=300,width=150,height=20)
        
        bulgur_ent = Entry(food_frame,font=("Arial",15),textvariable=self.bulgur)
        bulgur_ent.place(x=140,y=340,width=150,height=20)
        
        oats_ent = Entry(food_frame,font=("Arial",15),textvariable=self.oats)
        oats_ent.place(x=140,y=380,width=150,height=20)
        
        suger_ent = Entry(food_frame,font=("Arial",15),textvariable=self.suger)
        suger_ent.place(x=140,y=420,width=150,height=20)
        
        paprika_ent = Entry(food_frame,font=("Arial",15),textvariable=self.paprika)
        paprika_ent.place(x=140,y=460,width=150,height=20)
        
        bean_ent = Entry(food_frame,font=("Arial",15),textvariable=self.bean)
        bean_ent.place(x=140,y=500,width=150,height=20)
        
        hummus_ent = Entry(food_frame,font=("Arial",15),textvariable=self.hummus)
        hummus_ent.place(x=140,y=540,width=150,height=20)
        
        lintil_ent = Entry(food_frame,font=("Arial",15),textvariable=self.lintil)
        lintil_ent.place(x=140,y=580,width=150,height=20)
        
        cowpea_ent = Entry(food_frame,font=("Arial",15),textvariable=self.cowpea)
        cowpea_ent.place(x=140,y=620,width=150,height=20)
        
        water_ent = Entry(food_frame,font=("Arial",15),textvariable=self.water)
        water_ent.place(x=140,y=660,width=150,height=20)
        
        milk_ent = Entry(food_frame,font=("Arial",15),textvariable=self.milk)
        milk_ent.place(x=140,y=700,width=150,height=20)
        
        # ------------------------ electric tools --------------------------------
        
        elec_frame=Frame(self.root,bg="#0B4C5F")
        elec_frame.place(x=701,y=47,width=398,height=750)
        
        lbl_2=Label(elec_frame,text="Electric Devices Section",bg="#0B4C5F",fg="#F1C40F",font=("Lobster",25))
        lbl_2.pack()
        
        tv_lbl = Label(elec_frame,text="Tv :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        tv_lbl.place(x=10,y=50)
        
        mobile_lbl = Label(elec_frame,text="Mobile :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        mobile_lbl.place(x=10,y=90)
        
        laptop_lbl = Label(elec_frame,text="Laptop :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        laptop_lbl.place(x=10,y=130)
        
        computer_lbl = Label(elec_frame,text="Computer :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        computer_lbl.place(x=10,y=170)
        
        wash_lbl = Label(elec_frame,text="Washing Machine:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",15))
        wash_lbl.place(x=0,y=215)
        
        refri_lbl = Label(elec_frame,text="refrigerator :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",18))
        refri_lbl.place(x=10,y=250)
        
        iron_lbl = Label(elec_frame,text="Iron :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        iron_lbl.place(x=10,y=290)
        
        filter_lbl = Label(elec_frame,text="Filter :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        filter_lbl.place(x=10,y=330)
        
        boiler_lbl = Label(elec_frame,text="Boiler :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",18))
        boiler_lbl.place(x=10,y=370)
        
        oven_lbl = Label(elec_frame,text="oven :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        oven_lbl.place(x=10,y=410)
        
        mixer_lbl = Label(elec_frame,text="mixer:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        mixer_lbl.place(x=10,y=450)
        
        vaccum_lbl = Label(elec_frame,text="Vaccum :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        vaccum_lbl.place(x=10,y=490)
        
        microwave_lbl = Label(elec_frame,text="Microwave:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        microwave_lbl.place(x=10,y=530)
        
        fan_lbl = Label(elec_frame,text="fan :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        fan_lbl.place(x=10,y=570)
        
        wallfan_lbl = Label(elec_frame,text="wall fan:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        wallfan_lbl.place(x=10,y=610)
        
        keybourd_lbl = Label(elec_frame,text="keyboard :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        keybourd_lbl.place(x=10,y=650)
        
        mouse_lbl = Label(elec_frame,text="mouse :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        mouse_lbl.place(x=10,y=690)
        
        tv_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.tv)
        tv_ent.place(x=160,y=60,width=150,height=20)
        
        mobile_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.mobile)
        mobile_ent.place(x=160,y=100,width=150,height=20)
        
        laptop_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.laptop)
        laptop_ent.place(x=160,y=140,width=150,height=20)
        
        computer_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.computer)
        computer_ent.place(x=160,y=180,width=150,height=20)
        
        wash_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.wash)
        wash_ent.place(x=160,y=220,width=150,height=20)
        
        refei_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.refr)
        refei_ent.place(x=160,y=260,width=150,height=20)
        
        iron_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.iron)
        iron_ent.place(x=160,y=300,width=150,height=20)
        
        filter_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.filter)
        filter_ent.place(x=160,y=340,width=150,height=20)
        
        boiler_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.bioler)
        boiler_ent.place(x=160,y=380,width=150,height=20)
        
        oven_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.oven)
        oven_ent.place(x=160,y=420,width=150,height=20)
        
        mixer_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.mixer)
        mixer_ent.place(x=160,y=460,width=150,height=20)
        
        vaccum_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.vaccum)
        vaccum_ent.place(x=160,y=500,width=150,height=20)
    
        microwave_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.microwave)
        microwave_ent.place(x=160,y=540,width=150,height=20)
        
        fan_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.fan)
        fan_ent.place(x=160,y=580,width=150,height=20)
        
        wallfan_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.wallfan)
        wallfan_ent.place(x=160,y=620,width=150,height=20)
        
        keybourd_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.keyboard)
        keybourd_ent.place(x=160,y=660,width=150,height=20)
        
        mouse_ent = Entry(elec_frame,font=("Arial",15),textvariable=self.mouse)
        mouse_ent.place(x=160,y=700,width=150,height=20)
        
    # ----------------------- kitchen tools -------------------------- 
        house_frame=Frame(self.root,bg="#0B4C5F")
        house_frame.place(x=351,y=47,width=349,height=632)
        
        lbl_3=Label(house_frame,text="Kitchen Items Section",bg="#0B4C5F",fg="#F1C40F",font=("Lobster",25))
        lbl_3.pack()
        
        spoon_lbl = Label(house_frame,text="Spoon :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        spoon_lbl.place(x=10,y=50)
        
        fork_lbl = Label(house_frame,text="Fork :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        fork_lbl.place(x=10,y=90)
        
        knife_lbl = Label(house_frame,text="Knife :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        knife_lbl.place(x=10,y=130)
        
        grater_lbl = Label(house_frame,text="Grater :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        grater_lbl.place(x=10,y=170)
        
        dishs_lbl = Label(house_frame,text="Dishs :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        dishs_lbl.place(x=10,y=215)
        
        ovenpan_lbl = Label(house_frame,text="oven pan :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        ovenpan_lbl.place(x=10,y=250)
        
        cookingsuit_lbl = Label(house_frame,text="Cooking Suit:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        cookingsuit_lbl.place(x=0,y=290)
        
        tray_lbl = Label(house_frame,text="tray :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        tray_lbl.place(x=10,y=330)
        
        cuban_lbl = Label(house_frame,text="cuban :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",18))
        cuban_lbl.place(x=10,y=370)
        
        glassbottle_lbl = Label(house_frame,text="Glass Bottel :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        glassbottle_lbl.place(x=10,y=410)
        
        table_lbl = Label(house_frame,text="Table Cloth :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        table_lbl.place(x=10,y=450)
        
        pan_lbl = Label(house_frame,text="pan :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        pan_lbl.place(x=10,y=490)
        
        frayingpan_lbl = Label(house_frame,text="Frying pan:",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        frayingpan_lbl.place(x=10,y=530)
        
        Airfrayer_lbl = Label(house_frame,text="Air Frayer :",bg="#0B4C5F",fg="#F1C40F",font=("lobster",20))
        Airfrayer_lbl.place(x=10,y=570)
        
        spoon_ent = Entry(house_frame,font=("Arial",15),textvariable=self.spoon)
        spoon_ent.place(x=150,y=60,width=150,height=20)
        
        fork_ent = Entry(house_frame,font=("Arial",15),textvariable=self.fork)
        fork_ent.place(x=150,y=100,width=150,height=20)
        
        knife_ent = Entry(house_frame,font=("Arial",15),textvariable=self.knifr)
        knife_ent.place(x=150,y=140,width=150,height=20)
        
        grater_ent = Entry(house_frame,font=("Arial",15),textvariable=self.grater)
        grater_ent.place(x=150,y=180,width=150,height=20)
        
        dishs_ent = Entry(house_frame,font=("Arial",15),textvariable=self.dishs)
        dishs_ent.place(x=150,y=220,width=150,height=20)
        
        ovenpan_ent = Entry(house_frame,font=("Arial",15),textvariable=self.ovenpan)
        ovenpan_ent.place(x=150,y=260,width=150,height=20)
        
        cookingsuit_ent = Entry(house_frame,font=("Arial",15),textvariable=self.cookingsuit)
        cookingsuit_ent.place(x=150,y=300,width=150,height=20)
        
        tray_ent = Entry(house_frame,font=("Arial",15),textvariable=self.tray)
        tray_ent.place(x=150,y=340,width=150,height=20)
        
        cuban_ent = Entry(house_frame,font=("Arial",15),textvariable=self.cuban)
        cuban_ent.place(x=150,y=380,width=150,height=20)
        
        glassbottel_ent = Entry(house_frame,font=("Arial",15),textvariable=self.glassbottel)
        glassbottel_ent.place(x=150,y=420,width=150,height=20)
        
        tablecloth_ent = Entry(house_frame,font=("Arial",15),textvariable=self.tablecloth)
        tablecloth_ent.place(x=150,y=460,width=150,height=20)
        
        pan_ent = Entry(house_frame,font=("Arial",15),textvariable=self.pan)
        pan_ent.place(x=150,y=500,width=150,height=20)
        
        frayongpan_ent = Entry(house_frame,font=("Arial",15),textvariable=self.frayingpan)
        frayongpan_ent.place(x=150,y=540,width=150,height=20)
        
        airfrayer_ent = Entry(house_frame,font=("Arial",15),textvariable=self.airfrayer)
        airfrayer_ent.place(x=150,y=580,width=150,height=20)
        self.welcome()
        self.renew()
        
       
    # ====================================== Functions ==================================================
    
     
    def welcome (self): 
        day = datetime.datetime.now().day 
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        hour = datetime.datetime.now().hour
        minuit = datetime.datetime.now().minute
        self.textarea.delete("1.0",END)
        self.textarea.insert(END,"\t Walcome to Supermarket")
        self.textarea.insert(END,f"\n \t\t{day}/{month}/{year}")
        self.textarea.insert(END,f"\n \t\t {hour}:{minuit}")
        self.textarea.insert(END,"\n ========================================")
        self.textarea.insert(END,f"\n \t Bill Number :{self.number.get()} ")
        self.textarea.insert(END,f"\n \t Name :{self.name.get()}")
        self.textarea.insert(END,f"\n \t Phone :{self.phone.get()} ")
        self.textarea.insert(END,"\n ========================================")
        self.textarea.insert(END,"\n Sells \t        Count \t        price \t ")
        self.textarea.insert(END,"\n ========================================")
            
    def total (self):
        if (self.name.get() == "" and self.phone.get()== "") :
            messagebox.showerror("WARNING","You must enter the Customer's name and Phone number")
        else:  
            self.q1= self.rice.get()*20
            self.q2 = self.pasta.get() * 18
            self.q3 = self.bread.get() * 10
            self.q4 = self.flour.get() * 25
            self.q5 = self.wheat.get() * 20
            self.q6 = self.corn.get() * 10
            self.q7 = self.salt.get() * 5
            self.q8 = self.bulgur.get() * 20
            self.q9 = self.oats.get() * 80
            self.q10 = self.suger.get() * 15
            self.q11 = self.paprika.get() * 100
            self.q12 = self.bean.get() * 80
            self.q13 = self.hummus.get() * 70
            self.q14 = self.lintil.get() * 60
            self.q15 = self.cowpea.get() * 80
            self.q16 = self.water.get() * 10
            self.q17 = self.milk.get() * 20
       
            self.totalf = (self.q1 + self.q2 + self.q3 + self.q4 + self.q5 + self.q6 + self.q7 + self.q8 + self.q9 
                            + self.q10 + self.q11+self.q12+self.q13+self.q14+self.q15+self.q16+self.q17)
            
            self.totalfood.set(str(self.totalf) +" E.G.P")
            
            
            self.qq1 = self.tv.get()*10000
            self.qq2 = self.mobile.get()*10000
            self.qq3 = self.laptop.get()*25000
            self.qq4 = self.computer.get()*30000
            self.qq5 = self.wash.get()*40000
            self.qq6 = self.refr.get()*30000
            self.qq7 = self.iron.get()*5000
            self.qq8 = self.filter.get()*1000
            self.qq9 = self.bioler.get()*1000
            self.qq10 = self.oven.get()*20000
            self.qq11 = self.mixer.get()*3000
            self.qq12 = self.vaccum.get()*5000
            self.qq13 = self.microwave.get()*2000
            self.qq14 = self.fan.get()*1000
            self.qq15 = self.wallfan.get()*700
            self.qq16 = self.keyboard.get()*500
            self.qq17 = self.mouse.get()*300
            
            self.totale = (self.qq1+ self.qq2 +self.qq3 +self.qq4 +self.qq5 +self.qq6 +self.qq7 +self.qq8 +self.qq9 +self.qq10+ self.qq11 +self.qq12 +self.qq13 + self.qq15 +self.qq16 +self.qq17 )
                            
            self.totalelec.set(str(self.totale) + " E.G.P")
            
            self.qqq1 = self.spoon.get()*20
            self.qqq2 = self.fork.get()*20
            self.qqq3 = self.grater.get()*20
            self.qqq4 = self.dishs.get()*50
            self.qqq5 = self.knifr.get()*30
            self.qqq6 = self.ovenpan.get()*100
            self.qqq7 = self.cookingsuit.get()*1000
            self.qqq8 = self.tray.get()*60
            self.qqq9 = self.cuban.get()*50
            self.qqq10 = self.glassbottel.get()*50
            self.qqq11 = self.tablecloth.get()*60
            self.qqq12 = self.pan.get()*100
            self.qqq13 = self.frayingpan.get()*400
            self.qqq14 = self.airfrayer.get()*1200
            
            self.totalk = self.qqq1+self.qqq2+self.qqq3+self.qqq4+self.qqq5+self.qqq6+self.qqq7+self.qqq8+self.qqq9+self.qqq10+self.qqq12+self.qqq13+self.qqq14               
            self.totalkitchen.set(str(self.totalk)+" E.G.P")
            self.alltotal = self.totale + self.totalf + self.totalk
            self.Billing()
            self.save()
             
    def clear(self): 
        self.rice.set(0)
        self.pasta.set(0)
        self.bread.set(0)
        self.flour.set(0)
        self.wheat.set(0)
        self.corn.set(0)
        self.salt.set(0)
        self.bulgur.set(0)
        self.oats.set(0)
        self.suger.set(0)
        self.paprika.set(0)
        self.bean.set(0)
        self.hummus.set(0)
        self.lintil.set(0)
        self.cowpea.set(0)
        self.milk.set(0)
        self.water.set(0)
        self.tv.set(0)
        self.mobile.set(0)
        self.laptop.set(0)
        self.computer.set(0)
        self.wash.set(0)
        self.refr.set(0)
        self.iron.set(0)
        self.filter.set(0)
        self.bioler.set(0)
        self.oven.set(0)
        self.mixer.set(0)
        self.vaccum.set(0)
        self.microwave.set(0)
        self.fan.set(0)
        self.wallfan.set(0)
        self.keyboard.set(0)
        self.mouse.set(0)
        self.spoon.set(0)
        self.fork.set(0)
        self.knifr.set(0)
        self.grater.set(0)
        self.dishs.set(0)
        self.ovenpan.set(0)
        self.cookingsuit.set(0)
        self.tray.set(0)
        self.cuban.set(0)
        self.glassbottel.set(0)
        self.tablecloth.set(0)
        self.pan.set(0)
        self.frayingpan.set(0)
        self.airfrayer.set(0)
        self.name.set("")
        self.phone.set("")
        self.renew()
        self.randomnumber()
        
    def save(self):
        if (self.totalelec.get()== "0 E.G.P" and self.totalfood.get() == "0 E.G.P"  and self.totalkitchen.get() == "0 E.G.P"):
            self.warning()
            return
        op = messagebox.askyesno("Save","Do You Want to save this Bill ?") 
        if (op != 0  and self.name.get() !="" and self.phone.get() !="") or (self.totalelec.get()!= "0 E.G.P" and self.totalfood.get() != "0 E.G.P"  and self.totalkitchen.get() != "0 E.G.P" ):
            self.bb = self.textarea.get("1.0",END)
            f1 = open("D:\\supermarket\\"+str(self.number.get())+".txt","w")
            f1.write(self.bb)
            f1.close()
        else:
            return
            
    def search (self):
        try:
             if self.number.get():
                f2=open("D:\\supermarket\\"+str(self.number.get())+".txt")
                messagebox.showinfo("Success","Opened")
                self.textarea.delete("1.0",END)
                self.textarea.insert(END,f2.read())
                f2.close()
        except:
            messagebox.showwarning("WARNING","THE BILL NUMBER IS WRONG \n TRY AGAIN")
            
    def Billing (self):
            self.welcome()
            if self.rice.get() != 0:
                self.textarea.insert(END,f"\n Rice \t\t{self.rice.get()}\t\t{self.q1}")
            if self.pasta.get() !=0:
                self.textarea.insert(END,f"\n Pasta \t\t{self.pasta.get()}\t\t {self.q2}")
            if self.bread.get() !=0:
                self.textarea.insert(END,f"\n Bread \t\t{self.bread.get()}\t\t {self.q3}")
            if self.flour.get() !=0:
                self.textarea.insert(END,f"\n Flour\t\t{self.flour.get()}\t\t {self.q4}")
            if self.wheat.get() !=0:
                self.textarea.insert(END,f"\n Wheat \t\t{self.wheat.get()}\t\t {self.q5}")
            if self.corn.get() !=0:
                self.textarea.insert(END,f"\n Corn \t\t{self.corn.get()}\t\t {self.q6}")
            if self.salt.get() !=0:
                self.textarea.insert(END,f"\n Salt \t\t{self.salt.get()}\t\t {self.q7}")
            if self.bulgur.get() !=0:
                self.textarea.insert(END,f"\n Bulger \t\t{self.bulgur.get()}\t\t {self.q8}")
            if self.oats.get() !=0:
                self.textarea.insert(END,f"\n Oats \t\t{self.oats.get()}\t\t{self.q9}")
            if self.suger.get() !=0:
                self.textarea.insert(END,f"\n Suger \t\t{self.suger.get()}\t\t {self.q10}")
            if self.paprika.get() !=0:
                self.textarea.insert(END,f"\n Paprika \t\t{self.paprika.get()}\t\t {self.q11}")
            if self.bean.get() !=0:
                self.textarea.insert(END,f"\n Bean \t\t{self.bean.get()}\t\t{self.q12}")
            if self.hummus.get() !=0:
                self.textarea.insert(END,f"\n Hummus \t\t{self.hummus.get()}\t\t {self.q13}")
            if self.lintil.get() !=0:
                self.textarea.insert(END,f"\n Lintil \t\t{self.lintil.get()}\t\t {self.q14}")
            if self.cowpea.get() !=0:
                self.textarea.insert(END,f"\n Cowpea \t\t{self.cowpea.get()}\t\t {self.q15}")
            if self.water.get() !=0:
                self.textarea.insert(END,f"\n Water \t\t{self.water.get()}\t\t {self.q16}")
            if self.milk.get() !=0:
                self.textarea.insert(END,f"\n Milk \t\t{self.milk.get()}\t\t {self.q17}")
                
                # ---------------------- elec ------------------------------- 
            if self.tv.get() !=0:
                self.textarea.insert(END,f"\n Tv \t\t{self.tv.get()}\t\t {self.qq1}")
            if self.mobile.get() !=0:
                self.textarea.insert(END,f"\n Mobile \t\t{self.mobile.get()}\t\t{self.qq2}")
            if self.laptop.get() !=0:
                self.textarea.insert(END,f"\n Laptop \t\t{self.laptop.get()}\t\t {self.qq3}")
            if self.computer.get() !=0:
                self.textarea.insert(END,f"\nComputer\t\t{self.computer.get()}\t\t {self.qq4}") 
            if self.wash.get() !=0:
                self.textarea.insert(END,f"\n Washing Machine \t\t{self.wash.get()}\t\t {self.qq5}")
            if self.refr.get() !=0:
                self.textarea.insert(END,f"\n Refrigerator \t\t{self.refr.get()}\t\t {self.qq6}")
            if self.iron.get() !=0:
                self.textarea.insert(END,f"\n Iron \t\t{self.iron.get()}\t\t {self.qq7}")
            if self.filter.get() !=0:
                self.textarea.insert(END,f"\n Filter \t\t{self.filter.get()}\t\t{self.qq8}")
            if self.bioler.get() !=0:
                self.textarea.insert(END,f"\n Boiler \t\t{self.bioler.get()}\t\t  {self.qq9}")
            if self.oven.get() !=0:
                self.textarea.insert(END,f"\n Oven \t\t{self.oven.get()}\t\t{self.qq10}")
            if self.mixer.get() !=0:
                self.textarea.insert(END,f"\n Mixer \t\t{self.mixer.get()}\t\t  {self.qq11}")
            if self.vaccum.get() !=0:
                self.textarea.insert(END,f"\n Vaccum \t\t{self.vaccum.get()}\t\t {self.qq12}")
            if self.microwave.get() !=0:
                self.textarea.insert(END,f"\n Microwave \t\t{self.microwave.get()}\t\t{self.qq13}")
            if self.fan.get() !=0:
                self.textarea.insert(END,f"\n Fan \t\t{self.fan.get()}\t\t {self.qq14}")
            if self.wallfan.get() !=0:
                self.textarea.insert(END,f"\n Wall Fan\t\t{self.wallfan.get()}\t\t {self.qq15}")
            if self.keyboard.get() !=0:
                self.textarea.insert(END,f"\n Keyboard \t\t{self.keyboard.get()}\t\t{self.qq16}")
            if self.mouse.get() !=0:
                self.textarea.insert(END,f"\n Mouse \t\t{self.mouse.get()}\t\t{self.qq17}")
            # ----------------------------- kitchen ----------------------------------
            if self.spoon.get() !=0:
                self.textarea.insert(END,f"\n Spoon \t\t{self.spoon.get()}\t\t {self.qqq1}")
            if self.fork.get() !=0:
                self.textarea.insert(END,f"\n Fork \t\t{self.fork.get()}\t\t{self.qqq2}")
            if self.knifr.get() !=0:
                self.textarea.insert(END,f"\n Knife \t\t{self.knifr.get()}\t\t {self.qqq5}")
            if self.grater.get() !=0:
                self.textarea.insert(END,f"\n Grater \t\t{self.grater.get()}\t\t{self.qqq3}")
            if self.dishs.get() !=0:
                self.textarea.insert(END,f"\n Dish \t\t{self.dishs.get()}\t\t{self.qqq4}")
            if self.ovenpan.get() !=0:
                self.textarea.insert(END,f"\n Oven pan \t\t{self.ovenpan.get()}\t\t {self.qqq6}")
            if self.cookingsuit.get() !=0:
                self.textarea.insert(END,f"\n Cooking Suit \t\t{self.cookingsuit.get()}\t\t{self.qqq7}")
            if self.tray.get() !=0:
                self.textarea.insert(END,f"\n tray \t\t{self.tray.get()}\t\t{self.qqq8}")
            if self.cuban.get() !=0:
                self.textarea.insert(END,f"\n Cuban \t\t{self.cuban.get()}\t\t {self.qqq9}")
            if self.glassbottel.get() !=0:
                self.textarea.insert(END,f"\n Glass Bottle \t\t{self.glassbottel.get()}\t\t {self.qqq10}")
            if self.tablecloth.get() !=0:
                self.textarea.insert(END,f"\n Table Cloth \t\t{self.tablecloth.get()}\t\t {self.qqq11}")
            if self.pan.get() !=0:
                self.textarea.insert(END,f"\n Pan \t\t{self.pan.get()}\t\t {self.qqq12}")
            if self.frayingpan.get() !=0:
                self.textarea.insert(END,f"\n Fraying Pan \t\t{self.frayingpan.get()}\t\t {self.qqq13}")
            if self.airfrayer.get() !=0:
                self.textarea.insert(END,f"\n Air Frayer \t\t{self.airfrayer.get()}\t\t {self.qqq14}")   
            self.textarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------------------------------------")
            self.textarea.insert(END,f"\nTotal:  \t        {self.alltotal}              E.G.P ")
            self.textarea.insert(END,"\n\n\n\n\n\n\n\n\n-----------------------------------------")   
                 
    def randomnumber(self):
        x= random.randint(1,99999)
        self.number.set(str(x))
           
    def renew(self): 
        self.totalelec.set("0 E.G.P")
        self.totalfood.set("0 E.G.P")
        self.totalkitchen.set("0 E.G.P")
        
    def warning(self):
        if self.totalelec.get()== "0 E.G.P" and self.totalfood.get() == "0 E.G.P"  and self.totalkitchen.get() == "0 E.G.P" : 
            messagebox.showerror("WARNING","THERE IS NOT PRODUCT ADDED TO THE BILL")  
                      
root = Tk()
ob = Super(root)
root.mainloop()