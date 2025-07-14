import tkinter as tk

root = tk.Tk()
root.title("Label Example")

root.geometry("300x400")

def myFunction():
    dynamicVar.set("Value is being changed")


dynamicVar = tk.StringVar(value='This is label')
label = tk.Label(root,textvariable=dynamicVar)
label.pack()
button= tk.Button(root,text="My Button", command=lambda:myFunction())
button.pack()

root.mainloop()