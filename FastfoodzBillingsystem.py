from tkinter import*
import random
import time;

#Defining frame and name of the project
root = Tk()
root.geometry('1600x800+0+0')
root.title("FastFoodz Billing System")

#Input for calculator
text_Input = StringVar()
operator  =""

#Top frame
Tops = Frame(root, width = 1600, height = 50, relief=SUNKEN)
Tops.pack(side=TOP)

#Left frame
f1 = Frame(root, width = 800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

#Right frame
f2 = Frame(root, width = 300, height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#date and time fx
localtime =time.asctime(time.localtime(time.time()))

#system info
lblInfo = Label(Tops, font = ("arial",50,"bold"), text = "FastFoodz Billing System",fg ="steel blue",bd = 10, anchor = "w")
lblInfo.grid(row=0,column=0)
lblDateTime = Label(Tops, font = ("arial",20,"bold"), text =localtime,fg ="steel blue",bd = 10, anchor = "w")
lblDateTime.grid(row=1,column=0)

#calculator
#function to take in values
def btnClick(numbers):
    global operator
    operator = operator+ str(numbers)
    text_Input.set(operator)
    
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
    
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
def Ref():
    x= random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)
    
    #Cost Of Fries
    CoF = float(Fries.get())
    #Cost Of Drinks
    CoD = float(Drinks.get())
    #Cost Of Filet
    CoKebab= float(Kebab.get())
    #Cost Of Burger
    CoBurger = float(Burger.get())
    #Cost Of Chicken burger
    CoChicken = float(Chicken.get())
    #Cost Of Cheese burger
    CoSmokies = float(Smokies.get())
     
    #Cost of single quantity item
    CostofFries = CoF * 150
    CostofDrinks = CoD * 100
    CostofKebab = CoKebab * 90
    CostofBurger = CoBurger * 120
    CostofChickenFried = CoChicken * 450
    CostofSmokies = CoSmokies * 75
     
    #Cost of meal into 2dp
    CostofMeal = "Kes", str('%.2f ' % (CostofFries +  CostofDrinks + CostofKebab +  CostofBurger
                                        + CostofChickenFried + CostofSmokies ))
    #Tax
    payTax = ((CostofFries +  CostofDrinks +  CostofKebab +  CostofBurger
                                        + CostofChickenFried + CostofSmokies ) * 0.002)
    #Total Cost
    TotalCost = (CostofFries +  CostofDrinks +  CostofKebab +  CostofBurger
                                        + CostofChickenFried +  CostofSmokies )
    #Service Charge
    Ser_Charge = ((CostofFries +  CostofDrinks +  CostofKebab +  CostofBurger
                                        + CostofChickenFried + CostofSmokies )/50)
    Service = "Kes", str('%.2f' % Ser_Charge)
     
    #Overall Cost
    OverAllCost =  "Kes", str('%.2f' % (TotalCost))
     
    #paid Tax
    paidTax = "Kes", str('%.2f' % payTax)
     
     
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(paidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    

def qExit():
    root.destroy()
    
def Reset():
        rand.set("")
        Fries.set("")
        Burger.set("")
        Kebab.set("")
        Chicken.set("")
        Smokies.set("")
        Drinks.set("")
        Cost.set("")
        Tax.set("")
        Service_Charge.set("")
        SubTotal.set("")
        Total.set("")
    
#Calculator screen
txtDisplay = Entry(f2, font = ("arial",20,"bold"),textvariable = text_Input,bd=30,insertwidth=4,bg="#052205",fg="white", justify ="right")
txtDisplay.grid(columnspan = 4)

#Calculator Button
btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="7",bg="#c0c0c0",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="8",bg="#c0c0c0",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="9",bg="#c0c0c0",command=lambda:btnClick(9)).grid(row=2,column=2)
Addition = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="+",bg="#fff",command=lambda:btnClick("+")).grid(row=2,column=3)

btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="4",bg="#c0c0c0",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="5",bg="#c0c0c0",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="6",bg="#c0c0c0",command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="-",bg="#fff",command=lambda:btnClick("-")).grid(row=3,column=3)

btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="1",bg="#c0c0c0",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="2",bg="#c0c0c0",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3= Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="3",bg="#c0c0c0",command=lambda:btnClick(3)).grid(row=4,column=2)
Multiply = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="*",bg="#fff",command=lambda:btnClick("*")).grid(row=4,column=3)

btn0 = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="0",bg="#c0c0c0",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear= Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="C",bg="#f51010", command=btnClearDisplay).grid(row=5,column=1)
btnEquals = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="=",bg="#029402",command=btnEqualsInput).grid(row=5,column=2)
Division = Button(f2,padx=16,pady=16,bd=8,fg="black", font = ("arial",20,"bold"),text="/",bg="#fff",command=lambda:btnClick("/")).grid(row=5,column=3)

rand = StringVar()
Fries =  StringVar()
Burger = StringVar()
Kebab = StringVar()
Chicken = StringVar()
Smokies = StringVar()
Drinks = StringVar()
Cost = StringVar()
Tax = StringVar()
Service_Charge = StringVar()
SubTotal = StringVar()
Total = StringVar()

#Resto info 1
lblReference = Label(f1, font = ("arial",16,"bold"), text = "Reference No.", bd=16, anchor = "w")
lblReference.grid(row=0,column=0)
txtReference = Entry(f1, font = ("arial",16,"bold"), textvariable = rand, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtReference.grid(row=0,column=1)

lblFries = Label(f1, font = ("arial",16,"bold"), text = "French Fries", bd=16, anchor = "w")
lblFries.grid(row=1,column=0)
txtFries = Entry(f1, font = ("arial",16,"bold"), textvariable = Fries, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtFries.grid(row=1,column=1)

lblBurger = Label(f1, font = ("arial",16,"bold"), text = "Beef Burger", bd=16, anchor = "w")
lblBurger.grid(row=2,column=0)
txtBurger = Entry(f1, font = ("arial",16,"bold"), textvariable = Burger, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtBurger.grid(row=2,column=1)

lblKebab = Label(f1, font = ("arial",16,"bold"), text = "Hot Kebab", bd=16, anchor = "w")
lblKebab.grid(row=3,column=0)
txtKebab = Entry(f1, font = ("arial",16,"bold"), textvariable = Kebab, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtKebab.grid(row=3,column=1)

lblChicken = Label(f1, font = ("arial",16,"bold"), text = "Fried Chicken", bd=16, anchor = "w")
lblChicken.grid(row=4,column=0)
txtChicken = Entry(f1, font = ("arial",16,"bold"), textvariable = Chicken, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtChicken.grid(row=4,column=1)

lblSmokies= Label(f1, font = ("arial",16,"bold"), text = "Hot Smokies", bd=16, anchor = "w")
lblSmokies.grid(row=5,column=0)
txtSmokies = Entry(f1, font = ("arial",16,"bold"), textvariable = Smokies, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtSmokies.grid(row=5,column=1)

#Resto info 2
lblDrinks = Label(f1, font = ("arial",16,"bold"), text = "Fruit Juice", bd=16, anchor = "w")
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1, font = ("arial",16,"bold"), textvariable = Drinks, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtDrinks.grid(row=0,column=3)

lblCost = Label(f1, font = ("arial",16,"bold"), text = "Cost of Meal", bd=16, anchor = "w")
lblCost.grid(row=1,column=2)
txtCost = Entry(f1, font = ("arial",16,"bold"), textvariable = Cost, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtCost.grid(row=1,column=3)

lblService = Label(f1, font = ("arial",16,"bold"), text = "Service Charge", bd=16, anchor = "w")
lblService.grid(row=2,column=2)
lblService = Entry(f1, font = ("arial",16,"bold"), textvariable = Service_Charge, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
lblService.grid(row=2,column=3)

lblStateTax = Label(f1, font = ("arial",16,"bold"), text = "Tax", bd=16, anchor = "w")
lblStateTax.grid(row=3,column=2)
txtStateTax = Entry(f1, font = ("arial",16,"bold"), textvariable = Tax, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtStateTax.grid(row=3,column=3)

lblSubTotal = Label(f1, font = ("arial",16,"bold"), text = "Sub Total", bd=16, anchor = "w")
lblSubTotal.grid(row=4,column=2)
txtSubTotal = Entry(f1, font = ("arial",16,"bold"), textvariable = SubTotal, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1, font = ("arial",16,"bold"), text = "Total Cost", bd=16, anchor = "w")
lblTotalCost.grid(row=5,column=2)
txtTotalCost  = Entry(f1, font = ("arial",16,"bold"), textvariable = Total, bd=10, insertwidth = 4, bg = "black", fg = "white",justify = "right")
txtTotalCost .grid(row=5,column=3)

#Buttons
btnTotal = Button(f1,padx =16, pady =8, bd = 16, fg ="black",font = ("arial",16,"bold"), width = 10,
                  text = "Total",bg = "#029402", command = Ref).grid(row=7, column=1)

btnReset = Button(f1,padx =16, pady =8, bd = 16, fg ="black",font = ("arial",16,"bold"), width = 10,
                  text = "Reset",bg = "#fff", command = Reset).grid(row=7, column=2)

btnExit = Button(f1,padx =16, pady =8, bd = 16, fg ="black",font = ("arial",16,"bold"), width = 10,
                  text = "Exit",bg = "#f51010", command = qExit).grid(row=7, column=3)

root.mainloop()