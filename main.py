'''import required modules:'''
import platform
import webbrowser
import tkinter
import os
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox

changelog_contents = """

v2.0:
- The program creates a folder if it does not exists
- The default output folder is set to "./images" (a folder named "images" in the program's folder) instead of "C:/Program files/Whirlpool-Programmer/Png2Ico/"
- Added the feature to change the output file's name when it is saved
- Added a defined height and width of the windows and made it not - resizable
- Changed the program theme to "Lite Blue" instead of the standard white
- Added Menu-Bar for accessing special commands
- Special Commands:
	- Help Menu:
		- Website (http://www.github.com/whirlpool-programmer/png2ico)
		- Changelog (complete changes record)
		- About (Information of the software)
	- Report Menu:
		- Report Issues (Report the problems and issues with the software on the GitHub page)

v1.0 :
Initial Release
"""

terms = """
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

'''functions:'''

#function to convert the png to icon
def convert_to_ico(path,output,filename):
    global fileno
    filepath = path
    if os.path.exists(filepath) == True:
        if os.path.isfile(filepath) == True:
            image = Image.open(filepath)
            if os.path.isdir(output):
                image.save("{}{}.ico".format(output,filename), format = 'ICO')    
            else:
                os.makedirs(output)
                image.save("{}//{}.ico".format(output,filename), format = 'ICO')
            messagebox.showinfo("File conversion successful", "Your Png file \"{}\" has been successfully converted to an Icon file".format(filepath))
            fileno = fileno + 1
            output_name.set('Icon-{}'.format(fileno))
        else:
            messagebox.showerror("Path is not a file", "\"{}\" is not a file".format(filepath))
    else:
        messagebox.showerror("Path does not exists", "Png file's path \"{}\" does not exists".format(filepath))

#function for dialog box to select png file
def openFile(): 
    file = filedialog.askopenfilename(defaultextension=".png", filetypes=[("PNG files","*.png"),("All Files","*.*")])
    path.set(file)    

#function for dialog box to select output folder
def selectFolder():
    folder = filedialog.askdirectory()
    if folder == os.path.curdir:
        output_location.set(os.path.curdir + "/")
    elif folder != os.path.curdir:
        output_location.set(folder + "/")

#function for the changelog
def changelog():
    clog = tkinter.Toplevel(bg = "#0084FF")
    clog.title("Changelog")
    clog.resizable(False, False)
    log_head = tkinter.Label(clog,text = "Changelog", font = ("Segoe",20),fg = "white", bg = "#0084FF")
    log_head.grid()
    print(changelog_contents)
    log = tkinter.Label(clog, text = changelog_contents, font = ("Segoe", 12), fg = "white", bg = "#0084FF", justify = tkinter.LEFT)
    log.grid()
    clog.mainloop()

#function for the about
def about():
    window = tkinter.Toplevel(bg = "#0084FF")
    window.title("About Png2Ico")
    window.resizable(False, False)
    head = tkinter.Label(window, text = "Png2Ico 2.0", font = ("Segoe", 20),fg = "white", bg = "#0084FF")
    head.grid()
    texts = tkinter.Label(window, text = "Running on {}\nMade on Python 3.7.0\n\n(c) 2021 Whirlpool-Programmer\n{}\n\nThe Tkinter Feather Logo is a copyright to PSF (Python Software Foundations)\nVersion 2.0\nBuild 65".format(platform.platform(),terms), font = ("Segoe",10),fg = "white", bg = "#0084FF")
    texts.grid()
    
    window.mainloop()

'''Scripts'''
#making "app" a tkinter main window object
app = tkinter.Tk()
app.geometry('340x350')
app.title("Png2Icon 2.0")
app.resizable(False, False)
app.config(bg="#0084FF")

#making tkinter variables
path = tkinter.StringVar()
output_name = tkinter.StringVar()
output_location = tkinter.StringVar()

#giving variables initial value
fileno = 1
path.set('*.png')
output_name.set('Icon-{}'.format(fileno))
output_location.set('{}\\Images\\'.format(os.path.curdir))


Menubar = tkinter.Menu(app, activebackground ="#0084FF", activeforeground = "#FFFFFF",bg = "#FFFFFF", fg = "#0084FF" ,font = "Segoe")

Filemenu = tkinter.Menu(Menubar, tearoff = 0)
Filemenu.add_command(label="Choose File", command=openFile)
Filemenu.add_command(label="Choose Output Folder", command = selectFolder)
Filemenu.add_separator()
Filemenu.add_command(label="Convert", command = lambda:convert_to_ico(path.get(),output_location.get(),output_name.get()))
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=app.destroy)
Menubar.add_cascade(label="File", menu=Filemenu)

Helpmenu = tkinter.Menu(Menubar, tearoff = 0)
Helpmenu.add_command(label = "Website", command=lambda:webbrowser.open("http://www.github.com/Whirlpool-Programmer/Png2Ico"))
Helpmenu.add_separator()
Helpmenu.add_command(label = "Changelog", command=changelog)
Helpmenu.add_command(label = "About",command = about)
Menubar.add_cascade(label = "Help", menu=Helpmenu)

Reportmenu = tkinter.Menu(Menubar, tearoff=0)
Reportmenu.add_command(label="Report Issues", command = lambda:webbrowser.open("http://www.github.com/whirlpool-programmer/png2ico/issues"))
Menubar.add_cascade(label="Report", menu=Reportmenu)

#making tkinter entries, labels and buttons
info = tkinter.Label(app,text = "Png2Icon 2.0",font = (("sans-sherif"),25),bg="#0084FF",fg="White")
i =tkinter.Label(app,text = "\n\nINPUT",bg="#0084FF",fg="white")
o =tkinter.Label(app,text = "\nOUTPUT",bg="#0084FF",fg="white")
fpi = tkinter.Label(app,text = "Png file location:",fg = "blue",bg = "#0084FF")
filepath = tkinter.Entry(app, textvariable=path, fg = "#0084FF", bg="white")
oni = tkinter.Label(app,text = "output file name:",fg = "blue", bg="#0084FF")
outputname = tkinter.Entry(app, textvariable=output_name, fg="#0084FF", bg = "white")
opi = tkinter.Label(app,text = "output folder location:",fg = "blue",bg="#0084FF")
outputpath = tkinter.Entry(app, textvariable=output_location, fg = "#0080FF", bg="white")
explorefile = tkinter.Button(app,text='>', command=lambda:openFile(), fg='white', bg='blue', height=1, width=1)
explorefolder = tkinter.Button(app,text='>', command=lambda:selectFolder(), fg='white', bg='blue', height=1, width=1)
convertbutton = tkinter.Button(app,text='Convert', command=lambda:convert_to_ico(path.get(),output_location.get(),output_name.get()), fg='white', bg='green', height=1, width=30)
txt1 = tkinter.Label(app,text="",bg="#0084FF")

#giving tkinter entries and buttons their locations
info.grid(row=0,column=0)
i.grid(row=1,column=0)
fpi.grid(row =2,column = 0)
filepath.grid(columnspan=1, ipadx=100)
o.grid(row=4,column=0)
oni.grid(row =5,column = 0)
outputname.grid(columnspan=1,ipadx=100)
opi.grid(row =7,column = 0)
outputpath.grid(columnspan=1, ipadx=100)
explorefile.grid(row=3, column=2)
explorefolder.grid(row=8, column=2)
txt1.grid(row =9,column =0)
convertbutton.grid(row =10,column = 0)

'''Mainloop'''
#running the tkinter object "app"'s mainloop:
app.config(menu = Menubar)
app.mainloop()
