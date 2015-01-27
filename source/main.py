from tkinter import *
root = Tk()

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


#Edit menu - Undo, Redo, Cut, Copy and Paste 
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", compound=LEFT,  image=undoicon,
                     accelerator='Ctrl+Z')
editmenu.add_command(label="Redo", compound=LEFT,  image=redoicon,
                     accelerator='Ctrl+Y')
editmenu.add_separator() 
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon,
                     accelerator='Ctrl+X')
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon,
                     accelerator='Ctrl+C')
editmenu.add_command(label="Paste", compound=LEFT, image=pasteicon,
                     accelerator='Ctrl+V')
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
clrschms = {
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
for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice)
menubar.add_cascade(label="View", menu=viewmenu)

# About menu - Aboutus, Help
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About")
aboutmenu.add_command(label="Help")
menubar.add_cascade(label="About",  menu=aboutmenu)

root.config(menu=menubar)

root.mainloop()