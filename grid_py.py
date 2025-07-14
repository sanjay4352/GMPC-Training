import tkinter as tk


root = tk.Tk()
symbol_list=['+','-','*','/']

first_number=0
operator=''

def numberKeyClick(val):
    old_val = entry.get()
    if old_val in symbol_list:
        old_val = ''
    entry.delete(0,tk.END)
    entry.insert(0,old_val+str(val))

def actionButtonClick(op):
    global first_number
    global operator
    first_number = entry.get()
    operator = op
    entry.delete(0,tk.END)
    entry.insert(0,op)

def equalsToClick():
    print("clicked")
    second_number = int(entry.get())
   
    if operator == '+':
        entry.delete(0,tk.END)
        entry.insert(0,str(int(first_number)+second_number))
    if operator == '-':
        entry.delete(0,tk.END)
        entry.insert(0,str(int(first_number)-second_number))
    if operator == '*':
        entry.delete(0,tk.END)
        entry.insert(0,str(int(first_number)*second_number))
    if operator == '/':
        entry.delete(0,tk.END)
        entry.insert(0,str(int(first_number)/second_number))

    
    old_history = entry_history.get()
    entry_history.insert(0,str(old_history)+str(first_number)+operator+str(second_number))
         

root.geometry("300x500")
root.title("Calculator")
entry=tk.Entry(bg="white",width=200, font=('Arial',16,'bold') )
entry_history=tk.Entry(bg="white",width=200, font=('Arial',16,'bold') )
button1=tk.Button(root,text="1", padx=12, pady=10, width=2, command=lambda:numberKeyClick(1) )
button2=tk.Button(root,text="2", padx=12, pady=10, width=2, command=lambda:numberKeyClick(2))
button3=tk.Button(root,text="3", padx=12, pady=10, width=2, command=lambda:numberKeyClick(3))
button4=tk.Button(root,text="4", padx=12, pady=10, width=2  , command=lambda:numberKeyClick(4))
button5=tk.Button(root,text="5", padx=12, pady=10,  width=2 , command=lambda:numberKeyClick(5))
button6=tk.Button(root,text="6", padx=12, pady=10,  width=2 , command=lambda:numberKeyClick(6))
button7=tk.Button(root,text="7", padx=12, pady=10,  width=2 , command=lambda:numberKeyClick(7))
button8=tk.Button(root,text="8", padx=12, pady=10,  width=2 , command=lambda:numberKeyClick(8))
button9=tk.Button(root,text="9", padx=12, pady=10,  width=2 , command=lambda:numberKeyClick(9))
button0=tk.Button(root,text="0", padx=12, pady=10,  width=2 , command=lambda:numberKeyClick(0))
buttoneq=tk.Button(root,text="=", padx=12, pady=10,  width=2, command=equalsToClick )
button1add=tk.Button(root,text="+", padx=12, pady=10,  width=2, command=lambda:actionButtonClick('+') )
button1sub=tk.Button(root,text="-", padx=12, pady=10,  width=2, command=lambda:actionButtonClick('-') )
button1mul=tk.Button(root,text="*", padx=12, pady=10,  width=2 , command=lambda:actionButtonClick('*'))
button1div=tk.Button(root,text="/", padx=12, pady=10,  width=2 , command=lambda:actionButtonClick('/'))


# root.rowconfigure([0,1,2],weight=1)
# root.columnconfigure([0,1,2,3,4,5],weight=1)

entry_history.grid(row=0,column=0, columnspan=40, ipadx=10, ipady=25 )
entry.grid(row=1,column=0, columnspan=40, ipadx=10, ipady=25 )
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)


button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)


button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)

button0.grid(row=5,column=0)
buttoneq.grid(row=5,column=1)
button1add.grid(row=5,column=2)


button1sub.grid(row=6,column=0)
button1mul.grid(row=6,column=1)
button1div.grid(row=6,column=2)
# button0.grid(row=4,column=2)





root.mainloop()