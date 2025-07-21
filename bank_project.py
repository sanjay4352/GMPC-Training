import tkinter as tk
from tkinter import messagebox
import random
import json
class BankApplication:

    def __init__(self,root):
        self.root = root
    
    def openAccount(self):
        self.clearWindow()
        self.root.title("Open Account")
        
        nameLabel =tk.Label(self.root,text="Enter Your Name: ")
        self.nameEntry = tk.Entry(self.root,text="Name")
        nameLabel.grid(row=0,column=0)
        self.nameEntry.grid(row=0,column=1)

        phoneLabel =tk.Label(self.root,text="Enter Your phone: ")
        self.phoneEntry = tk.Entry(self.root,text="phone")
        phoneLabel.grid(row=1,column=0)
        self.phoneEntry.grid(row=1,column=1)


        addressLabel =tk.Label(self.root,text="Enter Your address: ")
        self.addressEntry = tk.Entry(self.root,text="address")
        addressLabel.grid(row=2,column=0)
        self.addressEntry.grid(row=2,column=1)

        submitBtn = tk.Button(self.root,text="Submit Details", background="red", command=self.getOpenAccountFormData)

        submitBtn.grid(row=4,column=1)
      
    
    def getOpenAccountFormData(self):
        name = self.nameEntry.get()
        phone = self.phoneEntry.get()
        address = self.addressEntry.get()
        canSave=True
        if name =="":
            canSave=False
            messagebox.showerror(title="Account Openig Error",message="Kindly enter your name")
        if len(phone)!=10:
            canSave=False
            messagebox.showerror(title="Account Openig Error",message="Kindly enter valid phone number")
        if address =="":
            canSave=False
            messagebox.showerror(title="Account Openig Error",message="Kindly enter your address")

        if canSave:
            account={
                "name":name,
                "phone":phone,
                "address":address,
                "balance":0,
                "account_number":random.randint(1000000000,9999999999)
            }
            
            file = open("mybank.txt","w")

            json.dump(fp=file,obj=account)

            messagebox.showinfo(title="Account Opening ",message="You account has been open")
            self.dashboard()


    def deposit(self):
        self.clearWindow()

        amountLabel =tk.Label(self.root,text="Enter Deposit Amount: ")
        self.amountEntry = tk.Entry(self.root,text="Amount")
        amountLabel.grid(row=2,column=0)
        self.amountEntry.grid(row=2,column=1)

        submitBtn = tk.Button(self.root,text="Submit Details", background="red", command=self.depositAmount)

        submitBtn.grid(row=4,column=1)
        
    
    def depositAmount(self):
        amount = self.amountEntry.get()
        file = open("mybank.txt","r")
        data=json.load(fp=file)
        data['balance'] += float(amount)
        file1 = open("mybank.txt","w")
        json.dump(fp=file1,obj=data)
        messagebox.showinfo(title="Account Deposit ",message="Deposit successful")
        self.dashboard()



    def withdrawl(self):
        self.clearWindow()

        amountLabel =tk.Label(self.root,text="Enter Withdrawl Amount: ")
        self.amountEntry = tk.Entry(self.root,text="Amount")
        amountLabel.grid(row=2,column=0)
        self.amountEntry.grid(row=2,column=1)

        submitBtn = tk.Button(self.root,text="Submit Details", background="red", command=self.withdrawlAmount)

        submitBtn.grid(row=4,column=1)
    
    def withdrawlAmount(self):
        amount = self.amountEntry.get()
        file = open("mybank.txt","r")
        data=json.load(fp=file)
        data['balance'] -= float(amount)
        file1 = open("mybank.txt","w")
        json.dump(fp=file1,obj=data)
        messagebox.showinfo(title="Account Withdrawl ",message="Withdrawl successful")
        self.dashboard()

    def viewBalance(self):
        file = open("mybank.txt","r")
        data=json.load(fp=file)
        
        messagebox.showinfo(title="Account Balance ",message=f"You account balance is {data['balance']}")
        


    def clearWindow(self):
        list = self.root.winfo_children()
        for x in list:
            x.destroy()

    def dashboard(self):
        self.clearWindow()
        self.root.title("Dashboard")
        openAccountBtn = tk.Button(self.root,text="Open Account", background="red", command=self.openAccount)
        openAccountBtn.grid(row=0,column=0)

        depositBtn = tk.Button(self.root,text="Deposit", background="red", command=self.deposit)
        depositBtn.grid(row=0,column=1)
        withdrawltBtn = tk.Button(self.root,text="Withdrawal", background="red", command=self.withdrawl)
        withdrawltBtn.grid(row=0,column=2)
        viewBtn = tk.Button(self.root,text="View Balance", background="red", command=self.viewBalance)
        viewBtn.grid(row=0,column=3)




root = tk.Tk()
root.geometry("600x400")
root.title("Bank Application")





bank = BankApplication(root)
bank.dashboard()

tk.mainloop()
