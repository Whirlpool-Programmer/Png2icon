'''import required modules:'''
import tkinter
import os
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox

'''functions:'''

#function to convert the png to icon
def convert_to_ico(path,output):
    global fileno
    filepath = path
    if os.path.exists(filepath) == True:
        if os.path.isfile(filepath) == True:
            image = Image.open(filepath)
            image.save("{}Icon-{}.ico".format(output,fileno), format = 'ICO')
            tkinter.messagebox.showinfo("File conversion successful", "Your Png file \"{}\" has been successfully converted to an Icon file".format(filepath))
            fileno = fileno + 1
        else:
            tkinter.messagebox.showerror("Path is not a file", "\"{}\" is not a file".format(filepath))
    else:
        tkinter.messagebox.showerror("Path does not exists", "Png file's path \"{}\" does not exists".format(filepath))

#function for dialog box to select png file
def openFile(): 
    file = tkinter.filedialog.askopenfilename(defaultextension=".png", filetypes=[("PNG files","*.png")])
    path.set(file)    

#function for dialog box to select output folder
def selectFolder():
    folder = tkinter.filedialog.askdirectory()
    output_location.set(folder + "/")

'''Scripts'''
#making "app" a tkinter main window object
app = tkinter.Tk()
app.geometry('340x140')
app.title("Png to Icon")
app.wm_iconbitmap("favicon.ico")

#making tkinter variables
path = tkinter.StringVar()
output_location = tkinter.StringVar()

#giving variables initial value
fileno = 1
path.set('*.Png file location')
output_location.set('C:\\Program Files\\Whirlpool-Programmer\\Png2Icon\\Images\\')

#defining tkinter LabelFrames
loc_input = tkinter.LabelFrame(app,text = "Input Location")
loc_output = tkinter.LabelFrame(app,text = "Output location")
convert_options = tkinter.LabelFrame(app,text = "Conversion Options")

#giving tkinter LabelFrames their locations
loc_input.grid(row=0,column=0)
loc_output.grid(row = 3,column=0)
convert_options.grid(row = 6,column =0)

#making tkinter entries and buttons
filepath = tkinter.Entry(loc_input, textvariable=path, fg = "white", bg="blue")
outputpath = tkinter.Entry(loc_output, textvariable=output_location, fg = "white", bg="blue")
explorefile = tkinter.Button(loc_input,text='>', command=lambda:openFile(), fg='white', bg='red', height=1, width=1)
explorefolder = tkinter.Button(loc_output,text='>', command=lambda:selectFolder(), fg='white', bg='red', height=1, width=1)
convertbutton = tkinter.Button(convert_options,text='Convert', command=lambda:convert_to_ico(path.get(),output_location.get()), fg='white', bg='green', height=1, width=30)

#giving tkinter entries and buttons their locations
filepath.grid(columnspan=1, ipadx=100)
outputpath.grid(columnspan=1, ipadx=100)
explorefile.grid(row=0, column=2)
explorefolder.grid(row=0, column=2)
convertbutton.grid(row = 0,column = 0)

'''Mainloop'''
#running the tkinter object "app"'s mainloop:
app.mainloop()
