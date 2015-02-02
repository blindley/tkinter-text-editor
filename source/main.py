from tkinter import *
root = Tk()
root.geometry('350x350')

def undo():
    textPad.event_generate("<<Undo>>")

def redo():
    textPad.event_generate("<<Redo>>")

def cut():
    textPad.event_generate("<<Cut>>")

def copy():
    textPad.event_generate("<<Copy>>")

def paste():
    textPad.event_generate("<<Paste>>")

def makeicon(name):
    return PhotoImage(file='icons/' + name + '.gif')

newicon = makeicon('new_file')
openicon = makeicon('open_file')
saveicon = makeicon('Save')
cuticon = makeicon('Cut')
copyicon = makeicon('Copy')
pasteicon = makeicon('Paste')
undoicon = makeicon('Undo')
redoicon = makeicon('Redo')

menubar = Menu(root)

# File menu,for open,save,save as and quit
filemenu = Menu(menubar, tearoff=0 ) 
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT,
                     image=newicon, underline=0  )
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT,
                     image=openicon, underline =0)
filemenu.add_command(label="Save", accelerator='Ctrl+S',compound=LEFT,
                     image=saveicon,underline=0)
filemenu.add_command(label="Save as",accelerator='Shift+Ctrl+S')
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator='Alt+F4') 
menubar.add_cascade(label="File", menu=filemenu)

# config menu
configmenu = Menu(menubar, tearoff=0 ) 
configmenu.add_command(label="Language", underline=0)
configmenu.add_command(label="Editor", underline=0)
configmenu.add_command(label="Project", underline=0)
menubar.add_cascade(label="Config", menu=configmenu)


#Edit menu - Undo, Redo, Cut, Copy and Paste 
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", compound=LEFT,  image=undoicon,
                     accelerator='Ctrl+Z', command=undo)
editmenu.add_command(label="Redo", compound=LEFT,  image=redoicon,
                     accelerator='Ctrl+Y', command=redo)
editmenu.add_separator() 
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon,
                     accelerator='Ctrl+X', command=cut)
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon,
                     accelerator='Ctrl+C', command=copy)
editmenu.add_command(label="Paste", compound=LEFT, image=pasteicon,
                     accelerator='Ctrl+V', command=paste)
editmenu.add_separator()
editmenu.add_command(label="Find",underline= 0, accelerator='Ctrl+F')
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator='Ctrl+A')
menubar.add_cascade(label="Edit", menu=editmenu)


#View menu - 
viewmenu = Menu(menubar, tearoff=0)
showln = IntVar()
showln.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=showln)
showinbar = IntVar()
showinbar.set(1)
viewmenu.add_checkbutton(label="Show Info Bar at Bottom", variable=showinbar)
hltln = IntVar()
viewmenu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0, variable=hltln)
themesmenu = Menu(menubar, tearoff=0)
viewmenu.add_cascade(label="Themes", menu=themesmenu)

#we define a color scheme dictionary containg name and color code as key value pair
color_schemes = {
'1. Default White': 'FFFFFF',
'2. Greygarious Grey':'D1D4D1',
'3. Lovely Lavender':'E1E1FF' , 
'4. Aquamarine': 'D1E7E0',
'5. Bold Beige': 'FFF0E1',
'6. Cobalt Blue':'333AA',
'7. Olive Green': '5B8340',
}
themechoice= StringVar()
themechoice.set('1. Default White')
for k in sorted(color_schemes):
    themesmenu.add_radiobutton(label=k, variable=themechoice)
menubar.add_cascade(label="View", menu=viewmenu)

# About menu - Aboutus, Help
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About")
aboutmenu.add_command(label="Help")
menubar.add_cascade(label="About",  menu=aboutmenu)

root.config(menu=menubar)

shortcutbar = Frame(root, height=25, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()