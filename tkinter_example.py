import tkinter as tk # tkinter module import as tk, as is for aliases. you can write anything that you want

root = tk.Tk()
root.geometry("800x600")
root.title("My Notepad") # Window's title

textEntry = tk.Entry(root,show="*")
textField = tk.Text(root, height=2, width=20)
checkBtn = tk.Checkbutton(root)
radioBtn = tk.Radiobutton(root)

textEntry.grid(row=0, column=0)
textField.grid(row=1, column=1)
btn = tk.Button(root,text="CLick Here", background="red", padx=20, pady=20)

btn.grid(row=2,column=0)

# textEntry.pack() # pack will place the element at center of row
# textField.pack()

root.mainloop()