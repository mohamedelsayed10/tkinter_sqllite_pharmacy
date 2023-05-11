import tkinter as tk
import subprocess
import os

def run_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), f'{script_name}.py')
    subprocess.run(['python', script_path])
    root.destroy()  # Close the window when the button is clicked

root = tk.Tk()
root.title(" Pharmacy Managment System(Home)")
root.attributes('-fullscreen', True)

root.configure(bg='black')
root.geometry("400x300")  # Set the window size

button_names = ['MANGER', 'missing', 'product', 'staff', 'CUSTOMER', 'SUPPLIES']

for name in button_names:
    button = tk.Button(root, text=name, command=lambda script_name=name: run_script(script_name), bg='red', width=20, height=2)
    button.pack(pady=10)
button6=tk.Button(root,text='Close', bg='red', width=20, height=2,command=root.destroy)
button6.pack(pady=10)
root.mainloop()
