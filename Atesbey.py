import os
import tkinter

tke = tkinter.Tk()
tke.title("PYTHON MODULLERİ")


tke.geometry(f"{400}x{200}")
button1 = tkinter.Button(tke, text=("dowland pygame!"),background="yellow", command=lambda: os.system("pip install pygame"))
button2 = tkinter.Button(tke, text=("dowland colorama!"),background="yellow", command=lambda: os.system("pip install colorama"))
button3 = tkinter.Button(tke, text=("dowland pygamezero!"),background="yellow", command=lambda: os.system("pip install pgzero"))
button5 = tkinter.Button(tke, text=("dowland pillow!"),background="yellow", command=lambda: os.system("pip install pillow"))
button4 = tkinter.Button(tke, text=("dowland rich!"),background="yellow", command=lambda: os.system("pip install rich"))
button4.pack()
button5.pack()
button2.pack()
button3.pack()
button1.pack()

try:
    import pygame
    button1.config(text="pygame yüklü!",background="green")
except ImportError:
    print("pygame yüklencek!")
try:
    import colorama
    button2.config(text="colorama yüklü!",background="green")
except ImportError:
    print("colorama yüklencek!")
try:
    import pygame
    button3.config(text="pgzero yüklü!",background="green")
except ImportError:
    print("pgzero yüklencek!")
try:
    import pygame
    button4.config(text="rich yüklü!",background="green")
except ImportError:
    print("rich yüklencek!")
try:
    import pygame
    button5.config(text="pillow yüklü!",background="green")
except ImportError:
    print("pillow yüklencek!")
    

tke.mainloop()