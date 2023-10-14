import tkinter as tk

# Setup the window
window=tk.Tk()
window.title(" Tkinter Test ")
window.geometry("600x400")
newlabel = tk.Label(text = "A simple label")
newlabel.grid(column=0,row=0)

# Main loop
window.mainloop()