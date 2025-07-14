import tkinter as tk
from tkinter import messagebox

# def submit():
#     gender = gender_var.get()
#     selected_hobbies = []
#     if hobby_reading.get():
#         selected_hobbies.append("Reading")
#     if hobby_traveling.get():
#         selected_hobbies.append("Traveling")
#     if hobby_coding.get():
#         selected_hobbies.append("Coding")

#     selected_country = country_var.get()

#     messagebox.showinfo("Selection", f"Gender: {gender}\n"
#                                      f"Hobbies: {', '.join(selected_hobbies)}\n"
#                                      f"Country: {selected_country}")




def changeLabel():

    dynamicLabel.set("Mohak Gupta")

root = tk.Tk()
root.title("Tkinter Radio, Checkbox, Dropdown")
root.geometry("300x400")



dynamicLabel = tk.StringVar(value='')

dlabel = tk.Label(root, textvariable=dynamicLabel )

dlabel.pack()

tk.Button(root, text="Change Label", command=changeLabel).pack(pady=10)


# tk.Label(root, text="Select Gender:").pack(anchor='w')
# gender_var = tk.StringVar(value="Male")
# tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor='w')
# tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor='w')

# tk.Label(root, text="\nSelect Hobbies:").pack(anchor='w')
# hobby_reading = tk.BooleanVar()
# hobby_traveling = tk.BooleanVar()
# hobby_coding = tk.BooleanVar()
# tk.Checkbutton(root, text="Reading", variable=hobby_reading).pack(anchor='w')
# tk.Checkbutton(root, text="Traveling", variable=hobby_traveling).pack(anchor='w')
# tk.Checkbutton(root, text="Coding", variable=hobby_coding).pack(anchor='w')

# tk.Label(root, text="\nSelect Country:").pack(anchor='w')
# country_var = tk.StringVar(value="India")
# dropdown = tk.OptionMenu(root, country_var, "India", "USA", "UK", "Australia")
# dropdown.pack(anchor='w')

# tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
