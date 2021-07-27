import tkinter as tk
from tkinter import Canvas, Label, filedialog,Text
import os

root = tk.Tk()
root.title("Opener")

apps= []


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempapps = f.read()
        tempapps = tempapps.split('\n')
        apps = [x for x in tempapps if x.strip() ]


def addApp():

    for widget in  frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/",title = "Select file" , filetypes = (("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app,bg='gray',padx=5,pady=5)
        label.pack()




def run():
    for app in apps:
        os.startfile(app)

Canvas = tk.Canvas(root, width=600, height=600, bg='#263D42')
Canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor='center')

openFile = tk.Button(root, text="Open File", padx=10,pady=5,fg="white",bg="#263D42" , command=addApp)
openFile.pack()

runsapp = tk.Button(root, text="Run App", padx=10,pady=5,fg="white",bg="#263D42",command=run)
runsapp.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
root.mainloop()

with open("save.txt","w") as f:
    for app in apps:
        f.write(app+"\n")