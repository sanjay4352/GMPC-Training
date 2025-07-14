import tkinter as tk
from tkinter import messagebox
import json
import random
class BankApp:
    def __init__(self,root):
        self.root =root
        self.dashboard()
    def primaryButton(self,text, command):
        button = tk.Button(self.root,text=text, bg="yellow", fg="#000", font=("Arial",16,"bold"), command=command )
        return button
    def openAccount(self):
        # root = tk.Tk()
        self.clearWindow()
        self.root.title("Open Account")
        label_name = tk.Label(self.root,text="Name")
        self.entry_name = tk.Entry(self.root)
        label_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)

        
        label_phone = tk.Label(self.root,text="Phone Number")
        self.entry_phone = tk.Entry(self.root)
        label_phone.grid(row=1, column=0)
        self.entry_phone.grid(row=1, column=1)

        
        label_age = tk.Label(self.root,text="Age")
        self.entry_age = tk.Entry(self.root)
        label_age.grid(row=2, column=0)
        self.entry_age.grid(row=2, column=1)

        submit_button = self.primaryButton("Submit", command=self.submitAccountForm)
        submit_button.grid(row=3, column=1)
    
        pass

    def submitAccountForm(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        age = self.entry_age.get()
        account_number = random.randint(100000,999999999)

        if len(phone)==10:
            
            account = {
                "account_number":account_number,
                "name":name,
                "phone":phone,
                "age":age,
                "balance":0
            }

            file = open("bank_account.txt","w")
            json.dump(fp=file, obj=account)
            messagebox.showinfo(title="Account Opening", message="You account has been open, with account number: "+str(account_number))
            self.dashboard()
        else:
            messagebox.showerror(title="Account Opening Error", message="Invalid Phone Number")



        pass

    def clearWindow(self):
        list = self.root.winfo_children()
        for x in list:
            x.destroy()

    def login():
        pass

    def deposit(self):

        self.clearWindow()
        self.root.title("Deposit Window")

        
        label_deposit = tk.Label(self.root,text="Enter Amount to be Deposit: ")
        self.entry_depost = tk.Entry(self.root)
        label_deposit.grid(row=0, column=0)
        self.entry_depost.grid(row=0,column=1)

        
        submit_button = self.primaryButton("Submit", command=self.submitDeposit)
        submit_button.grid(row=1, column=1)


        pass

    def submitDeposit(self):
        file = open("bank_account.txt","r")
        account = json.load(fp=file)
        old_bal = float(account["balance"])
        deposit_bal = float(self.entry_depost.get())

        final_bal = old_bal+deposit_bal
        account["balance"] = final_bal
        
        file = open("bank_account.txt","w")
        json.dump(fp=file, obj=account)
        messagebox.showinfo(title="Deposit", message="Deposit Successful")
        self.dashboard()


        pass

    def dashboard(self):
        # root = tk.Tk()
        self.clearWindow()
        self.root.title("Dashboard")
        open_account_button = self.primaryButton("Open Account", command=self.openAccount)
        login_button =  self.primaryButton("Login", command=self.login)
        deposit_button =  self.primaryButton("Deposit", command=self.deposit)
        open_account_button.grid(row=0,column=0)
        login_button.grid(row=0,column=1)       
        deposit_button.grid(row=0,column=2) 
        pass
root = tk.Tk()
root.geometry("600x400")
bank = BankApp(root)
root.mainloop()



