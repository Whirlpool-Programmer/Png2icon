import os
from tkinter import *
from PIL import Image

def convert_to_ico(path):
    filepath = path
    if os.path.exists(filepath) == True:
        if os.path.isfile(filepath) == True:
            if Windows == 1:
                pxs = [()]
            image = Image.open(filepath)
            image.save("PNG.ico", format = 'ICO',sizes=pxs)
            messagebox.showinfo("File conversion successful", "Your PNG file \"{}\" has been successfully converted to an ICO file".format(filepath))
        else:
            messagebox.showerror("Path is not a file", "\"{}\" is not a file".format(filepath))
    else:
        messagebox.showerror("Path does not exists", "PNG file's path \"{}\" does not exists".format(filepath))
        
app = Tk()
app.geometry('323x500')
app.title("PNG to ICO")

path = StringVar()

label = Label( app, text="")
label.grid(row=1,column=0)

filepath = Entry(app, textvariable=path, bg="gray")
filepath.grid(columnspan=1, ipadx=100)

path.set('Path to PNG file')

convertbutton = Button(app,text='Convert to ICO', command=lambda:convert_to_ico(path.get()), fg='black', bg='gray', height=1, width=30)
convertbutton.grid(row=10, column=0)

mb = Menubutton ( app, text="System", relief = "ridge",fg = 'black', bg = 'gray')
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
Windows  = IntVar()
MacOS    = IntVar()
iOS      = IntVar()
Linux    = IntVar()
Android  = IntVar()
WinPhone = IntVar()
favicon  = IntVar()
mb.menu.add_checkbutton ( label="Windows",
                          variable=Windows )
mb.menu.add_checkbutton ( label="macOS",
                          variable=MacOS )
mb.menu.add_checkbutton ( label="Linux",
                          variable=Linux )
mb.menu.add_checkbutton ( label="Android",
                          variable=Android )
mb.menu.add_checkbutton ( label="Windows Phone",
                          variable=WinPhone )
mb.menu.add_checkbutton ( label="iOS",
                          variable=iOS)
mb.menu.add_checkbutton ( label="favicon",
                          variable=favicon )

app.mainloop()
