import tkinter as tk


def openAccount():
    root = tk.Tk()
    root.title("Account Opening Form")
    root.geometry("400x600")
    root.mainloop()


def dashboard():
    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("800x400")
    button = tk.Button(root,text="Open Account", command=lambda:openAccount())
    button.pack()

    root.mainloop()


dashboard()