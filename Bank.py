#imports :33
import tkinter as tk
from tkinter import*
from tkinter import ttk
import os
from tkinter import font
from PIL import ImageTk, Image

#Main Screen
root = Tk()
root.title("BH bank managment")
root.attributes('-fullscreen', True)
root.config(bg= "#FFFFFF")



def registered_succ():
    root.deiconify()
    register_screen.destroy()
    re_success = Toplevel(root)
    re_success.title("Registering Completed")
    re_success.geometry("450x200+750+300")
    re_success.overrideredirect(True)
    re_success.config(bg= "#FFFFFF")

    Label (re_success,text= "Account Created Successfully!!", font= ("Calibri", 22), fg= "blue", bg= "#FFFFFF").place(x= 225, y= 60, anchor= "center")

    Button (re_success,text= "Close",command= re_success.destroy, font= ("Calibri", 18), width= 10, bg= "#FFFFFF").place(x= 225, y= 150, anchor= "center")

    


#Functions
def finish_reg():
   
    global notif

    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    
    
    x= False

    if name == "" or age == "" or gender == "" or password == "":
        Label (register_screen, font= ("Calibri", 20), bg= "#FFFFFF",fg= "red", width= 30, text= "All Feilds Are Required * ").place(x= 450, y= 750, anchor= "center")
        return
    for name_check in all_accounts:
        if name == name_check:
            Label (register_screen, font= ("Calibri", 20), bg= "#FFFFFF",fg= "red", width= 30, text= "Account Already Exists").place(x= 450, y= 750, anchor= "center")
            return
            x= False
        else:
            new_file = open("DataBase\data_" + name, "w")
            new_file.write(name + "\n")
            new_file.write(password + "\n")
            new_file.write(gender + "\n")
            new_file.write(age + "\n")
            new_file.write("0")
            new_file.close()
            
            x = True
    if x:
        registered_succ()
                

def register_back():
    root.deiconify()
    register_screen.destroy()
    

def register():

    #vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global register_screen

    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Register screen
    root.withdraw()
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.attributes('-fullscreen', True)
    register_screen.config(bg= "#FFFFFF")


    #image imports
    global img1
    
    img1 = Image.open("Data\secure1.png")
    img1 = img1.resize((600, 600))
    img1 = ImageTk.PhotoImage(img1)
    Label (register_screen, image= img1,).place(x= 1400, y= 500, anchor= "center")

    #Labels
    Label (register_screen, text= "Please Enter Your Details Below", font= ("Calibri", 22), bg= "#FFFFFF").place(x= 450, y= 150, anchor= "center")
    Label (register_screen, text= "Name", font= ("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 300, anchor= "center")
    Label (register_screen, text= "Age", font= ("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 400, anchor= "center")
    Label (register_screen, text= "Gender", font= ("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 500, anchor= "center")
    Label (register_screen, text= "Password", font= ("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 600, anchor= "center")

    #Entries
    Entry (register_screen,textvariable= temp_name, width= 30, font= ("Calibri", 20), bg= "#FCFBFB").place(x= 550, y= 300, anchor= "center")
    Entry (register_screen,textvariable= temp_age, width= 30, font= ("Calibri", 20), bg= "#FCFBFB").place(x= 550, y= 400, anchor= "center")

     #gender
    choices = ["Male", "Female"]
    variable = StringVar(root)
    variable.set("Male")
    ttk.Combobox(register_screen, values = choices,state= "readonly", textvariable= temp_gender,width= 29, font= ("Calibri", 20)).place(x= 550, y= 500, anchor= "center")
    
    Entry (register_screen,textvariable= temp_password, show= "*", width= 30, font= ("Calibri", 20), bg= "#FCFBFB").place(x= 550, y= 600, anchor= "center")
    #buttons
    Button(register_screen, text="Register", command= finish_reg, font=("Calibri",16), width= 25, bg= "#FFFFFF").place(x= 450, y= 850, anchor= "center")
    Button(register_screen, text="Back", command= register_back, font=("Calibri",16), width= 25, bg= "#FFFFFF").place(x= 450, y= 925, anchor= "center")


def signout():
    root.deiconify()
    account_dashboard.destroy()


def login_session():
    #Vars
    global login_name
    global account_dashboard


    all_accounts = os.listdir(path= "DataBase")
    print(all_accounts)
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        print("works hoe")
        print(name)
        print("data_" + login_name.upper())
        if name.upper() == ("data_" + login_name).upper():
            print("works hoe 2")
            file = open("DataBase\data_" + login_name, "r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[1]
            #Account DashBoard
            if login_password == password:
                print("works hoe 3") 
                login_screen.destroy()
                account_dashboard = Toplevel(root)
                account_dashboard.title("DashBoard")
                account_dashboard.attributes("-fullscreen", True)
                account_dashboard.config(bg= "#FFFFFF")
                #image imports
                global img3
                
                img3 = Image.open("Data\secure3.png")
                img3 = img3.resize((600, 600))
                img3 = ImageTk.PhotoImage(img3)
                Label (account_dashboard, image= img3,).place(x= 1400, y= 500, anchor= "center")

                #Label
                Label (account_dashboard, text= "Account Dashboard", font= ("Calibri", 22), bg= "#FFFFFF").place(x= 450, y= 150, anchor= "center")
                Label (account_dashboard, text= "Welcome " + name[5: ], font= ("Calibri", 20), bg= "#FFFFFF").place(x= 450, y= 200, anchor= "center")

                #Buttons
                Button (account_dashboard, text= "Personal Details",font= ("Calibri", 16), width= 25, command= personal_details, bg= "#FFFFFF").place(x= 450, y= 450, anchor= "center")
                Button (account_dashboard, text= "Deposit",font= ("Calibri", 16), width= 25, command= deposit, bg= "#FFFFFF").place(x= 450, y= 550, anchor= "center")
                Button (account_dashboard, text= "Withdraw",font= ("Calibri", 16), width= 25, command= withdraw, bg= "#FFFFFF").place(x= 450, y= 650, anchor= "center")
                Button (account_dashboard, text= "Sign Out",font= ("Calibri", 16), width= 25,command= signout, bg= "#FFFFFF").place(x= 450, y= 750, anchor= "center")
            
                
                return
            else:
                login_notif.config(fg= "red", text= "Password Is Incorrect!")
            return
    login_notif.config(fg= "red", text= "User Does Not Exist!")


def finish_deposit():
    if amount.get() == "":
        Label (deposit_screen,text= "Amount Is Required", font=("Calibri", 20), fg= "red", bg= "#FFFFFF", width= 30).place(x= 450, y=500, anchor= "center")
        return
    if float(amount.get()) <= 0:
        Label (deposit_screen,text= "Deposit Should Be More Than 0", font=("Calibri", 20), fg= "red", bg= "#FFFFFF", width= 30).place(x= 450, y=500, anchor= "center")
        return
    file = open("DataBase\data_" + login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    Label (deposit_screen, text="Current Balance :" + str(updated_balance) + " DT", fg= "blue", width= 30, font=("Calibri", 19), bg= "#FFFFFF").place(x= 86, y= 350, anchor= "w")
    Label (deposit_screen,text= "Balance Updated", font=("Calibri", 20), fg= "blue", bg= "#FFFFFF").place(x= 450, y=500, anchor= "center")



def deposit_back():
    account_dashboard.deiconify()
    deposit_screen.destroy()


def deposit():
    #Vars
    global amount
    global deposit_notif
    global deposit_screen

    amount = StringVar()
    file = open("DataBase\data_" + login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    #deposit screen
    deposit_screen = Toplevel(root)
    deposit_screen.title("Deposit")
    deposit_screen.attributes("-fullscreen", True)
    deposit_screen.config(bg= "#FFFFFF")
    account_dashboard.withdraw()
    
    #image imports
    global img4
    
    img4 = Image.open("Data\secure4.png")
    img4 = img4.resize((600, 600))
    img4 = ImageTk.PhotoImage(img4)
    Label (deposit_screen, image= img4,).place(x= 1400, y= 500, anchor= "center")

    #Labels
    Label (deposit_screen, text="Deposit", font=("Calibri", 28), bg= "#FFFFFF").place(x= 420, y=150, anchor= "center")
    Label (deposit_screen, text="Curent Balance: " + details_balance + " DT",width= 30, font=("Calibri", 19), bg= "#FFFFFF").place(x= 86, y= 350, anchor= "w")
    Label (deposit_screen, text="Amount: ", font=("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 400, anchor= "center")
    Label(deposit_screen,text= "notif", font=("Calibri", 20))

    #Entry
    Entry(deposit_screen, textvariable=amount, font= ("Calibri", 20), width= 10, bg= "#FCFBFB").place(x= 550, y= 400, anchor= "center")

    #Button
    Button(deposit_screen, text="Deposit", font=("Calibri", 20), command=finish_deposit, width= 25, bg= "#FFFFFF").place(x= 450, y=600, anchor= "center")
    Button(deposit_screen, text="Back", font=("Calibri", 20), command=deposit_back, width= 25, bg= "#FFFFFF").place(x= 450, y=675, anchor= "center")


def withdraw_back():
    account_dashboard.deiconify()
    withdraw_screen.destroy()

def finish_withdraw():
    if withdraw_amount.get() == "":
        Label (withdraw_screen,text= "Amount Is Required", font=("Calibri", 20), fg= "red", bg= "#FFFFFF", width= 30).place(x= 450, y=500, anchor= "center")

        return
    if float(withdraw_amount.get()) <= 0:
        Label (withdraw_screen,text= "Withdraw Should Be More Than 0", font=("Calibri", 20), fg= "red", bg= "#FFFFFF", width= 30).place(x= 450, y=500, anchor= "center")

        return
    file = open("DataBase\data_" + login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]

    if float(withdraw_amount.get()) > float(current_balance):
        Label (withdraw_screen,text= "Insufficent Funds", font=("Calibri", 20), fg= "red", bg= "#FFFFFF", width= 30).place(x= 450, y=500, anchor= "center")

        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    Label (withdraw_screen,text= "Balance Updated", font=("Calibri", 20), fg= "blue", bg= "#FFFFFF").place(x= 450, y=500, anchor= "center")
    Label (withdraw_screen, text="Curent Balance: " + str(updated_balance) + " DT",width= 30, font=("Calibri", 19), bg= "#FFFFFF", fg= "blue").place(x= 86, y= 350, anchor= "w")
    


def withdraw():
    #Vars
    global withdraw_amount
    global withdraw_screen

    withdraw_amount = StringVar()
    file = open("DataBase\data_" + login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_balance = user_details[4]

    #deposit screen
    withdraw_screen = Toplevel(root)
    withdraw_screen.title("Withdraw")
    withdraw_screen.attributes("-fullscreen", True)
    withdraw_screen.config(bg= "#FFFFFF")
    account_dashboard.withdraw()
    
    #image imports
    global img4
    
    img4 = Image.open("Data\secure4.png")
    img4 = img4.resize((600, 600))
    img4 = ImageTk.PhotoImage(img4)
    Label (withdraw_screen, image= img4,).place(x= 1400, y= 500, anchor= "center")

    #Labels
    Label (withdraw_screen, text="Withdraw", font=("Calibri", 28), bg= "#FFFFFF").place(x= 420, y=150, anchor= "center")
    Label (withdraw_screen, text="Curent Balance: " + details_balance + " DT",width= 30, font=("Calibri", 19), bg= "#FFFFFF").place(x= 86, y= 350, anchor= "w")
    Label (withdraw_screen, text="Amount: ", font=("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 400, anchor= "center")
    Label (withdraw_screen,text= "notif", font=("Calibri", 20))

    #Entry
    Entry (withdraw_screen, textvariable=withdraw_amount, font= ("Calibri", 20), width= 10, bg= "#FCFBFB").place(x= 550, y= 400, anchor= "center")

    #Button
    Button (withdraw_screen, text="Withdraw", font=("Calibri", 20), command=finish_withdraw, width= 25, bg= "#FFFFFF").place(x= 450, y=600, anchor= "center")
    Button (withdraw_screen, text="Back", font=("Calibri", 20), command=withdraw_back, width= 25, bg= "#FFFFFF").place(x= 450, y=675, anchor= "center")

def personal_back():
    account_dashboard.deiconify()
    personal_details_screen.destroy()

def personal_details():
    #Vars
    global personal_details_screen

    file = open("DataBase\data_" + login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_name = user_details[0]
    details_age = user_details[3]
    details_gender = user_details[2]
    details_balance = user_details[4]

    #personal details sceen
    personal_details_screen = Toplevel(root)
    personal_details_screen.title("Personal Details")
    personal_details_screen.attributes("-fullscreen", True)
    personal_details_screen.config(bg= "#FFFFFF")
    account_dashboard.withdraw()

    #image imports
    global img5
    
    img5 = Image.open("Data\secure5.png")
    img5 = img5.resize((600, 600))
    img5 = ImageTk.PhotoImage(img5)
    Label (personal_details_screen, image= img5,).place(x= 1400, y= 500, anchor= "center")



    #Buttons
    Button (personal_details_screen, text="Back", font=("Calibri", 20), command=personal_back, width= 25, bg= "#FFFFFF").place(x= 420, y=750, anchor= "center")

    #Label
    Label (personal_details_screen, text= "Personal Details", font= ("Calibri", 28), bg= "#FFFFFF").place(x= 420, y=150, anchor= "center")
    Label (personal_details_screen, text= "Name: " + details_name, font= ("Calibri", 20), bg= "#FFFFFF").place(x= 270, y= 300, anchor= "w")
    Label (personal_details_screen, text= "Age: " + details_age, font= ("Calibri", 20), bg= "#FFFFFF").place(x= 270, y= 400, anchor= "w")
    Label (personal_details_screen, text= "Gender: " + details_gender, font= ("Calibri", 20), bg= "#FFFFFF").place(x= 270, y= 500, anchor= "w")
    Label (personal_details_screen, text= "Blance: " + details_balance + " DT", font= ("Calibri", 20), bg= "#FFFFFF").place(x= 270, y= 600, anchor= "w")
    

def login_back():
    root.deiconify()
    login_screen.destroy()

def login():
    #vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name = StringVar()
    temp_login_password = StringVar()
    
    #login screen
    root.withdraw()
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.attributes('-fullscreen', True)
    login_screen.config(bg= "#FFFFFF")

    #images
    global img2

    img2 = Image.open("Data\secure2.png")
    img2 = img2.resize((600, 600))
    img2 = ImageTk.PhotoImage(img2)
    Label (login_screen, image= img2).place (x= 1400, y= 500, anchor= "center")

    #Labels
    Label (login_screen, text= "Login To Your Account", font= ("Calibri", 22), bg= "#FFFFFF").place(x= 450, y= 150, anchor= "center")
    Label (login_screen, text= "Name", font= ("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 450, anchor= "center")
    Label (login_screen, text= "Password", font= ("Calibri", 19), bg= "#FFFFFF").place(x= 200, y= 550, anchor= "center")
    login_notif = Label (login_screen, font= ("Calibri", 19))

    #Entries-
    Entry (login_screen, textvariable = temp_login_name, width= 30, font= ("Calibri", 20), bg= "#FCFBFB").place(x= 550, y= 450, anchor= "center")
    Entry (login_screen, textvariable = temp_login_password, show= "*", width= 30, font= ("Calibri", 20), bg= "#FCFBFB").place(x= 550, y= 550, anchor= "center")

    #buttons
    Button(login_screen, text="Login",command= login_session,width= 25, font=("Calibri",16), bg= "#FFFFFF").place(x= 450, y= 850, anchor= "center")
    Button(login_screen, text="Back",command= login_back,width= 25, font=("Calibri",16), bg= "#FFFFFF").place(x= 450, y= 925, anchor= "center")
    


#image imports
global img
    
img = Image.open("Data\secure.png")
img = img.resize((600, 600))
img = ImageTk.PhotoImage(img)
Label (root, image= img,).place(x= 1400, y= 500, anchor= "center")




#Labels
Label (root, text = "BH Bank Banking System", font = ("Calibri", 28), bg= "#FFFFFF").place(x= 495, y= 300, anchor="center")
Label (root, text = "Number 1 Bank In Tunisia", font = ("Calibri", 24), bg= "#FFFFFF").place(x= 495, y= 360, anchor="center")

#Buttons
Button (root, text= "Register", font=("Calibri", 16), width=25, command= register, bg= "#FFFFFF").place(x= 495, y= 600, anchor="center")
Button (root, text= "Login", font=("Calibri", 16), width=25, command= login, bg= "#FFFFFF").place(x= 495, y= 700, anchor="center")
Button (root, text= "Exit", font=("Calibri", 16), width= 25,command= root.destroy, bg= "#FFFFFF").place(x= 495, y= 800, anchor="center")


root.mainloop()