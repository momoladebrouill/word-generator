from essai3 import create
import tkinter as tk
import time
from tkinter import messagebox

def produce():
  global mot
  mot.set(create())
  isenregist.set('')

  
  
def write(mot):
  try:
    momo=open('memorables palabres.txt','r')
    t=momo.read()
    momo.close()
  except:
    t=''
  momories=open('memorables palabres.txt','w')
  momories.write(t+'\n'+str(int(time.time()))+': '+mot)
  momories.close()
  isenregist.set('Done')
  #messagebox.showinfo(message='Mot enregistré dans "memorables palabres.txt"')
f=tk.Tk()
mot=tk.StringVar(f,create())
isenregist=tk.StringVar(f,'')
tk.Label(f,text='~~ Le générateur de palabres ~~',font='Consolas 25 bold').pack(pady=10)
tk.Label(f,text="Par l'ultime momoladebrouill",font='Consolas 15 italic').pack()
tk.Label(f,textvariable=mot,font='Helvetica 25',fg='red').pack()
bas=tk.Frame(f)
bas.pack(pady=10)
tk.Button(bas,text='Générer',command=produce).grid(row=0,column=0)
tk.Button(bas,text='Enregistrer',command=lambda:write(mot.get())).grid(row=0,column=1)
tk.Label(bas,textvariable=isenregist).grid(row=0,column=2)
f.mainloop()
