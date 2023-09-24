import tkinter as tk
import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo
window=tk.Tk()

def Courier():
	T["font"]=("Courier" , 15)


def roman():
	T["font"]=("Roman" , 15)

def system():
	T["font"]=("System" , 15)

def italic():
	T["font"]=("italic" , 15)

def bold():
	T["font"]=("bold" , 18)

def feedback():
	webbrowser.open("https://krishnadua.github.io/PROJECT---CRICKET/INDEX.HTML")

def Gold():
	T["bg"]="gold"

def White():
	T["bg"]="white"
	
def LightGreen():
	T["bg"]="lightgreen"
	
def Blue():
	T["bg"]="lightblue"
	
def Open():
	text=tk.Text(window)
	text.pack()
	
	text.bind('<Control-v>', lambda _:'break')
  

	text.bind('<Control-c>', lambda _:'break')
  

	text.bind('<BackSpace>', lambda _:'break')
  
	
	filetypes=(
('text files' ,  ' *.txt') , 
("All files" , ".")
	)
	
	f=fd.askopenfile(filetypes=filetypes)
	T.insert('1.0',f.readlines())
   

	
def Save():
	window.title("krishna_dua")
	f = asksaveasfile(initialfile = 'Untitled.txt',
defaultextension=".txt",filetypes=[("All Files","."),("Text Documents","*.txt")])



#main window

window.title("Krishna_Dua")

menubar=Menu(window)
window.config(menu=menubar)

File_menu = Menu(menubar)

File_menu.add_command(
label="Open",command=Open
)
File_menu.add_separator()

File_menu.add_command(
label="Save",command=Save
)

menubar.add_cascade(
label="File" , menu=File_menu
)

# Text on window

T = Text(window,height=43)
T.pack()

# Second Menubar

help_menu=Menu(menubar)

help_menu.add_command(label="White",command=White)

help_menu.add_separator()

help_menu.add_command(label="Green",command=LightGreen)

help_menu.add_separator()

help_menu.add_command(label="Blue",command=Blue)

help_menu.add_separator()

help_menu.add_command(label="gold",command=Gold)

menubar.add_cascade(
label="Colours" , menu=help_menu
)

# Third Menubar

Exit_menu = Menu(menubar)

Exit_menu.add_command(label="Close" , command=window.destroy)

menubar.add_cascade(
label="Exit" , menu=Exit_menu
)

# fourth menubar

help= Menu(menubar)

help.add_command(label="Feedback" , command=feedback)

menubar.add_cascade(
label="Help" , menu=help
)

# fifth menubar

font= Menu(menubar)

font.add_command(label="bold" , command=bold)

font.add_separator()

font.add_command(label="italic" , command=italic)

font.add_separator()

font.add_command(label="system" , command=system)

font.add_separator()

font.add_command(label="roman" , command=roman)

font.add_separator()

font.add_command(label="Courier" , command=Courier)

menubar.add_cascade(
label="font" , menu=font
)

window.mainloop()