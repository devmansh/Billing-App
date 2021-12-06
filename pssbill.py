from tkinter import *
import math,random,os, datetime
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("PSS")

        
        bg_color = "#003366"
        fg_color = "white"
        lbl_color = '#00ffff'
        lbl_color2 = "white"




        # This function for title frame
        title = Label(self.root, text="PRATAP & SONS", bd=12, relief=GROOVE, fg="BLUE", bg=bg_color,font=("algerian", 30), pady=2).pack(fill=X)


        #====================Variables===================


        #=============Lowers varibales===============
        self.lowercc=IntVar()
        self.lowerfc=IntVar()
        self.lowerbc=IntVar()
        self.lowerpent=IntVar()
        self.lowerlwcc=IntVar()
        self.lowerlwlp=IntVar()
        self.lowerlwfc=IntVar()


        #=============TShirt varibales===============
        self.tshirtrn=IntVar()
        self.tshirtvn=IntVar()
        self.tshirtrns=IntVar()
        self.tshirtvns=IntVar()
        self.tshirtsf=IntVar()
        self.tshirtsh=IntVar()
        self.runkit=IntVar()

        #=============Shoes varibales===============
        self.pss1=IntVar()
        self.pss2=IntVar()
        self.pss3=IntVar()
        self.pss4=IntVar()
        self.pss5=IntVar()
        self.pss6=IntVar()
        self.pss7=IntVar()


        #==================== Total price and tax variables===============
        self.lower_total=StringVar()
        self.tshirt_total=StringVar()
        self.shoes_total=StringVar()

        self.lower_tax=StringVar()
        self.tshirt_tax=StringVar()
        self.shoes_tax=StringVar()

        #=====================customer variable==========================
        self.cus_name=StringVar()
        self.cus_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        # =============================================================This function for Customers Frame==================================================================
        F1 = LabelFrame(self.root, bd=10, text="Customer Information", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, relief=GROOVE)
        F1.place(x=0, y=80, relwidth=1)

        # This function for customer name
        customername_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        customername_en = Entry(F1, bd=7,width=12, textvariable=self.cus_name, relief=SUNKEN,font=("times new roman", 18, "bold")).grid(row=0, column=1, pady=5, padx=10)

        # This function is for customer mobile no.
        customercontact_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        customercontact_en = Entry(F1, bd=7,width=12, textvariable=self.cus_phone, relief=SUNKEN,font=("times new roman", 18, "bold")).grid(row=0, column=3, pady=5, padx=10)
        
        # This fucntion for Invoice Number
        customerinvoice_lbl = Label(F1, text="Invoice No.", bg=bg_color, fg=fg_color, font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        customerinvoice_en = Entry(F1, bd=7,width=12, textvariable=self.search_bill, relief=SUNKEN, font=("times new roman", 18, "bold")).grid(row=0, column=5, pady=5, padx=10)

        # This function for Invoice Search Button
        invoice_btn = Button(F1, text="Search", command=self.find_bill, width=8, bd=7, relief=RAISED, font=("times new roman", 15, "bold"), bg=bg_color,fg=fg_color).grid(row=0, column=6, padx=20, pady=10)
        


        #========================================This function for Sports Lower Frame============================================================================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text='PS-AirFlex Lower',  bg=bg_color, fg="gold", font=("times new roman", 15, "bold"))
        F2.place(x=0, y=180, width=325, height=380)


        # This function for Lower Type Cross Chain
        lowercc_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-CC").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        lowercc_en = Entry(F2, bd=5, relief=SUNKEN, textvariable=self.lowercc, width=6, font=("times new roman", 15, "bold")).grid(row=0, column=1, pady=5, padx=5)
        
        # This function for lower type front chain
        lowerfc_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-FC").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        lowerfc_en = Entry(F2, bd=5, relief=SUNKEN, width=6, textvariable=self.lowerfc, font=("times new roman", 15, "bold")).grid(row=1, column=1, pady=5, padx=5)
    
        # This function for lower type back chain
        lowerbc_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-BC").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        lowerbc_en = Entry(F2, bd=5, relief=SUNKEN, width=6, textvariable=self.lowerbc, font=("times new roman", 15, "bold")).grid(row=2, column=1, pady=5, padx=5)
        
        # This function for lower type pent
        lowerpent_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-Pent").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        lowerpent_en = Entry(F2, bd=5, relief=SUNKEN, width=6, textvariable=self.lowerpent, font=("times new roman", 15, "bold")).grid(row=3, column=1, pady=5, padx=5)
        
        # This function for lower type light weight cross chain
        lowerlwcc_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-LWCC").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        lowerlwcc_en = Entry(F2, bd=5, relief=SUNKEN, width=6, textvariable=self.lowerlwcc, font=("times new roman", 15, "bold")).grid(row=4, column=1, pady=5, padx=5)

        # This function for lower type light weight l Pocket
        lowerlwlp_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-LWLP").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        lowerlwlp_en = Entry(F2, bd=5, relief=SUNKEN, width=6, textvariable=self.lowerlwlp, font=("times new roman", 15, "bold")).grid(row=5, column=1, pady=5, padx=5)

        # This function for lower type light weight front chain
        lowerlwfc_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-Lower-LWFC").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        lowerlwfc_en = Entry(F2, bd=5, relief=SUNKEN, width=6, textvariable=self.lowerlwfc, font=("times new roman", 15, "bold")).grid(row=6, column=1, pady=5, padx=5)


        


        #========================================This function for Sports T-Shirt Frame============================================================================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text='PS-AirFlex T-Shirt',  bg=bg_color, fg="gold", font=("times new roman", 15, "bold"))
        F3.place(x=325, y=180, width=325, height=380)


        # This function for tshirt round neck
        tshirtrn_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-TShirt-RN").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tshirtrn_en = Entry(F3, bd=5, relief=SUNKEN, textvariable=self.tshirtrn, width=6, font=("times new roman", 15, "bold")).grid(row=0, column=1, pady=5, padx=5)
        
        # This function for tshirt type v-neck
        tshirtvn_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-TShirt-VN").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tshirtvn_en = Entry(F3, bd=5, relief=SUNKEN, textvariable=self.tshirtvn, width=6, font=("times new roman", 15, "bold")).grid(row=1, column=1, pady=5, padx=5)
    
        # This function for tshirt round neck stretch
        tshirtrns_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-TShirt-RNS").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        tshirtrns_en = Entry(F3, bd=5, relief=SUNKEN, textvariable=self.tshirtrns, width=6, font=("times new roman", 15, "bold")).grid(row=2, column=1, pady=5, padx=5)
        
        # This function for tshirt type V-neck stretch
        tshirtvns_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-TShirt-VNS").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        tshirtvns_en = Entry(F3, bd=5, relief=SUNKEN, width=6, textvariable=self.tshirtvns, font=("times new roman", 15, "bold")).grid(row=3, column=1, pady=5, padx=5)
        
        # This function for tshirt type stretch full sleeve
        tshirtsf_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-TShirt-SF").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tshirtsf_en = Entry(F3, bd=5, relief=SUNKEN, width=6, textvariable=self.tshirtsf, font=("times new roman", 15, "bold")).grid(row=4, column=1, pady=5, padx=5)

        # This function for tshirt type stretch half sleeves
        tshirtsh_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-TShirt-SH").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tshirtsh_en = Entry(F3, bd=5, relief=SUNKEN, width=6, textvariable=self.tshirtsh, font=("times new roman", 15, "bold")).grid(row=5, column=1, pady=5, padx=5)

        # This function for running kit
        runkit_lbl = Label(F3, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-RunningKit").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        runkit_en = Entry(F3, bd=5, relief=SUNKEN, width=6, textvariable=self.runkit, font=("times new roman", 15, "bold")).grid(row=6, column=1, pady=5, padx=5)





        #========================================This function for Sports Shoes Frame============================================================================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text='PS-AirFlex Shoes',  bg=bg_color, fg="gold", font=("times new roman", 15, "bold"))
        F4.place(x=650, y=180, width=275, height=380)


        # This function for Lower Type Cross Chain
        pss1_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS1").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        pss1_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss1, font=("times new roman", 15, "bold")).grid(row=0, column=1, pady=5, padx=5)
        
        # This function for lower type front chain
        pss2_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS2").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        pss2_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss2, font=("times new roman", 15, "bold")).grid(row=1, column=1, pady=5, padx=5)
    
        # This function for lower type back chain
        pss3_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS3").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        pss3_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss3, font=("times new roman", 15, "bold")).grid(row=2, column=1, pady=5, padx=5)
        
        # This function for lower type pent
        pss4_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS4").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        pss4_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss4, font=("times new roman", 15, "bold")).grid(row=3, column=1, pady=5, padx=5)
        
        # This function for lower type light weight cross chain
        pss5_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS5").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        pss5_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss5, font=("times new roman", 15, "bold")).grid(row=4, column=1, pady=5, padx=5)

        # This function for lower type light weight l Pocket
        pss6_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS6").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        pss6_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss6, font=("times new roman", 15, "bold")).grid(row=5, column=1, pady=5, padx=5)

        # This function for lower type light weight front chain
        pss7_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="AirFlex-PS7").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        pss7_en = Entry(F4, bd=5, relief=SUNKEN, width=6, textvariable=self.pss7, font=("times new roman", 15, "bold")).grid(row=6, column=1, pady=5, padx=5)




        #=======================This function is for receipt area==================================================
        F5 = Label(self.root, bd=10, relief=GROOVE)
        F5.place(x=925, y=180, width=355, height=380)

        #this function if for receipt title 
        receipt_title = Label(F5, text="Invoice Area", font=("Arial 15 bold"), bd=7, relief=RAISED).pack(fill=X)

        #This function for Scroll bar Button frames
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txt = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)
        

        #========================================== This function for Bottom Buttons Frame=================================================
        F6 = LabelFrame(self.root, text='Total Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",font=("times new roman", 15, "bold"))
        F6.place(x=0, y=560, relwidth=1, height=140)


        #================
        #this function is for lower total button
        lower_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color2, bg=bg_color, text="Total of Lower").grid(row=0, column=0, padx=20, pady=1, sticky="w")
        lower_txt = Entry(F6, width=15, textvariable=self.lower_total, bd=7, relief=SUNKEN, font="Arial 10 bold").grid(row=0, column=1, padx=10, pady=1)

        #this function is for tshirt total button
        tshirt_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color2, bg=bg_color, text="Total of TShirt").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        tshirt_txt = Entry(F6, width=15, bd=7, textvariable=self.tshirt_total, relief=SUNKEN, font="Arial 10 bold").grid(row=1, column=1, padx=10, pady=1)

        #this function is for shoes total button
        shoes_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color2, bg=bg_color, text="Total of Shoes").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        shoes_txt = Entry(F6, width=15, bd=7, textvariable=self.shoes_total, relief=SUNKEN, font="Arial 10 bold").grid(row=2, column=1, padx=10, pady=1)

        
        #================
        #this function is for lower tax button
        lowertax_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color2, bg=bg_color, text="Tax on Lower").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        lowertax_txt = Entry(F6, width=15, bd=7, textvariable=self.lower_tax, relief=SUNKEN, font="Arial 10 bold").grid(row=0, column=3, padx=10, pady=1)

        #this function is for tshirt tax button
        tshirttax_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color2, bg=bg_color, text="Tax on Tshirt").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        tshirttax_txt = Entry(F6, width=15, textvariable=self.tshirt_tax, bd=7, relief=SUNKEN, font="Arial 10 bold").grid(row=1, column=3, padx=10, pady=1)

        #this function is for shoes tax button
        shoestax_lbl = Label(F6, font=("times new roman", 15, "bold"), fg=lbl_color2, bg=bg_color, text="Tax on Shoes").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        shoestax_txt = Entry(F6, width=15, textvariable=self.shoes_tax, bd=7, relief=SUNKEN, font="Arial 10 bold").grid(row=2, column=3, padx=10, pady=1)


        # =========================================== This function for total Button frames==============================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=650, width=600,height=100)
        

        #================Buttons
        total_btn=Button(btn_f,command=self.total, text="Total",bg="cadetblue", fg=fg_color, pady=15, width=12,font="Arial 13 bold", bd=5).grid(row=0,column=0,padx=5,pady=8)
        generate_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue", fg=fg_color, pady=15, width=12,font="Arial 13 bold", bd=5).grid(row=0,column=1,padx=5,pady=8)
        clear_btn=Button(btn_f,command=self.clear_data,text="Clear",bg="cadetblue", fg=fg_color, pady=15, width=12,font="Arial 13 bold", bd=5).grid(row=0,column=2,padx=5,pady=8)
        exit_btn=Button(btn_f,command=self.Exit_App, text="Exit",bg="cadetblue", fg=fg_color, pady=15, width=12,font="Arial 13 bold", bd=5).grid(row=0,column=3,padx=5,pady=8)
        self.welcome_bill()


#============================================total sections===========================
    def total(self):

        #for lowers
        self.lower_lowercc=self.lowercc.get()*300
        self.lower_lowerfc=self.lowerfc.get()*300
        self.lower_lowerbc=self.lowerbc.get()*300
        self.lower_lowerpent=self.lowerpent.get()*300
        self.lower_lowerlwcc=self.lowerlwcc.get()*350
        self.lower_lowerlwlp=self.lowerlwlp.get()*350
        self.lower_lowerlwfc=self.lowerlwfc.get()*350

        self.lower_total_price=float(
                                self.lower_lowercc+
                                self.lower_lowerfc+
                                self.lower_lowerbc+
                                self.lower_lowerpent+
                                self.lower_lowerlwcc+
                                self.lower_lowerlwlp+
                                self.lower_lowerlwfc
                                )
        self.lower_total.set("Rs. "+str(self.lower_total_price))
        self.l_tax=round((self.lower_total_price*0.05),2)
        self.lower_tax.set("Rs. "+str(self.l_tax))

        #for tshirts
        self.t_tshirtrn=self.tshirtrn.get()*200
        self.t_tshirtvn=self.tshirtvn.get()*200
        self.t_tshirtrns=self.tshirtrns.get()*200
        self.t_tshirtvns=self.tshirtvns.get()*200
        self.t_tshirtsf=self.tshirtsf.get()*250
        self.t_tshirtsh=self.tshirtsh.get()*250
        self.t_runkit=self.runkit.get()*150
        
        self.tshirt_total_price=float(
                                self.t_tshirtrn+
                                self.t_tshirtvn+
                                self.t_tshirtrns+
                                self.t_tshirtvns+
                                self.t_tshirtsf+
                                self.t_tshirtsh+
                                self.t_runkit
                                )
        self.tshirt_total.set("Rs. "+str(self.tshirt_total_price))
        self.t_tax=round((self.tshirt_total_price*0.05),2)
        self.tshirt_tax.set("Rs. "+str(self.t_tax))

        #for tshirts
        self.s_pss1=self.pss1.get()*400
        self.s_pss2=self.pss2.get()*400
        self.s_pss3=self.pss3.get()*400
        self.s_pss4=self.pss4.get()*400
        self.s_pss5=self.pss5.get()*450
        self.s_pss6=self.pss6.get()*450
        self.s_pss7=self.pss7.get()*450

        self.shoes_total_price=float(
                                self.s_pss1+
                                self.s_pss2+
                                self.s_pss3+
                                self.s_pss4+
                                self.s_pss5+
                                self.s_pss6+
                                self.s_pss7
                                )
        self.shoes_total.set("Rs. "+str(self.shoes_total_price))
        self.s_tax=round((self.shoes_total_price*0.05),2)
        self.shoes_tax.set("Rs. "+str(self.s_tax))

        self.total_bill=float(  self.lower_total_price+
                                self.tshirt_total_price+
                                self.shoes_total_price+
                                self.l_tax+
                                self.t_tax+
                                self.s_tax
                            )



    #=============================bill area==========================
    def welcome_bill (self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome to Pratap&Sons Sports")
        self.txt.insert(END,"\n\t    Phone no. 7983628969")
        self.txt.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txt.insert(END,f"\nCustomer Name : {self.cus_name.get()}")
        self.txt.insert(END,f"\nPhone Number : {self.cus_phone.get()}")
        self.txt.insert(END,f"\nDate & Time : {datetime.datetime.now()}")
        self.txt.insert(END,f"\n=========================================")
        self.txt.insert(END,f"\n Product\t\tU/P\tQTY\tPrice")
        self.txt.insert(END,f"\n=========================================")

    def bill_area(self):
        if self.cus_name.get()=="" or self.cus_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.lower_total.get()=="Rs. 0.0" and self.tshirt_total.get()=="Rs. 0.0" and self.shoes_total.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Selected")
        else:
            self.welcome_bill()
            #=====lowers=====
            if self.lowercc.get()!=0:
                self.txt.insert(END,f"\n Lower CC\t\t300\t{self.lowercc.get()}\t{self.lower_lowercc}")
            if self.lowerfc.get()!=0:
                self.txt.insert(END,f"\n Lower FC\t\t300\t{self.lowerfc.get()}\t{self.lower_lowerfc}")
            if self.lowerbc.get()!=0:
                self.txt.insert(END,f"\n Lower BC\t\t300\t{self.lowerbc.get()}\t{self.lower_lowerbc}")
            if self.lowerpent.get()!=0:
                self.txt.insert(END,f"\n Lower Pent\t\t300\t{self.lowerpent.get()}\t{self.lower_lowerpent}")
            if self.lowerlwcc.get()!=0:
                self.txt.insert(END,f"\n Lower LWCC\t\t350\t{self.lowerlwcc.get()}\t{self.lower_lowerlwcc}")
            if self.lowerlwlp.get()!=0:
                self.txt.insert(END,f"\n Lower LWLP\t\t350\t{self.lowerlwlp.get()}\t{self.lower_lowerlwlp}")
            if self.lowerlwfc.get()!=0:
                self.txt.insert(END,f"\n Lower LWFC\t\t350\t{self.lowerlwfc.get()}\t{self.lower_lowerlwfc}")
            #=======tshirts==========
            if self.tshirtrn.get()!=0:
                self.txt.insert(END,f"\n TShirt RN\t\t200\t{self.tshirtrn.get()}\t{self.t_tshirtrn}")
            if self.tshirtvn.get()!=0:
                self.txt.insert(END,f"\n TShirt VN\t\t200\t{self.tshirtrn.get()}\t{self.t_tshirtvn}")
            if self.tshirtrns.get()!=0:
                self.txt.insert(END,f"\n TShirt RNS\t\t200\t{self.tshirtrns.get()}\t{self.t_tshirtrns}")
            if self.tshirtvns.get()!=0:
                self.txt.insert(END,f"\n TShirt VNS\t\t200\t{self.tshirtvns.get()}\t{self.t_tshirtvns}")
            if self.tshirtsf.get()!=0:
                self.txt.insert(END,f"\n TShirt SF\t\t250\t{self.tshirtsf.get()}\t{self.t_tshirtsf}")
            if self.tshirtsh.get()!=0:
                self.txt.insert(END,f"\n TShirt SH\t\t250\t{self.tshirtsh.get()}\t{self.t_tshirtsh}")
            if self.runkit.get()!=0:
                self.txt.insert(END,f"\n RunningKit\t\t150\t{self.runkit.get()}\t{self.t_runkit}")
            #==========shoes==========
            if self.pss1.get()!=0:
                self.txt.insert(END,f"\n Airflex S1\t\t400\t{self.pss1.get()}\t{self.s_pss1}")
            if self.pss2.get()!=0:
                self.txt.insert(END,f"\n Airflex S2\t\t400\t{self.pss2.get()}\t{self.s_pss2}")
            if self.pss3.get()!=0:
                self.txt.insert(END,f"\n Airflex S3\t\t400\t{self.pss3.get()}\t{self.s_pss3}")
            if self.pss4.get()!=0:
                self.txt.insert(END,f"\n Airflex S4\t\t400\t{self.pss4.get()}\t{self.s_pss4}")
            if self.pss5.get()!=0:
                self.txt.insert(END,f"\n Airflex S5\t\t450\t{self.pss5.get()}\t{self.s_pss5}")
            if self.pss6.get()!=0:
                self.txt.insert(END,f"\n Airflex S6\t\t450\t{self.pss6.get()}\t{self.s_pss6}")
            if self.pss7.get()!=0:
                self.txt.insert(END,f"\n Airflex S7\t\t450\t{self.pss7.get()}\t{self.s_pss7}")
            
            #=====tax in billing area=====
            self.txt.insert(END,f"\n-----------------------------------------")
            if self.lower_tax.get()!="Rs. 0.0":
                self.txt.insert(END,f"\nLowers_5%GST:\t\t{self.lower_tax.get()}")
            if self.tshirt_tax.get()!="Rs. 0.0":
                self.txt.insert(END,f"\nTShirts_5%GST:\t\t{self.tshirt_tax.get()}")
            if self.shoes_tax.get()!="Rs. 0.0":
                self.txt.insert(END,f"\nShoes_5%GST:\t\t{self.shoes_tax.get()}")
            self.txt.insert(END,f"\n-----------------------------------------")
            self.txt.insert(END,f"\nTotal bill: \t\tRs. {self.total_bill}")
            self.txt.insert(END,f"\n-----------------------------------------")
            self.txt.insert(END,f"\n     Thank You for Shopping with us")
            self.txt.insert(END,f"\n\t      Have Goood Day!")
            self.save_bill()

    
    
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txt.get('1.0',END)
            f1=open("invoices/"+str(self.bill_no.get())+".rtf","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved successfully")
        else:
            return
            
    #=====find bill
    def find_bill(self):
        present="no"
        for i in os.listdir("invoices/"): 
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"invoices/{i}","r")
                self.txt.delete('1.0', END)
                for d in f1:
                    self.txt.insert(END, d)
                f1.close()
                present="yes"
        if present == "no":
            messagebox.showerror("Error","Invalid Invoice No.")

    #====clear data
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear Data?")
        if op>0:
            #=================Lower variable
            self.lowercc.set(0)
            self.lowerfc.set(0)
            self.lowerbc.set(0)
            self.lowerpent.set(0)
            self.lowerlwcc.set(0)
            self.lowerlwlp.set(0)
            self.lowerlwfc.set(0)


            #=============TShirt varibales===============
            self.tshirtrn.set(0)
            self.tshirtvn.set(0)
            self.tshirtrns.set(0)
            self.tshirtvns.set(0)
            self.tshirtsf.set(0)
            self.tshirtsh.set(0)
            self.runkit.set(0)

            #=============Shoes varibales===============
            self.pss1.set(0)
            self.pss2.set(0)
            self.pss3.set(0)
            self.pss4.set(0)
            self.pss5.set(0)
            self.pss6.set(0)
            self.pss7.set(0)


            #==================== Total price and tax variables===============
            self.lower_total.set("")
            self.tshirt_total.set("")
            self.shoes_total.set("")

            self.lower_tax.set("")
            self.tshirt_tax.set("")
            self.shoes_tax.set("")

            #=====================customer variable==========================
            self.cus_name.set("")
            self.cus_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_App(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

    
    
        
        


root=Tk()
obj = Bill_App(root)
root.mainloop()